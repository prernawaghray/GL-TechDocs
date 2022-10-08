# Import all libraries
import os
import mysql.connector
from mysql.connector import connect, errorcode

# Method to store definitions of all the necessary tables into an array
def defineTables():
    # Table - UserAuthentication
    tbl_array['UserAuthentication'] = (
        "Create Table if not exists `UserAuthentication` ("
        "   UserId          varchar(256) UNIQUE,"
        "   UserEmail       varchar(256) UNIQUE,"
        "   Password        varchar(256),"
        "   IsAdmin         boolean DEFAULT false,"
        "   PRIMARY KEY (UserId)"
        ")"
    )

    # Table - Occupation
    tbl_array['Occupation'] = (
        "Create Table if not exists `Occupation` ("
        "   OccupationId    int not null AUTO_INCREMENT,"
        "   OccupationName  varchar(256),"
        "   PRIMARY KEY (OccupationId)"
        ")"
    )

    # Table - FieldOfWork
    tbl_array['FieldOfWork'] = (
        "Create Table if not exists `FieldOfWork` ("
        "   FieldId    int not null AUTO_INCREMENT,"
        "   FieldWork  varchar(50),"
        "   PRIMARY KEY (FieldId)"
        ")"
    )

    # Table - PurposeOfUsage
    tbl_array['PurposeOfUsage'] = (
        "Create Table if not exists `PurposeOfUsage` ("
        "   PurposeId  int not null AUTO_INCREMENT,"
        "   Purpose    varchar(100),"
        "   PRIMARY KEY (PurposeId)"
        ")"
    )

    # Table - UserProfile
    tbl_array['UserProfile'] = (
        "Create Table if not exists `UserProfile` ("
        "   UserId          varchar(256),"
        "   FirstName       varchar(100),"
        "   LastName        varchar(256),"
        "   Address         varchar(256),"
        "   SignUpDate      datetime,"
        "   lastActive      datetime,"
        "   OccupationId    int,"
        "   FieldId         int,"
        "   PurposeId       int,"
        "   AlternateEmail  varchar(256)"
        "   PRIMARY KEY (UserId),"
        "   FOREIGN KEY (UserID) REFERENCES UserAuthentication(UserId),"
        "   FOREIGN KEY (FieldId) REFERENCES FieldOfWork(FieldId),"
        "   FOREIGN KEy (PurposeId) REFERENCES PurposeOfUsage(PurposeId)"
        ")"
    )

    # Table - LinkedAccount
    tbl_array['LinkedAccount'] = (
        "Create Table if not exists `LinkedAccount` ("
        "   UserId              varchar(256),"
        "   AccountType         varchar(256),"
        "   AccountName         varchar(256),"
        "   AccountPassword     varchar(256),"    
        "   PRIMARY KEY (UserId),"
        "   FOREIGN KEY (UserID) REFERENCES UserAuthentication(UserId)"
        ")"
    )

# Creates a connection to the Database
def createTables():
    # Get all details of the DB from the environment variables
    db_conn = "latexdb.czl9dubxqhpg.us-east-1.rds.amazonaws.com"
    db_port = "3306"
    db_database = os.environ.get('MYSQL_DB')
    db_user = "latexedb"
    db_pass = "latexdb@12345"

    try:
        cnx = mysql.connector.connect(
            host=db_conn,
            database=db_database,
            user=db_user,
            password=db_pass
        )
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        cursor = cnx.cursor()

    for tbl_name in tbl_array:
        tbl_def = tbl_array[tbl_name]
        try:
            print("Running table def: {}: ".format(tbl_name), end='')
            cursor.execute(tbl_def)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already exists.")
            else:
                print(err.msg)
        else:
            print("...Passed")

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    # Variable to store all table definitions
    tbl_array = {}
    # Table definitions
    defineTables()
    # Open connection and run table defitions
    createTables()