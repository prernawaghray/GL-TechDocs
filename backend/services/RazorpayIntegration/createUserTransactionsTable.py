# DB Connector library
import mysql.connector

mydb = mysql.connector.connect(
        host="44.197.242.29",
        user="latexdb",
        password="Latexdb123!",
        database="latexdb"
        )

    # Define a Cursor
mycursor = mydb.cursor()

# Drop the table
sql = "DROP TABLE IF EXISTS UserTransactions"
mycursor.execute(sql)

#Create the transactions table
sql=""" CREATE TABLE UserTransactions(
            PaymentId VARCHAR(255) NOT NULL,
            UserId VARCHAR(255) NOT NULL,
            Type VARCHAR(255) ,
            Amount DECIMAL (6,2) NOT NULL,
            Currency VARCHAR(10) ,
            Status VARCHAR(255) ,
            Method VARCHAR(255) ,
            CardType VARCHAR(255) ,
            CardNetwork VARCHAR(255) ,
            CardLast4 VARCHAR(255) ,
            CardIssuer VARCHAR(255) ,
            CardInternational VARCHAR(255) ,
            CardEmi VARCHAR(255) ,
            CardSubType VARCHAR(255) ,
            CardTokenIin VARCHAR(255) ,
            OrderId VARCHAR(255) ,
            Description VARCHAR(255) ,
            RefundStatus VARCHAR(255) ,
            AmountRefunded DECIMAL (6,2) NOT NULL,
            Email VARCHAR(255) ,
            Contact VARCHAR(255) ,
            ErrorCode VARCHAR(255) ,
            DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (PaymentId),
	    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE
            )"""
mycursor.execute(sql)
mycursor.execute("show tables")

#for tables in  mycursor:
    #print(tables)
#Close the connection
mydb.close()


