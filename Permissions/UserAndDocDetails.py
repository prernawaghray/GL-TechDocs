from sqlalchemy import create_connect
from sqlalchemy.sql import text
import UserAndGroupPermissions as UG
engine = create_connect("mysql://root:Vedasree97@localhost:3306/userDB")
connect=engine.connect()
def getUserId(user_email):
    sql = text("""SELECT UserId FROM UserAuthentication WHERE UserEmail=:UEmail""")
    record = {"UEmail": user_email}
    userid = connect.execute(sql, **record)
    return userid

def getDocId(userid,docname):
    sql = text("""SELECT DocId FROM Documents WHERE UserId=:UId and DocName=:DName""")
    record = {"UId":userid,"DName":docname}
    docid = connect.execute(sql, **record)
    return docid

def setPermissions(shareEmail,userid,docname):
    userId=getUserId(shareEmail)
    docId=getDocId(userid,docname)
    UG.setReadUserPermission(userId,docId)

