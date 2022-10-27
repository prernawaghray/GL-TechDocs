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

def authentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            key = current_app.config["SECRET"]
        if not token:
            return jsonify(message="token missing")
        try:
            data= jwt.decode(token, key, algorithms=["HS256"])
            session = session_factory()
            sql_stmt = (select(User.Id) .where (User.username == data["Email"]))
            user_id = session.execute(sql_stmt).first()
            
            if not user_id[0]:
                return jsonify(message="invalid token")
        except:
            return jsonify(message="error while decoding")
        return f(user_id[0], *args, **kwargs)
    return decorated