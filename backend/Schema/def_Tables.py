#----------------------------------------------------------------------------------
# Usage:
# This script is used to configure tables on the dataabase
# Ref_Task: 1.3.3
#----------------------------------------------------------------------------------
# Pre requisites:
# Database connection string, database name, userid & password are to be configured 
#   as system environment variables 
# These values are fetched from the environment variables
#----------------------------------------------------------------------------------
# Revision history:
## Author        Date       Comment
## Shravan       20221005   Initial version
#----------------------------------------------------------------------------------

#ToDo: Defining FK constraints later after the code for Users schema is uploaded 

# Import all libraries
import os
import yaml
import os.path
import logging
import mysql.connector
from mysql.connector import connect, errorcode

##
# Method to store definitions of all the necessary tables into an array
# This array will later be looped and executed to create tables 
def defineTables():
    # Table - Documents
    # Stores all Document info - the latest version only
    tbl_array['Documents'] = (
    "Create Table if not exists `Documents` ("
    "   DocId           int not null AUTO_INCREMENT,"
    "   DocName         varchar(256),"
    "   UserId          varchar(256),"
    "   IsUpload        boolean,"
    "   FilePath        text,"
    "   CreatedDate     datetime,"
    "   ModifiedDate    datetime,"
    "   ModifiedBy      varchar(256),"
    "   Version         int,"
    "   s_Misc1         varchar(1024),"
    "   s_Misc2         varchar(1024),"
    "   n_Misc1         int,"
    "   n_Misc2         int,"
    "   PRIMARY KEY (DocId),"
    "   UNIQUE (DocId, UserId),"
    "   INDEX idx_Doc_ByUserDoc      (UserId, DocId),"
    "   INDEX idx_Doc_ByUserCreated  (UserId, CreatedDate),"
    "   INDEX idx_Doc_ByUserModified (UserId, ModifiedDate)"
    ")"
    )
    
    # Table - Permissions
    # Store permission of all documents for all users
    # Col Permission, possible values are (R)ead, (W)rite, (S)hare
    tbl_array['Permissions'] = (
    "Create Table if not exists `Permissions` ("
    "   PermissionId        int not null AUTO_INCREMENT,"
    "   DocId               int,"
    "   UserId              varchar(256),"
    "   UserPermissions     varchar(25),"
    "   GroupPermissions    varchar(25),"
    "   OtherPermissions    varchar(25),"
    "   Version             int,"
    "   s_Misc1             varchar(1024),"
    "   s_Misc2             varchar(1024),"
    "   n_Misc1             int,"
    "   n_Misc2             int,"
    "   PRIMARY KEY (PermissionId),"
    "   INDEX idx_Perm_ByUserDoc (UserId, DocId)"
    ")"
    )
    
    # Table - PaymentAccounts
    # Stores the payment methods of all users
    # Col - AccType, possible values are 'creditcard', 'debitcard', 'personal'
    tbl_array['PaymentAccounts'] = (
    "Create Table if not exists `PaymentAccounts` ("
    "   RecordId        int not null AUTO_INCREMENT,"
    "   UserId          varchar(256),"   
    "   IsDefault       bool,"
    "   AccType         varchar(50),"
    "   AccName         varchar(256),"
    "   AccNumber       int(20),"
    "   AccCvv          int(4),"
    "   AccExpiry       date,"
    "   AccIFSC         varchar(128),"
    "   Version         int,"
    "   s_Misc1         varchar(1024),"
    "   s_Misc2         varchar(1024),"
    "   n_Misc1         int,"
    "   n_Misc2         int,"
    "   PRIMARY KEY (RecordId),"
    "   INDEX idx_PA_User (UserId)"
    ")"
    )
    
    # Table - UserPayments
    # Stores the history of all payments of all users
    # Col - PaymentMethod, possible values are 'card', 'netbank', 'UPI'
    # Col - Status, possible values are 'success', 'failed'
    tbl_array['UserPayments'] = (
    "Create Table if not exists `UserPayments` ("
    "   RecordId        int not null AUTO_INCREMENT,"
    "   UserId          varchar(256),"
    "   PaidDate        datetime,"
    "   Amount          decimal(65,30),"
    "   PayAccountId    int,"
    "   PaymentMethod   varchar(128),"
    "   Status          varchar(50),"
    "   Notes           text,"
    "   Version         int,"
    "   s_Misc1         varchar(1024),"
    "   s_Misc2         varchar(1024),"
    "   n_Misc1         int,"
    "   n_Misc2         int,"
    "   PRIMARY KEY (RecordId),"
    "   INDEX idx_UP_UserDate (UserId, PaidDate)"
    ")"
    )
    
    # Table - UserSubscriptions
    # Stores the User subscriptions info
    # Col - Type, possible values are (F)ree, (PC) Paid Corporate
    # Col - TypeDesc, possible values are 'Personal', 'Corporate'
    # Col - Status, possible values are (A)ctive', (I)nactive
    tbl_array['UserSubscriptions'] = (
    "Create Table if not exists `UserSubscriptions` ("
    "   RecordId        int not null AUTO_INCREMENT,"
    "   UserId          varchar(256),"
    "   Type            char(5),"
    "   TypeDesc        varchar(128),"
    "   Status          Char(1),"
    "   ExpiryDate      datetime,"
    "   Version         int,"
    "   s_Misc1         varchar(1024),"
    "   s_Misc2         varchar(1024),"
    "   n_Misc1         int,"
    "   n_Misc2         int,"
    "   PRIMARY KEY (RecordId),"
    "   INDEX idx_US_User (UserId)"
    ")"
    )

    tbl_array['User'] = (
    "Create Table if not exists `User` ("
    "   Id             varchar(256) not null,"
    "   username       varchar(256),"
    "   password       varchar(256),"
    "   isadmin        boolean,"
    "   loginType      varchar(256),"
    "   PRIMARY KEY (id),           "
    "   INDEX idx_User (id)"
    ")"
    )

    tbl_array ['UsersProfile'] = (
    "Create Table if not exists `UsersProfile` ("
    "   username          varchar(256),"
    "   firstName       varchar(100),"
    "   lastName        varchar(100),"
    "   streetAddress   varchar(256),"
    "   state           varchar(256),"
    "   country         varchar(256),"
    "   occupation      varchar(256),"
    "   purposeOfUsage  varchar(256),"
    "   signUpDate      datetime,"
    "   lastActiveDate  datetime,"
    "   PRIMARY KEY (username),"
    "   FOREIGN KEY (username) REFERENCES User(username),"
    "   INDEX idx_UserProfile (username)"
    ")"

    )
