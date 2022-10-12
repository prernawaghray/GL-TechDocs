from curses import ALL_MOUSE_EVENTS
from datetime import datetime
from decimal import Decimal
from symbol import not_test
from telnetlib import STATUS
from sqlalchemy import Column, Integer, String, Text, DateTime, Index, Date, Boolean, DECIMAL
from sqlalchemy import UniqueConstraint

from Base import Base

class PaymentAccount(Base):
    __tablename__ = "PaymentAccounts"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)
    UserId          = Column(String(256))
    IsDefault       = Column(Boolean)
    AccType         = Column(String(50))
    AccName         = Column(String(256))
    AccNumber       = Column(Integer(20))
    AccCvv          = Column(Integer(4))
    AccExpiry       = Column(Date)
    AccIFSC         = Column(String(128))
    Version         = Column(Integer)
    s_Misc1         = Column(String(1024))
    s_Misc2         = Column(String(1024))
    n_Misc1         = Column(Integer)
    n_Misc2         = Column(Integer)
        
    #Index("idx_PA_User", UserId)

    # Constructors to insert data 
    #def __init__(self, UserId):

#############################
class UserPayment(Base):
    __tablename__ = "UserPayments"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)
    UserId          = Column(String(256))
    PaidDate        = Column(DateTime)
    Amount          = Column(Decimal(65,30))
    PayAccountId    = Column(Integer)
    PaymentMethod   = Column(String(128))
    Status          = Column(String(50))
    Notes           = Column(Text)
    Version         = Column(Integer)
    s_Misc1         = Column(String(1024))
    s_Misc2         = Column(String(1024))
    n_Misc1         = Column(Integer)
    n_Misc2         = Column(Integer)
        
    #Index("idx_UP_UserDate", UserId, PaidDate)

    # Constructors to insert data 
    #def __init__(self, UserId):

#############################
class UserSubscription(Base):
    __tablename__ = "UserSubscriptions"

    RecordId        = Column(Integer, primary_key=True, autoincrement=True)
    UserId          = Column(String(256))
    Type            = Column(String(5))
    TypeDesc        = Column(String(128))
    Status          = Column(String(1))
    ExpiryDate      = Column(datetime)
    Version         = Column(Integer)
    s_Misc1         = Column(String(1024))
    s_Misc2         = Column(String(1024))
    n_Misc1         = Column(Integer)
    n_Misc2         = Column(Integer)
        
    #Index("idx_US_User", UserId)

    # Constructors to insert data 
    #def __init__(self, UserId):