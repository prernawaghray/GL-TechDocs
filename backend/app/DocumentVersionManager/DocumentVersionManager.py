# Libraries
import os
import warnings
import logging
import yaml
import requests
from datetime import datetime
from flask import Flask, request, jsonify, json
from Base import session_factory

from DocumentHistory import DocumentHistory
from User import User
from Document import Document
# from tbl_Documents import Document

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

# Class to handle common version file related processes
class VersionManage:
    v_file_name =''
    v_file_path =''
        
    @classmethod
    def createNewVersionFile(cls, user_id, document_name, version, current_file_path):
        file_directory = data_path + '/' + str(user_id)
        if (document_name == ""):
            datestr  = datetime.today().strftime('%Y%m%d%H%M%S')
            document_name = 'untitled_' + datestr + 'v_' + str(version) + '.tex'
        else :
            index = document_name.index('.tex')
            document_name = document_name[:index]

        file_path = file_directory + '/' + document_name + '_v_' + str(version) + '.tex'

        if not os.path.exists(file_directory):
            os.makedirs(file_directory)

        # TODO: copy contents from old file to new file
        with open(current_file_path) as f:
            with open(file_path, "w") as f1:
                for line in f:
                    f1.write(line)

        cls.v_file_name = document_name
        cls.v_file_path = file_path


def get_document_record(document_id):
    try: 
        session = session_factory()
        document_query = session.query(Document).filter(Document.document_id == document_id).all()
        session.close()
        if len(document_query) > 0:
            return document_query[0]
        app.logger.info("Document record for document Id - " + str(document_id) + " doesn't exist")
        return False
    except Exception:
        app.logger.exception("Failure getting document id!")
        return False

def get_user_record(user_id):
    try: 
        session = session_factory()
        user_query = session.query(User).filter(User.user_id == user_id).all()
        session.close()
        if len(user_query) > 0:
            return user_query[0]
        app.logger.info("User record for user Id - " + str(user_id) + " doesn't exist")
        return False
    except Exception:
        app.logger.exception("Failure getting user record!")
        return False

def get_latest_document_version_record(document_id):
    try: 
        session = session_factory()
        document_version_query = session.query(DocumentHistory).filter(DocumentHistory.document_id==document_id).order_by(DocumentHistory.version.desc()).first()
        session.close()
        if document_version_query:
            return document_version_query[0]
        app.logger.info("Document version for doc Id - " + str(document_id) + " doesn't exist")
        return False
    except Exception:
        app.logger.exception("Failure getting document version!")
        return False



##############################################################################
# Home API for document_version_manager
# Check on DocumentVersionManager service
@app.route('/version', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "DocumentVersionManager home. Allowed endpoints are /version/create ; /version/get"
        return jsonify({'data': data})


# API to create a new version
# Input: UserId, DocumentId (if)
# Processing: 
# 1. Creates a sub folder with UserId in the destination directory 
# 2. Creates a file name suffixed with date time string 
# 3. Copies this file name to the above folder
# 4. Copies the content of Document to new file
# 5. Create an entry into Document version table
# Output: UserId, DocId, DocName

@app.route('/version/create', methods = ['GET', 'POST'])
def create_document_version():
    
    app.logger.info("Service version/create initiated")
    data_out = ''
    mess_out = ''
    if(request.method == 'POST'):
        # request data
        content  = request.get_json(silent=True)
        user_id   = content['UserId']
        document_id  = content['DocumentId']

        # processing request
        try: 
            session = session_factory()

            user = get_user_record(user_id)
            if not user:
                mess_out = "User record doesn't exist"
                return jsonify(message=mess_out, data=data_out)

            document = get_document_record(document_id)
            if (not document):
                mess_out = "Document record doesn't exist"
                return jsonify(message=mess_out, data=data_out)
            else:
                document_version = document.document_version
                document_name = document.document_name
                file_path = document.file_path
            file_version_object = VersionManage()
            file_version_object.createNewVersionFile(user_id, document_name, document_version, file_path)
            document_version_record = DocumentHistory(user, document, datetime.now(), file_version_object.v_file_name, file_version_object.v_file_path, document_version)

            session.add(document_version_record)
            session.commit()
            session.close()
            data_out = json.dumps({'UserId': user_id, 'DocId':document_id, 'DocName':file_version_object.v_file_name})

        except Exception as e:
            print(e)
            mess_out = 'fail'
            app.logger.exception("Failure Creating Version!")

    app.logger.info("Service version/create ended")
    
    #Return the json object to the caller
    return jsonify(message=mess_out, data=data_out)

# API to get latest version of a doc id
# Inputs:  DocumentId
# Processing: 
# 1. Retrieves the latest document version for the given document id
# Output:
# Version
@app.route('/version/get', methods = ['GET', 'POST'])
def get_latest_document_version():
    app.logger.info("Service version/get initiated")
    data_out = ''
    mess_out = ''

    if(request.method == 'POST'):
        # retrieve data inputs from the request
        content = request.get_json(silent=True)
        document_id = content['DocumentId']
        
        version_record = get_latest_document_version_record(document_id)
        if (not version_record):
            version =  1
        else:
            version =  version_record.version
    
    data_out = json.dumps({'DocumentId':document_id, 'Version':version})
    app.logger.info("Service version/get ended")
    return jsonify(message=mess_out, data=data_out)

#################
# Main Call
if __name__ == "__main__":
    app.run(debug=True)
    
