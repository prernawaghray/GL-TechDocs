
from sqlalchemy import Column, Integer, String, Text, DateTime, Index, Date, Boolean, DECIMAL, ForeignKey
from sqlalchemy import UniqueConstraint

from Base import Base


class UserAuthentication(Base):
    __tablename__ = "UserAuthentication"

    UserId = Column(String(256), primary_key=True, unique=True)
    UserEmail = Column(String(256), unique=True)
    Password = Column(String(256))
    IsAdmin = Column(Boolean)

    # Constructors to insert data
    # def __init__(self, UserId):


class UserProfile(Base):
    __tablename__ = "UserProfile"

    UserId = Column(String(256), ForeignKey(UserAuthentication.UserId), primary_key=True)
    FirstName = Column(String(256))
    LastName = Column(String(256))
    StreetAddress = Column(String(256))
    State = Column(String(256))
    Country = Column(String(100))
    SignUpDate = Column(DateTime)
    lastActive = Column(DateTime)
    OccupationName = Column(String(256))
    FieldWork = Column(String(256))
    Purpose = Column(String(256))

    # Constructors to insert data
    # def __init__(self, UserId):


class LinkedAccount(Base):
    __tablename__ = "LinkedAccount"

    UserId = Column(String(256), ForeignKey(UserAuthentication.UserId), primary_key=True)
    AccountType = Column(String(256))
    AccountName = Column(String(256))
    AccountPassword = Column(String(256))

    # Constructors to insert data
    # def __init__(self, UserId):

