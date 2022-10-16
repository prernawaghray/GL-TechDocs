from sqlalchemy import Column, Integer, String, Text
import uuid

from Base import Base

class Document(Base):
    __tablename__ = "document"

    document_id = Column(Integer, primary_key = True, default=uuid.uuid4)
    document_version = Column(Integer)
    document_name = Column(String(256))
    file_path = Column(Text)

    def __init__(self, document_name, file_path):
        self.document_version = 1
        self.document_name = document_name
        self.file_path = file_path
