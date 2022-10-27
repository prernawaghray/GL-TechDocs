from curses import ALL_MOUSE_EVENTS
from datetime import datetime
from decimal import Decimal
# from symbol import not_test
from telnetlib import STATUS
from sqlalchemy import Enum, Column, Integer, String, Text, DateTime, Index, Date, Boolean, DECIMAL, ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects import mysql 
from DBConnect import Base
from orm_Common import Common
import enum
from sqlalchemy.orm import relationship

#############################
class Document(Common):
    __tablename__ = "Documents"

    ModifiedDate    = Column(DateTime)
    ModifiedBy      = Column(String(256))      
  
############################# 
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

#############################
 
class User(Base): 
    __tablename__ = "User"
    
    Id              = Column(String(256), primary_key=True)
    username        = Column(String(256), nullable=False, unique=True)
    password        = Column(String(256), nullable=False)
    isadmin         = Column(Boolean,nullable=False)
    loginType       = Column(String(256),nullable=False)
    #user = relationship("UserPofile",backref = "user", CASCADE = 'all, delete-orphan', lazy = 'dynamic' )
    
    
    def __init__(self, Id, username, password, isadmin):
        self.Id = Id
        self.username = username
        self.password = password
        self.isadmin = isadmin
        
################################

class UserProfile(Base):
    __tablename__ = "UsersProfile"
    
    Id              = Column(Integer, primary_key=True, autoincrement=True)
    username         = Column(String(256), ForeignKey('User.username'),nullable=False, unique=True)
    firstName       = Column(String(100),nullable=True)
    lastName        = Column(String(100),nullable=True)
    streetAddress   = Column(String(256),nullable=True)
    state           = Column(String(256),nullable=True)
    country         = Column(String(256),nullable=True)
    occupation      = Column(String(256),nullable=True)
    purposeOfUsage  = Column(String(256),nullable=True)
    signUpDate      = Column(Date,nullable=True) 
    lastActiveDate  = Column(Date,nullable=True) 

    def __init__(self, Id, userID, firstName,lastName,streerAddress,state,country,occupation,purposeOfUsage,signUpDate,lastActiveDate):
        self.Id    = Id
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streerAddress
        self.state = state
        self.country = country
        self.occupation = occupation
        self.purposeOfUsage = purposeOfUsage
        self.signUpDate = signUpDate
        self.lastActiveDate = lastActiveDate