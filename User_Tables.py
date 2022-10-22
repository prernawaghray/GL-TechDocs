'''
    This file is for creating the user profile tables in the Database
    Created UserAuthentication, Occupation, FieldOfWork, PurposeOfUsage, LinkedAccount and UserProfile
    Tables in user_details schema.
'''

# Import all libraries
import os
import mysql.connector
import yaml
from mysql.connector import connect, errorcode

# Method to store definitions of all the necessary tables into an array
def define_tables():
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

    # Table - UserProfile
    tbl_array['UserProfile'] = (
        "Create Table if not exists `UserProfile` ("
        "   UserId          varchar(256),"
        "   FirstName       varchar(100),"
        "   LastName        varchar(256),"
        "   StreetAddress   varchar(256),"
        "   State           varchar(256)"
        "   Country         varchar(100)"
        "   Occupation      varchar(256),"
        "   PurposeOfUsage  varchar(256),"
        "   SignUpDate      datetime,"
        "   lastActive      datetime,"
        "   PRIMARY KEY (UserId),"
        "   FOREIGN KEY (UserID) REFERENCES UserAuthentication(UserId)"
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
def create_tables():
    # Get all details of the DB from the environment variables
    with open('database_config.yml') as stream:
        configs = yaml.safe_load(stream)

    db_conn = configs['MYSQL_CONNECTION']
    db_database = configs['MYSQL_DB']
    db_user = configs['MYSQL_USER']
    db_pass = configs['MYSQL_PASS']

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
    define_tables()
    # Open connection and run table defitions
    create_tables()