from sqlalchemy import Column, String

from Base import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(String(256), primary_key = True)
    email_id = Column(String(256))

    def __init__(self, user_id, email_id):
        self.user_id = user_id
        self.email_id = email_id
