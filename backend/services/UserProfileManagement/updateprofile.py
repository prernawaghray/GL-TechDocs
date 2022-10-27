# Updateprofile.py 
''' this file receives json file containing the  user profile details to be updated. This includes 
firstname, lastname, street address, state, country, occupation and purpose of use. 
Process: When the post method is called, first the user authentication is verified.
After the JWT token is verified, the entered userdetails are obtained and updated in the UserProfile Database.
On succesful Updation "OK" is being sent, else "error message" is sent.

'''

from flask import Blueprint, current_app, jsonify
from flask import request,make_response
from flask_bcrypt import Bcrypt
from . import *
import jwt
from flask import jsonify
from datetime import datetime
import pytz,json
from DBConnect import session_factory
from orm_Tables import User
from sqlalchemy import create_engine, select, update
from flask_bcrypt import Bcrypt
from orm_Tables import UsersProfile
from ..UserAuthentication.JWTAuthentication import authentication


updateUserProfile_bp = Blueprint('updateprofile',__name__)


@updateUserProfile_bp .route('/api/updateProfile',methods=['GET', 'POST'])
#check for user authorisation
@authentication
def updateProfile(user_id):
    if request.method == 'POST':
        requestparams = json.loads(request.data) #reading the parameters to update
        userData = requestparams["userData"]
        emailId = user_id
        firstName = userData["firstName"]
        lastName = userData["lastName"]
        address = requestparams["address"]
        streetAddress = address["streetAddress"]
        state = address["state"]
        country = address["country"]
        occupation = requestparams["occupation"]
        purposeOfUsage = requestparams["purposeOfUse"]
        #Updating to database
        session = session_factory()
        sql_stmt = (update(UsersProfile).where(UsersProfile.Id == emailId).values(firstName=firstName,lastName = lastName,streetAddress = streetAddress,state = state, country = country, occupation = occupation, purposeOfUsage = purposeOfUsage))
        session.execute(sql_stmt)
        session.commit()
        session.close()
        message = {"message":"OK"}
        return make_response(jsonify(message), 200)
    else:
            data_sent = {"message":"Error Message"} 
            return make_response(jsonify(data_sent),404)