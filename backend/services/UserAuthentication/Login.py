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

userLogin_bp = Blueprint('login',__name__)

@userLogin_bp.route('/api/signin', methods=['GET', 'POST'])
def signin():
    bcrypt = Bcrypt(current_app)
    if request.method == 'POST':
        loginType = request.form.get('loginType')
        username  = request.form.get('username')
        password  = request.form.get('password')

        if loginType == 'google':
            session = session_factory()
            sql_stmt = (select(User.Id, User.isadmin, User.loginType).where (User.username == username))
            result = session.execute(sql_stmt).first()
            session.close()
  
            if result[0]:
                    key = current_app.config["SECRET"]
                    admin = result[1]
                    data_sent = {"Email": username,
                                "isAdmin": admin,
                                "loginType":loginType}
                    JWT_Token = jwt.encode(data_sent, key, algorithm="HS256")
                    jsondata = {"userAuthToken":JWT_Token}
                    return make_response(jsonify(jsondata), 200)
            else:
                    data_sent = {"message":"User not Registered"} 
                    return make_response(jsonify(data_sent),401)

        elif loginType == "email":
            session = session_factory()
            sql_stmt = (select(User.Id, User.isadmin, User.password, User.loginType).where (User.username == username))
            result = session.execute(sql_stmt).first()
            session.close()
                
            if result[3] == "google":
                return jsonify('User already registered', 401)

            if result[0]:   
                if bcrypt.check_password_hash(result[2], password):
                    key = current_app.config["SECRET"]
                    admin = result[1]
                    data_sent = {"Email": username,
                                    "isAdmin": admin}
                    JWT_Token = jwt.encode(data_sent, key, algorithm="HS256")
                    data_sent  =  {"userAuthToken" : JWT_Token,     
                                        "isAdmin":admin}
                    return make_response(jsonify(data_sent), 200) 
                else:
                    data_sent = {"message":"Invalid Password"} 
                    return make_response(jsonify(data_sent),401)
            else:
                data_sent = {"message":"User not Registered"} 
                return make_response(jsonify(data_sent),401)
        else:
            data_sent = {"message":"User not Registered"} 
            return make_response(jsonify(data_sent),401)
        
    else:
        data_sent = {"message":"Invalid method"} 
        return make_response(jsonify(data_sent),401)


