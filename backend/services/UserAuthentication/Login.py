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


@userLogin_bp.route('/check',methods=['GET','POST'])
def check():
    if(request.method == 'POST'):
        session = session_factory()
        sql_stmt = (select(User.Id).where (User.username == "test@test.com"))
        user = session.execute(sql_stmt).first()
        print(user[0])
        return make_response(jsonify({'message':'exists'}), 200)


# @userLogin_bp.route('/api/signin', methods=['GET','POST'])
# def signin():
#     # sourcery skip: assign-if-exp, reintroduce-else, swap-if-else-branches, use-named-expression
#     if request.method == 'POST':
#         login_type = request.form.get('loginType')
#         if login_type == 'google':
#             username = request.form.get('email')
#             user = User.query.filter_by(username=username).first()
#             if user:
#                 key = "secret"
#                 admin = user.isadmin
#                 data_sent = {"Email": username,
#                              "isAdmin": admin}
#                 JWT_Token = jwt.encode(data_sent, key, algorithm="HS256")
#                 jsondata = {"userAuthToken":JWT_Token}
#                 return make_response(jsonify(jsondata), 200)
#             else:
#                 data_sent = {"message":"User not Registered"} 
#                 return make_response(jsonify(data_sent),401)
#         elif login_type == 'email':
#             username = request.form.get('email')
#             password = request.form.get('password')
#             #remember_me = request.form.get('rememberMe')
#             remember = True if request.form.get('remember') else False
#             user = User.query.filter_by(username=username).first()
#             if user:
#                 if bcrypt.check_password_hash(user.password, password):
                    
#                         if (user.isadmin == 0):
#                             key = "secret"
#                             admin = user.isadmin
#                             data_sent = {"Email": username,
#                                          "isAdmin": admin}
#                             JWT_Token = jwt.encode(data_sent, key, algorithm="HS256")
#                             admin = user.isadmin
#                             data_sent  =  {"userAuthToken" : JWT_Token,     
#                                            "isAdmin":admin}
#                             return make_response(jsonify(data_sent), 200) 
                      
#                         else:
#                             key = "secret"
#                             admin = user.isadmin
#                             data_sent = {"Email": username,
#                                          "isAdmin": admin}
#                             JWT_Token = jwt.encode(data_sent, key, algorithm="HS256")
#                             admin = user.isadmin
#                             data_sent  =  {"userAuthToken" : JWT_Token,     
#                                            "isAdmin":admin}
#                             return make_response(jsonify(data_sent), 200) 
#                 else:
#                         data_sent = {"message":"Invalid Password"} 
#                         return make_response(jsonify(data_sent),401)
#             else:
#                 data_sent = {"message":"User not Registered"} 
#                 return make_response(jsonify(data_sent),401)
         
#         else:
#             data_sent = {"message":"User not Registered"} 
#             return make_response(jsonify(data_sent),401)
#     else:
#          data_sent = {"message":"User not Registered"} 
#          return make_response(jsonify(data_sent),401)
     

@userLogin_bp.route('/api/signin', methods=['GET', 'POST'])
def signin():
    bcrypt = Bcrypt(current_app)
    if request.method == 'POST':
        content  = request.get_json(silent=True)
        loginType = content['loginType']
        username  = content['username']
        password  = content['password']
        remember  = content['remember']

        if loginType == 'google':
            session = session_factory()
            sql_stmt = (select(User.Id, User.isadmin).where (User.username == username))
            result = session.execute(sql_stmt).first()
            session.close()

            if result[0]:
                key = current_app.config["SECRET"]
                admin = result[1]
                data_sent = {"Email": username,
                             "isAdmin": admin}
                JWT_Token = jwt.encode(data_sent, key, algorithm="HS256")
                jsondata = {"userAuthToken":JWT_Token}
                return make_response(jsonify(jsondata), 200)
            else:
                data_sent = {"message":"User not Registered"} 
                return make_response(jsonify(data_sent),401)

        elif loginType == "email":
            session = session_factory()
            sql_stmt = (select(User.Id, User.isadmin, User.password).where (User.username == username))
            result = session.execute(sql_stmt).first()
            session.close()

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

