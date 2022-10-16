from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

class ActionEnum(enum.Enum):
    create = "create"
    edit = "edit"
    share = "share"
    delete = "delete"

from Base import Base

class UserHistory(Base):
    __tablename__ = "user_history"

    record_id = Column(Integer, primary_key = True, autoincrement=True)
    user_id = Column(String(256), ForeignKey("user.user_id"))
    user = relationship("User")
    document_id = Column(Integer, ForeignKey("document.document_id"))
    document= relationship("Document")
    document_name = Column(String(256))
    time_stamp = Column(DateTime)
    action = Column(Enum(ActionEnum))
    s_misc1 = Column( String(1024))
    s_misc2 = Column(String(1024)) 
    n_misc1 = Column(Integer)
    n_misc2 = Column(Integer)

    def __init__(self, user, document, time_stamp, document_name, action):
        self.user = user
        self.document = document
        self.time_stamp = time_stamp
        self.document_name = document_name
        self.action = action
