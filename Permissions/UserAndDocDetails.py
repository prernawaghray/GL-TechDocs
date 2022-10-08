from sqlalchemy import create_engine
from sqlalchemy.sql import text
import UserAndGroupPermissions as UG
engine = create_engine("mysql://root:Vedasree97@localhost:3306/userDB")
engine.connect()
def getUserId(user_email):
    sql = text("""SELECT UserId FROM UserAuthentication WHERE UserEmail=:UEmail""")
    record = {"UEmail": user_email}
    userid = engine.execute(sql, **record)
    return userid

def getDocId(userid,docname):
    sql = text("""SELECT DocId FROM Documents WHERE UserId=:UId and DocName=:DName""")
    record = {"UId":userid,"DName":docname}
    docid = engine.execute(sql, **record)
    return docid

def setPermissions(shareEmail,userid,docname):
    userId=getUserId(shareEmail)
    docId=getDocId(userid,docname)
    UG.setReadUserPermission(userId,docId)

