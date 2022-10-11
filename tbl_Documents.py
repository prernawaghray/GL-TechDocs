from sqlalchemy import Column, Integer, String, Text, DateTime, Index
from sqlalchemy import UniqueConstraint

from Base import Base

class Document(Base):
    __tablename__ = "Documents"

    DocId           = Column(Integer, primary_key=True, autoincrement=True)
    DocName         = Column(String(256))
    UserId          = Column(String(256))
    FilePath        = Column(Text)
    CreatedDate     = Column(DateTime)
    ModifiedDate    = Column(DateTime)
    ModifiedBy      = Column(String(256))      
    Version         = Column(Integer)
    s_Misc1         = Column(String(1024))
    s_Misc2         = Column(String(1024))
    n_Misc1         = Column(Integer)
    n_Misc2         = Column(Integer)
    
    UniqueConstraint(DocId, UserId)
    
    Index("idx_Doc_ByUserDoc", UserId, DocId)
    Index("idx_Doc_ByUserCreated", UserId, CreatedDate)
    Index("idx_Doc_ByUserModified", UserId, ModifiedDate)

    def __init__(self, Filename, UserId, Filepath, Datetime, Version):
        self.DocName     = Filename
        self.UserId      = UserId
        self.FilePath    = Filepath
        self.CreatedDate = Datetime
        self.Version     = Version
