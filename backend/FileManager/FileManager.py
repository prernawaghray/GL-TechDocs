# Libraries
import os
import warnings
import logging
import yaml
import requests
from functools import singledispatchmethod
from datetime import datetime
from xml.dom.xmlbuilder import DocumentLS 
from flask import Flask, render_template, url_for, redirect, session, flash, request, jsonify, json
import sqlalchemy as db
from sqlalchemy import create_engine, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DBConnect import session_factory
from orm_Tables import Document
#from Users import User
#from Services.FileManager.permissions import *

# Suppress warnings
warnings.filterwarnings("ignore")

# Get logging filepath
with open('config.yaml') as stream:
    configs = yaml.safe_load(stream)

# Data foler 
data_path = configs["DIR_ROOT"] + configs["DIR_DATA"] 
# Initiate logging 
log_path = configs['DIR_ROOT'] + configs['DIR_LOG']
logging.basicConfig(filename=log_path)
# Start flask
app = Flask(__name__)

# Flask configurations
app.config.from_object(configs)

# Class to handle common file related processes
class FileManage:
    v_filename =''
    v_filepath =''
        
    @classmethod
    def createNewFile(cls, userid, filename):
        datestr  = datetime.today().strftime('%Y%m%d%H%M%S')
        dirpath  = data_path + '/' + userid
        if (filename == ""):
            filename = 'untitled_'+datestr+'.tex'
        filepath = dirpath+'/'+filename
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        cls.v_filename = filename
        cls.v_filepath = filepath

##############################################################################
# Home API for filemanager
# Check on FileManager service
@app.route('/file', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "FileManager home. Allowed endpoints are /file/create ; /file/modify ; /file/delete"
        return jsonify({'data': data})

# API to create a new file
# Input: UserId, DocName (if)
# Processing: 
# 1. Creates a sub folder with UserId in the destination directory 
# 2. Creates a file name suffixed with date time string 
# 3. Copies this file name to the above folder
# 4. Create an entry into Documents table
# Output: UserId, DocId, DocName, Filename, body
@app.route('/file/create', methods = ['GET', 'POST'])
def file_create():
    userid   = ''
    docid    = ''
    filename = ''
    data_out = ''
    mess_out = ''
    
    app.logger.info("Service file/create initiated")
    if(request.method == 'POST'):
        # request data
        content  = request.get_json(silent=True)
        userid   = content['UserId']
        docname  = content['DocName']
        # processing request
        file_obj = FileManage()
        file_obj.createNewFile(userid, docname)
        #TODO: ver = api_call_to_get_document_version
        ver = 1
        
        open(file_obj.v_filepath, 'a').close()
        
        # Save it in the database - by using table object
        try:
            session = session_factory()
            doc_entry = Document(userid, file_obj.v_filename, file_obj.v_filepath, datetime.today(), ver)
            session.add(doc_entry)
            session.flush()
            docid_out = doc_entry.DocId
            session.commit()
            session.close()
            
            data_out = json.dumps({'UserId':userid, 'DocId':docid_out, 'DocName':file_obj.v_filename, 'DocText':""})
            mess_out = 'success'
        except Exception:
            mess_out = 'fail'
            app.logger.exception("Failure Creating File!")
    app.logger.info("Service file/create ended")
    
    #Return the json object to the caller
    return jsonify(message=mess_out, data=data_out)

# API to modify a file
# Inputs: UserId, DocId, DocName, Document data, Operation = modify/rename
# Processing: 
# 1. Checks & retrieves the document's file path, database entry
# 2. If DocId is not retrieved or modify operation, will create a new file in the back end and save the URL
# 2.a. URL is saved into DocumentHistory & Document tables
# 3. If save operation: will finally re-write the latest file edited then save the URL
# Output:
# UserId, DocId, DocName, DocText
@app.route('/file/modify', methods = ['GET', 'POST'])
def file_modify():
    app.logger.info("Service file/modify initiated")
    data_out = ''
    mess_out = ''

    if(request.method == 'POST'):
        # retrieve data inputs from the request
        content   = request.get_json(silent=True)
        userid    = content['UserId']
        docid     = content['DocId']
        docname   = content['DocName']
        doctext   = content['Doctext']
        operation = content['Operation']
        
        #TODO: call the method to know permission
        # check for user permissions
        userperm = 'w' #get_user_permissions(userid, docid)
        
        try:
            # User has write permission
            if(userperm == 'w'):
                if (operation == 'update') or (operation == "save"):
                    #TODO: get version number
                    session = session_factory()
                    sql_stmt = select(Document.DocName, Document.FilePath).where(Document.DocId == docid)
                    sql_result = session.execute(sql_stmt)
                    session.close()
                    
                    #TODO: also save into document history table
                
                    # there is always only 1 row
                    for row in sql_result:
                        filepath = row.FilePath
                    
                    # update the text file
                    if (os.path.exists(filepath)) or (operation == "save"):
                        file_obj = open(filepath, "w")
                        file_obj.write(doctext)
                        file_obj.close()
                    else:
                        app.logger.error("File does not exist at the path: ", filepath)
                    
                    mess_out = 'success'
                elif (operation == 'rename'):
                    # extract the file name stripping the extension of the file
                    filename_new = docname.split(".")[0] + '.tex'
                    filepath_new = data_path + '/' + userid + '/'+ filename_new
                    
                    # update the database record
                    session = session_factory()
                    sql_stmt = update(Document).where(Document.DocId == docid).values(DocName=filename_new)
                    sql_result = session.execute(sql_stmt)
                    session.commit()
                    sql_stmt = (select(Document.FilePath, Document.FilePath).where(Document.DocId == docid))
                    sql_result = session.execute(sql_stmt)
                    session.commit()
                    session.close()
                    
                    # there is always only 1 row
                    for row in sql_result:
                        filepath = row.FilePath
                    
                    # rename the physical file
                    # rename the file
                    if os.path.exists(filepath):
                        os.rename(filepath, filepath_new)
                    # write the content to the file creating a new file
                    else:
                        file_obj = open(filepath_new, "w")
                        file_obj.write(doctext)
                        file_obj.close()        
                    
                    mess_out = 'success'
                else:
                    app.logger.error("Operation uknown: ", operation)
            else:
                raise Exception("Access to modify denied!")
        except Exception:
            mess_out = 'fail'
            app.logger.exception("Failure Modifying file!")
    
    data_out = json.dumps({'UserId':userid, 'DocId':docid, 'DocName':docname, 'DocText':doctext})
    app.logger.info("Service file/modify ended")
    return jsonify(message=mess_out, data=data_out)

#################
# Main Call
if __name__ == "__main__":
    app.run(debug=True)
    

