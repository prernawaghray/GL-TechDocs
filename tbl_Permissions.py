from sqlalchemy import Column, Integer, String, Text, DateTime, Index, Boolean
from sqlalchemy import UniqueConstraint

from Base import Base

class Permission(Base):
    __tablename__ = "Permissions"

    PermissionId    = Column(Integer, primary_key=True, autoincrement=True)
    DocId           = Column(Integer)
    UserId          = Column(String(256))
    UserPermissions = Column(String(25))
    GroupPermissions = Column(String(25))
    OtherPermissions = Column(String(25))
    Version         = Column(Integer)
    s_Misc1         = Column(String(1024))
    s_Misc2         = Column(String(1024))
    n_Misc1         = Column(Integer)
    n_Misc2         = Column(Integer)
    
    Index("idx_Perm_ByUserDoc", UserId, DocId)

    def __init__(self, DocId, UserId, UserPermissions):
        self.DocId = DocId
        self.UserId = UserId
        self.UserPermissions = UserPermissions
