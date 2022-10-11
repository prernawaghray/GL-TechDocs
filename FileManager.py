# Libraries
import os
import warnings
import yaml
import requests
from datetime import datetime
from xml.dom.xmlbuilder import DocumentLS 
from flask import Flask, render_template, url_for, redirect, session, flash, request, jsonify, json
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Base import session_factory
from tbl_Documents import Document
#from Users import User

# Suppress warnings
warnings.filterwarnings("ignore")

# Start flask
app = Flask(__name__)

# Flask configurations
#app.config.from_object('filemanagerapp.default_settings')
app.config.from_pyfile('config.py')

##############################################################################
# Home API for filemanager
# Check on FileManager service
@app.route('/file', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "FileManager home"
        return jsonify({'data': data})

# API to create a new file
# Input: UserId
# Processing: 
# 1. Creates a sub folder with UserId in the destination directory 
# 2. Creates a file name suffixed with date time string 
# 3. Copies this file name to the above folder
# 4. Create an entry into Documents table
# Output: UserId & Filename with empty data
@app.route('/file/create', methods = ['GET', 'POST'])
def file_create():
    userid   = ''
    docid    = ''
    filename = ''
    if(request.method == 'POST'):
        # request data
        content  = request.get_json(silent=True)
        userid   = content['UserId']
        # process
        datestr  = datetime.today().strftime('%Y%m%d%H%M%S')
        dirpath  = app.config['DEST_FOLDER'] + '/' + userid 
        filename = 'untitled_'+datestr+'.tex'
        filepath = dirpath+'/'+filename
        #ver = api_call_to_get_document_version
        
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        
        open(filepath, 'a').close()
        
        # Save it in the database - by using table object
        session = session_factory()
        doc_entry = Document(filename, userid, filepath, datetime.today(), 1)
        session.add(doc_entry)
        session.flush()
        docid_out = doc_entry.DocId
        session.commit()
        session.close()
    
    #Return the json object to the caller
    data_out = json.dumps({'UserId':userid, 'DocumentId':docid_out, "Filename":filename, "body":""})
    return jsonify(message='success', data=data_out)

# Driver function
if __name__ == "__main__":
    app.run(debug=True)
    

