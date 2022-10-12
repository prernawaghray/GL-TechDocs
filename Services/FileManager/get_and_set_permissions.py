from sqlalchemy.sql import text
import sqlalchemy

engine = sqlalchemy.create_engine("mysql://username:password@host:3306/userDB")
connect = engine.connect()


def get_user_id(user_email):
    '''
        This function takes user_name fields from the UserAuthentication table as its input arguments
        queries the userid for that user_email.
        This function returns the UserId.
    '''
    sql = text("""SELECT user_id FROM UserAuthentication WHERE UserEmail=:UEMAIL""")
    record = {"UEMAIL": user_email}
    user_id = connect.execute(sql, **record)
    return user_id


def get_doc_id(user_id, doc_name):
    '''
        This function takes user_id and doc_name fields from the Document table as its input arguments
        queries the DocId for that Documents table.
        This function returns the DocId.
    '''
    sql = text("""SELECT doc_id FROM Documents WHERE user_id=:UID and DocName=:DNAME""")
    record = {"UID": user_id, "DNAME": doc_name}
    doc_id = connect.execute(sql, **record)
    return doc_id


def set_permissions(share_email, user_id, doc_name):
    '''
        This function takes share_email,user_id and doc_name as its input arguments.Fetches the
        userId of the sharing person and the DocId which is to be shared using the get_user_id and
        get_doc_id methods.This function helps to set the permissions by giving doc_id and share_user_id
        as inputs for the set permission methods.
    '''
    share_user_id = get_user_id(share_email)
    doc_id = get_doc_id(user_id, doc_name)
    set_read_user_permission(share_user_id, doc_id)


