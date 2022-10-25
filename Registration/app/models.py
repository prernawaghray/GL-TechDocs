from flask_sqlalchemy import SQLAlchemy
from flask import current_app, Blueprint
from datetime import datetime


models_bp = Blueprint('models', __name__)


db = SQLAlchemy(current_app)

class User(db.Model): 
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=0)
    loginType=db.Column(db.String(100))
    create_ts = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, name, loginType, email, password, is_admin=0):
        
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.loginType= loginType

db.create_all()
db.session.commit()