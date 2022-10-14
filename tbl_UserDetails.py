
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


class Occupation(Base):
    __tablename__ = "Occupation"

    OccupationId = Column(Integer, autoincrement=True)
    OccupationName = Column(String(256), primary_key=True)

    # Constructors to insert data
    # def __init__(self, UserId):


class FieldOfWork(Base):
    __tablename__ = "FieldOfWork"

    FieldId = Column(Integer, autoincrement=True)
    FieldWork = Column(String(50), primary_key=True)

    # Constructors to insert data
    # def __init__(self, UserId):


class PurposeOfUsage(Base):
    __tablename__ = "PurposeOfUsage"

    PurposeId = Column(Integer, autoincrement=True)
    Purpose = Column(String(100), primary_key=True)

    # Constructors to insert data
    # def __init__(self, UserId):


class UserProfile(Base):
    __tablename__ = "UserProfile"

    UserId = Column(String(256), ForeignKey(UserAuthentication.UserId), primary_key=True)
    FirstName = Column(String(256))
    LastName = Column(String(256))
    Address = Column(String(256))
    SignUpDate = Column(DateTime)
    lastActive = Column(DateTime)
    OccupationName = Column(String(256), ForeignKey(Occupation.OccupationName))
    FieldWork = Column(String(50), ForeignKey(FieldOfWork.FieldWork))
    Purpose = Column(String(100), ForeignKey(PurposeOfUsage.PurposeId))
    AlternateEmail = Column(String(256))

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

