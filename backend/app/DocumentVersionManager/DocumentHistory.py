from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from Base import Base

class DocumentHistory(Base):
    __tablename__ = "document_history"

    record_id = Column(Integer, primary_key = True, autoincrement=True)
    user_id = Column(String(256), ForeignKey("user.user_id"))
    user = relationship("User")
    document_id = Column(Integer, ForeignKey("document.document_id"))
    document= relationship("Document")
    time_stamp = Column(DateTime)
    document_name = Column(String(256))
    file_path = Column(String(65535))
    version = Column(Integer)
    s_misc1 = Column( String(1024))
    s_misc2 = Column(String(1024)) 
    n_misc1 = Column(Integer)
    n_misc2 = Column(Integer)

    def __init__(self, user, document, time_stamp, document_name, file_path, version):
        self.user = user
        self.document = document
        self.time_stamp = time_stamp
        self.document_name = document_name
        self.file_path = file_path
        self.version = version