def set_read_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and UserPermissions details. If UserPermissions is not set, then it'll
        set to "read". However, if it is already set then the "read" permission is added to the existing
        permission set. This function gives a user "read" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    user_permission = connect.execute(sql_query_2, **param_2)
    if user_permission is None:
        user_permission = "R"
    else:
        user_permission += "R"
    sql_query_3 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_3 = {"UPID": user_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def set_write_use_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and UserPermissions details. If UserPermissions is not set, then it'll
        set to "write". However, if it is already set then the "write" permission is added to the existing
        permission set. This function gives a user "write" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    user_permission = connect.execute(sql_query_2, **param_2)
    if user_permission is None:
        user_permission = "W"
    else:
        user_permission += "W"
    sql_query_3 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_3 = {"UPID": user_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def set_share_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and UserPermissions details. If UserPermissions is not set, then it'll
        set to "share". However, if it is already set then the "share" permission is added to the existing
        permission set. This function gives a user "share" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UID and DocId=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    user_permission = connect.execute(sql_query_2, **param_2)
    if user_permission is None:
        user_permission = "S"
    else:
        user_permission += "S"
    sql_query_3 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_3 = {"UPID": user_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def set_delete_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and UserPermissions details. If UserPermissions is not set, then it'll
        set to "delete". However, if it is already set then the "delete" permission is added to the existing
        permission set. This function gives a user "delete" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UID and DocId=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    user_permission = connect.execute(sql_query_2, **param_2)
    if user_permission is None:
        user_permission = "D"
    else:
        user_permission += "D"
    sql_query_3 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_3 = {"UPID": user_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def set_analytics_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and UserPermissions details. If UserPermissions is not set, then it'll
        set to "analytics". However, if it is already set then the "analytics" permission is added to the existing
        permission set. This function gives a user "analytics" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE UserId=:UID and DocId=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    user_permission = connect.execute(sql_query_2, **param_2)
    if user_permission is None:
        user_permission = "A"
    else:
        user_permission += "A"
    sql_query_3 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_3 = {"UPID": user_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def get_user_permissions(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and UserPermissions details.
        This function returns the UserPermissions set to the user.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT UserPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    user_permission = connect.execute(sql_query_2, **param_2)
    return list(user_permission)


def unset_read_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_user_permissions method helps to get the UserPermissions assigned for
        that particular user_id and doc_id.Removed the "read" permission from the UserPermissions.Then
        updated the UserPermissions.This function removes a user "read" permissions of a file.
    '''
    user_permissions = get_user_permissions(user_id, doc_id)
    user_permissions.remove('R')
    user_permissions = "".join(user_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_2 = {"UPID": user_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)


def unset_write_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_user_permissions method helps to get the UserPermissions assigned for
        that particular user_id and doc_id.Removed the "write" permission from the UserPermissions.Then
        updated the UserPermissions.This function removes a user "write" permissions of a file.
    '''
    user_permissions = get_user_permissions(user_id, doc_id)
    user_permissions.remove('W')
    user_permissions = "".join(user_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_2 = {"UPID": user_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)


def unset_share_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_user_permissions method helps to get the UserPermissions assigned for
        that particular user_id and doc_id.Removed the "share" permission from the UserPermissions.Then
        updated the UserPermissions.This function removes a user "share" permissions of a file.
    '''
    user_permissions = get_user_permissions(user_id, doc_id)
    user_permissions.remove('S')
    user_permissions = "".join(user_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_2 = {"UPID": user_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)


def unset_delete_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_user_permissions method helps to get the UserPermissions assigned for
        that particular user_id and doc_id.Removed the "delete" permission from the UserPermissions.Then
        updated the UserPermissions.This function removes a user "delete" permissions of a file.
    '''
    user_permissions = get_user_permissions(user_id, doc_id)
    user_permissions.remove('D')
    user_permissions = "".join(user_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_2 = {"UPID": user_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)


def unset_analytics_user_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_user_permissions method helps to get the UserPermissions assigned for
        that particular user_id and doc_id.Removed the "analytics" permission from the UserPermissions.Then
        updated the UserPermissions.This function removes a user "analytics" permissions of a file.
    '''
    user_permissions = get_user_permissions(user_id, doc_id)
    user_permissions.remove('A')
    user_permissions = "".join(user_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET UserPermissions=:UPID WHERE PermissionId=:PID""")
    param_2 = {"UPID": user_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)


def set_read_group_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and GroupPermissions details. If GroupPermissions is not set, then it'll
        set to "read". However, if it is already set then the "read" permission is added to the existing
        permission set. This function gives a group "read" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT GroupPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    group_permission = connect.execute(sql_query_2, **param_2)
    if group_permission is None:
        group_permission = "R"
    else:
        group_permission += "R"
    sql_query_3 = text("""UPDATE Permissions SET GroupPermissions=:GPID WHERE PermissionId=:PID""")
    param_3 = {"GPID": group_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def set_write_group_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and GroupPermissions details. If GroupPermissions is not set, then it'll
        set to "write". However, if it is already set then the "write" permission is added to the existing
        permission set. This function gives a group "write" permissions of a file.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT GroupPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    group_permission = connect.execute(sql_query_2, **param_2)
    if group_permission is None:
        group_permission = "W"
    else:
        group_permission += "W"
    sql_query_3 = text("""UPDATE Permissions SET GroupPermissions=:GPID WHERE PermissionId=:PID""")
    param_3 = {"GPID": group_permission, "PID": permission_id}
    connect.execute(sql_query_3, **param_3)


def get_group_permissions(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId and GroupPermissions details.
        This function returns the GroupPermissions set to the user.
    '''
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""SELECT GroupPermissions from Permissions WHERE PermissionId=:PID""")
    param_2 = {"PID": permission_id}
    group_permission = connect.execute(sql_query_2, **param_2)
    return list(group_permission)


def unset_read_group_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_group_permissions method helps to get the GroupPermissions assigned for
        that particular user_id and doc_id.Removed the "read" permission from the GroupPermissions.Then
        updated the GroupPermissions.This function removes a group "read" permissions of a file.
    '''
    group_permissions = get_group_permissions(user_id, doc_id)
    group_permissions.remove('R')
    group_permissions = "".join(group_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET GroupPermissions=:GPID WHERE PermissionId=:PID""")
    param_2 = {"GPID": group_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)


def unset_write_group_permission(user_id, doc_id):
    '''
        This function takes user_id and doc_id fields from the Permissions table as its input arguments
        and queries the PermissionId.get_group_permissions method helps to get the GroupPermissions assigned for
        that particular user_id and doc_id.Removed the "write" permission from the GroupPermissions.Then
        updated the GroupPermissions.This function removes a group "write" permissions of a file.
    '''
    group_permissions = get_group_permissions(user_id, doc_id)
    group_permissions.remove('W')
    group_permissions = "".join(group_permissions)
    sql_query_1 = text("""SELECT PermissionId FROM Permissions WHERE user_id=:UID and doc_id=:DID""")
    param_1 = {"UID": user_id, "DID": doc_id}
    permission_id = connect.execute(sql_query_1, **param_1)
    sql_query_2 = text("""UPDATE Permissions SET GroupPermissions=:GPID WHERE PermissionId=:PID""")
    param_2 = {"GPID": group_permissions, "PID": permission_id}
    connect.execute(sql_query_2, **param_2)
