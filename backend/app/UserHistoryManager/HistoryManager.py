# Libraries
import warnings
import logging
import yaml
import requests
import timeago
from datetime import date, datetime
from flask import Flask, request, jsonify, json
import sqlalchemy as db
from Base import session_factory

from UserHistory import UserHistory, ActionEnum
from User import User
from Document import Document
# from tbl_Documents import Document
#from Users import User
#from Services.FileManager.permissions import *

# Suppress warnings
warnings.filterwarnings("ignore")

# Get logging filepath
with open('config.yaml') as stream:
    configs = yaml.safe_load(stream)

# Initiate logging 
log_path = configs['DIR_ROOT'] + configs['DIR_LOG']

# Initiate logging 
logging.basicConfig(filename=log_path)
# Start flask
app = Flask(__name__)

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

def get_user_record_by_email(email):
    try: 
        session = session_factory()
        user_query = session.query(User).filter(User.email_id == email).all()
        session.close()
        if len(user_query) > 0:
            return user_query[0]
        app.logger.info("User record for email Id - " + str(email) + " doesn't exist")
        return False
    except Exception:
        app.logger.exception("Failure getting user record!")
        return False

##############################################################################
# Home API for historymanager
# Check on HistoryManager service
@app.route('/history', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "HistoryManager home. Allowed endpoints are /history/get; /history/create;"
        return jsonify({'data': data})

# API to create a new user history
# Input: UserId, DocumentId, Action, AdditionalInfo(JSON containing more info based on Action)
# For Action = share -> AdditionalInfo = {'email_id': 'abc@xyz.com'}
# Processing: 
# 1. Create an entry into UserHistory table
# Output: UserHistoryId
@app.route('/history/create', methods = ['GET', 'POST'])
def create_user_history():
    data_out = ''
    mess_out = ''
    additionalInfo = {}
    
    app.logger.info("Service history/create initiated")
    if(request.method == 'POST'):
        # request data
        content  = request.get_json(silent=True)
        user_id   = content['UserId']
        document_id  = content['DocumentId']
        action = content['Action']
        if "AdditionalInfo" in content:
            additionalInfo = content['AdditionalInfo']
        # processing request
        
        # Save it in the database - by using UserHistory object
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
                document_name = document.document_name

            user_history_record = UserHistory(user, document, datetime.now(), document_name, action)
            if action == ActionEnum.share.value:
                user_history_record.s_misc1 = additionalInfo["email_id"]

            session.add(user_history_record)
            session.flush()
            record_id = user_history_record.record_id
            session.commit()
            session.close()

            data_out = json.dumps({'UserHistoryId':record_id})
            mess_out = 'success'

        except Exception:
            mess_out = 'fail'
            app.logger.exception("Failure Creating UserHistory!")
    app.logger.info("Service history/create ended")
    
    #Return the json object to the caller
    return jsonify(message=mess_out, data=data_out)

# API to get user history
# Inputs: Email, PageNumber(if)
# Processing: 
# 1. Gets the user record for the email
# 2. Retrieves the user history records based on offset and pagesize
# 3. Convert time stamp to timeago format
# 4. If action is share, get the shared email id
# Output:
# UserId, DocId, DocName, DocText
@app.route('/history/get', methods = ['GET', 'POST'])
def get_user_history():
    app.logger.info("Service history/get initiated")
    data_out = ''
    mess_out = ''
    history_records = []

    if(request.method == 'POST'):
        # retrieve data inputs from the request
        page_size = 50
        content   = request.get_json(silent=True)
        user_email   = content['Email']
        if 'PageNumber' in content:
            page_number = content['PageNumber']
        else: 
            page_number = 0

        user_record = get_user_record_by_email(user_email)

        try :
            session = session_factory()
            user_history_query = session.query(UserHistory).filter(UserHistory.user_id == user_record.user_id).order_by(UserHistory.time_stamp.desc()).offset(page_number*page_size).limit(page_size).all()
            session.close()
            for user_history_record in user_history_query:
                shared_to = ""
                action = user_history_record.action
                if not action:
                    continue
                document_name = user_history_record.document_name
                time_stamp = timeago.format(user_history_record.time_stamp, datetime.now())
                if action == ActionEnum.share:
                    shared_to = user_history_record.s_misc1

                history_records.append({
                    "email": user_email,
                    "action": action.value,
                    "time": time_stamp,
                    "doc_name": document_name,
                    "shared_to": shared_to
                })

            data_out = json.dumps({'items':history_records})
            mess_out = "success"

        except Exception:
            mess_out = "Failed to retrieve history"
    
    app.logger.info("Service history/get ended")
    return jsonify(message=mess_out, data=data_out)

#################
# Main Call
if __name__ == "__main__":
    app.run(debug=True)
    
