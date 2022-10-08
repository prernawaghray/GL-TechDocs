# import os
# import mysql.connector
# from mysql.connector import connect, errorcode
from sqlalchemy import create_connect
from sqlalchemy.sql import text
from UserAndDocDetails import connect

def setReadUserPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    userpermission = connect.execute(sql, **record1)
    if userpermission == None:
        userpermission = "R"
    else:
        userpermission += "R"
    sql = text("""UPDATE Permissions SET UserPermissions=:UPId WHERE PermissionId=:PId""")
    record2 = {"UPId": userpermission, "PId": permissionid}
    connect.execute(sql, **record2)


def setWriteUserPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    userpermission = connect.execute(sql, **record1)
    if userpermission == None:
        userpermission = "W"
    else:
        userpermission += "W"
    sql = text("""UPDATE Permissions SET UserPermissions=:UPId WHERE PermissionId=:PId""")
    record2 = {"UPId": userpermission, "PId": permissionid}
    connect.execute(sql, **record2)


def setShareUserPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    userpermission = connect.execute(sql, **record1)
    if userpermission is None:
        userpermission = "S"
    else:
        userpermission += "S"
    sql = text("""UPDATE Permissions SET UserPermissions=:UPId WHERE PermissionId=:PId""")
    record2 = {"UPId": userpermission, "PId": permissionid}
    connect.execute(sql, **record2)


def setDeleteUserPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    userpermission = connect.execute(sql, **record1)
    if userpermission is None:
        userpermission = "D"
    else:
        userpermission += "D"
    sql = text("""UPDATE Permissions SET UserPermissions=:UPId WHERE PermissionId=:PId""")
    record2 = {"UPId": userpermission, "PId": permissionid}
    connect.execute(sql, **record2)


def setAnalyticsUserPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    userpermission = connect.execute(sql, **record1)
    if userpermission is None:
        userpermission = "A"
    else:
        userpermission += "A"
    sql = text("""UPDATE Permissions SET UserPermissions=:UPId WHERE PermissionId=:PId""")
    record2 = {"UPId": userpermission, "PId": permissionid}
    connect.execute(sql, **record2)


def getUserPermissions(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    userpermission = connect.execute(sql, **record1)
    return list(userpermission)


def setReadGroupPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT GroupPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    grouppermission = connect.execute(sql, **record1)
    if grouppermission is None:
        grouppermission = "R"
    else:
        grouppermission += "R"
    sql = text("""UPDATE Permissions SET GroupPermissions=:GPId WHERE PermissionId=:PId""")
    record2 = {"GPId": grouppermission, "PId": permissionid}
    connect.execute(sql, **record2)


def setWriteGroupPermission(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT GroupPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    grouppermission = connect.execute(sql, **record1)
    if grouppermission is None:
        grouppermission = "W"
    else:
        grouppermission += "W"
    sql = text("""UPDATE Permissions SET GroupPermissions=:GPId WHERE PermissionId=:PId""")
    record2 = {"GPId": grouppermission, "PId": permissionid}
    connect.execute(sql, **record2)


def getGroupPermissions(userid, docid):
    sql = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UId and DocId=:DId""")
    record = {"UId": userid, "DId": docid}
    permissionid = connect.execute(sql, **record)
    sql = text("""SELECT GroupPermissions from Permissions WHERE PermissionId=:PId""")
    record1 = {"PId": permissionid}
    grouppermission = connect.execute(sql, **record1)
    return list(grouppermission)
