from flask import Blueprint, current_app, jsonify
from flask import request,make_response
#from app.databases.database import *
from flask_bcrypt import Bcrypt
from . import *
import jwt
from flask import jsonify
from datetime import datetime
from functools import wraps
import sqlalchemy as db
from sqlalchemy import create_engine, select, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DBConnect import session_factory
from orm_Tables import User


authTokenDecode_bp = Blueprint('AuthTokenDecode',__name__)

# def AuthTokenDecode(JWT_EncodeToken):
#     print(JWT_EncodeToken)
#     if JWT_EncodeToken: 
#         key = 'secret'
#         JWT_Decode_Token = jwt.decode(JWT_EncodeToken, key, algorithms="HS256")
#         list_values = list(JWT_Decode_Token.values())
#         # print(list_values)
#         # Auth_User = User.query.filter_by(username=list_values[0]).first()
#         session = session_factory()
#         Auth_User = session.execute(select(User) .where (User.username==list_values[0]))
#         if Auth_User:
            
#             return (list_values[0],200)
#         else:
#             data_sent = {"message" : "JWT Error"} 
#             return (data_sent,404)

def authentication_json(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        key=current_app.config["SECRET"]
        content = request.get_json(silent=True)
        if content["token"]:
            token = content["token"]
        if not token:
            return jsonify(message="token missing")
        try:
            data = jwt.decode(token,key,algorithms=["HS256"])
            session = session_factory()
            user_id = session.execute(select(User.Id) .where (User.username == data["Email"])).first()
            if not user_id[0]:
                return jsonify(message="invalid token")

        except:
            return jsonify(message="error decoding")

        return f(user_id[0], *args, **kwargs)
    return decorated