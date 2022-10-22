from curses import ALL_MOUSE_EVENTS
from datetime import datetime
from decimal import Decimal
from symbol import not_test
from telnetlib import STATUS
from sqlalchemy import Column, Integer, String, Text, DateTime, Index, Date, Boolean, DECIMAL, ForeignKey, Enum
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import mysql 
from DBConnect import Base
from orm_Common import Common
import enum

class ActionEnum(enum.Enum):
    create = "create"
    edit = "edit"
    share = "share"
    delete = "delete"

#############################
class Document(Common):
    __tablename__ = "Documents"

    ModifiedDate    = Column(DateTime)
    ModifiedBy      = Column(String(256))      
  
#############################
class DocumentHistory(Common):
    __tablename__ = "DocumentHistory"

    DocId           = Column(Integer, ForeignKey("Documents.DocId"))
    UserId          = Column(String(256), ForeignKey("user.user_id"))
    RecordId        = Column(Integer, primary_key=True, autoincrement=True)    
    User            = relationship("User")
    Document        = relationship("Document")

    def __init__(self, user, document, created_date, document_name, file_path, version):
        self.User = user
        self.Document = document
        self.CreatedDate = created_date
        self.DocName = document_name
        self.FilePath = file_path
        self.Version = version

#############################
class UserHistory(Common):
    __tablename__ = "UserHistory"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)   
    UserId          = Column(String(256), ForeignKey("user.user_id"))
    User            = relationship("User")
    DocId           = Column(Integer, ForeignKey("Documents.DocId"))
    Document        = relationship("Document")
    Action          = Column(Enum(ActionEnum))


    def __init__(self, user, document, time_stamp, document_name, action):
        self.User = user
        self.Document = document
        self.CreatedDate = time_stamp
        self.DocName = document_name
        self.Action = action

############################ 
class Permission(Common):
    __tablename__ = "Permissions"

    PermissionId    = Column(Integer, primary_key=True, autoincrement=True)
    UserPermissions = Column(String(25))
    GroupPermissions = Column(String(25))
    OtherPermissions = Column(String(25))

#############################
class PaymentAccount(Common):
    __tablename__ = "PaymentAccounts"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)
    IsDefault       = Column(Boolean)
    AccType         = Column(String(50))
    AccName         = Column(String(256))
    AccNumber       = Column(mysql.INTEGER(20))
    AccCvv          = Column(mysql.INTEGER(4))
    AccExpiry       = Column(Date)
    AccIFSC         = Column(String(128))

#############################
class UserPayment(Common):
    __tablename__ = "UserPayments"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)
    PaidDate        = Column(DateTime)
    Amount          = Column(mysql.DECIMAL(65,30))
    PayAccountId    = Column(Integer)
    PaymentMethod   = Column(String(128))
    Status          = Column(String(50))
    Notes           = Column(Text)

#############################
class UserSubscription(Common):
    __tablename__ = "UserSubscriptions"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)
    Type            = Column(String(5))
    TypeDesc        = Column(String(128))
    Status          = Column(String(1))
    ExpiryDate      = Column(DateTime)
