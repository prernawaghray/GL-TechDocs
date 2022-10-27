# DB Connector library
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Smitha",
        database="techdocs"
        )

    # Define a Cursor
mycursor = mydb.cursor()

# Drop the table
sql = "DROP TABLE IF EXISTS transactions"
mycursor.execute(sql)

#Create the transactions table
sql=""" CREATE TABLE UserTransactions(
            payment_id VARCHAR(255) NOT NULL,
            user_id VARCHAR(255) NOT NULL,
            type VARCHAR(255) ,
            amount DECIMAL (6,2) NOT NULL,
            currency VARCHAR(10) ,
            status VARCHAR(255) ,
            method VARCHAR(255) ,
            card_type VARCHAR(255) ,
            card_network VARCHAR(255) ,
            card_last4 VARCHAR(255) ,
            card_issuer VARCHAR(255) ,
            card_international VARCHAR(255) ,
            card_emi VARCHAR(255) ,
            card_sub_type VARCHAR(255) ,
            card_token_iin VARCHAR(255) ,
            order_id VARCHAR(255) ,
            description VARCHAR(255) ,
            refund_status VARCHAR(255) ,
            amount_refunded DECIMAL (6,2) NOT NULL,
            email VARCHAR(255) ,
            contact VARCHAR(255) ,
            error_code VARCHAR(255) ,
            date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (payment_id)
            )"""
mycursor.execute(sql)
mycursor.execute("show tables")

for tables in  mycursor:
    print(tables)
#Close the connection
    mydb.close()


