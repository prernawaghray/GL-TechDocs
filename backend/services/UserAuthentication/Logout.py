from flask import Blueprint, current_app, jsonify
from flask import request,make_response
from flask_bcrypt import Bcrypt

from flask import Blueprint, current_app, jsonify
from flask import request,make_response
from . import *
import jwt
from flask import jsonify
import sqlalchemy as db
from sqlalchemy import create_engine, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DBConnect import session_factory
from orm_Tables import User
from flask_bcrypt import Bcrypt
from .JWTAuthentication import authentication_json
import pytz

userLogout_bp = Blueprint('logout',__name__)


# @userLogout_bp.route('/api/signout',methods=['GET', 'POST'])
# def signout():
#     if request.method == 'POST':
#         JWT_Encode_Token = (request.form.get('userAuthToken'))
#         logout_status = AuthTokenDecode(JWT_Encode_Token)
#         if logout_status[1] == 200:
#             authUser = logout_status[0]
#             currentDateTime = datetime.now(pytz.timezone('Asia/Kolkata'))
#             data_to_update = UserProfile.query.filter_by(userId=authUser).first()
#             if data_to_update:
#                 data_to_update.lastActiveDate = currentDateTime.today()
#                 db.session.commit()
#                 data_sent = {"userAuthToken":JWT_Encode_Token} 
#                 return make_response(jsonify(data_sent),200)
#             else:
#                 data_sent = {"message":"Invalid Request/No User Session"} 
#                 return make_response(jsonify(data_sent),400)
#         else:
#             data_sent = {"message":"Invalid Request/No User Session"} 
#             return make_response(jsonify(data_sent),400)
#     else:
#         return make_response(jsonify({'message':'invalid method'}))

@userLogout_bp.route('/api/signout', methods=["GET", "POST"])
@authentication_json
def signout(user_id):
    return jsonify(message=user_id)