##
# Method to run the table definitions defined in the earlier call in a loop
# Creates a connection to the Database and then executes the create query
def createTables():
    
    # Get all details of the DB from the environment variables
    #db_conn     = os.environ.get('MYSQL_CONNECTION')
    #db_database = os.environ.get('MYSQL_DB')
    #db_user     = os.environ.get('MYSQL_USER')
    #db_pass     = os.environ.get('MYSQL_PASS')
    
    # Get details from configuration file
    with open(os.path.dirname(__file__)+'../config.yaml') as stream:
        configs = yaml.safe_load(stream)
    
    db_conn     = configs['DB_CONN']
    db_database = configs['DB_NAME']
    db_user     = configs['DB_USER']
    db_pass     = configs['DB_PASS']
    log_path    = configs['DIR_ROOT'] + configs['DIR_LOG']
    # Initiate logging 
    logging.basicConfig(filename=log_path)

    try:
        cnx = mysql.connector.connect(
            host=db_conn,
            database=db_database,
            user=db_user,
            password=db_pass
        )
    except mysql.connector.Error as err:
        logging.exception(err)
    else:
        cursor = cnx.cursor()
        
    for tbl_name in tbl_array:
        tbl_def = tbl_array[tbl_name]
        try:
            print("Running table def: {}: ".format(tbl_name), end='')
            logging.info("Running table def: {}: ".format(tbl_name), end='')
            #print("\n Table def: ",tbl_def)
            cursor.execute(tbl_def)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logging.error("Table already exists.")
            else:
                logging.exception(err.msg)
        else:
            print("...Passed")
            logging.info("...Passed")
 
    cursor.close()
    cnx.close()

#########################
# Main Call
#########################
if __name__ == '__main__':
    # Variable to store all table definitions
    tbl_array = {}
    # Table definitions
    defineTables()
    # Open connection and run table defitions
    createTables()



