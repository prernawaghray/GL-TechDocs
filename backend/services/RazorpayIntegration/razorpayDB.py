# DB Connector library
import mysql.connector

# Function to insert the record in transactions table
def insert_rec(**payment_details):
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="44.197.242.29",
        user="latexdb",
        password="Latexdb123!",
        database="latexdb"
    )

    # Define a Cursor
    mycursor = mydb.cursor()

    sql = """ INSERT INTO UserTransactions
               (payment_id,
                UserId,
                type,
                amount,
                currency,
                status,
                method,
                order_id,
                description,
                refund_status,
                amount_refunded,
                email,
                contact,
                error_code,
                date_created,
                card_type,
                card_network,
                card_last4,
                card_issuer,
                card_international,
                card_emi,
                card_sub_type,                
                card_token_iin
                ) 
               VALUES (%s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                        %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s,
                       %s
                       )"""
    values = (payment_details['id'],
              payment_details['userId'],
              payment_details['entity'],
              payment_details['amount'],
              payment_details['currency'],
              payment_details['status'],
              payment_details['method'],
              payment_details['order_id'],
              payment_details['description'],
              payment_details['refund_status'],
              payment_details['amount_refunded'],
              payment_details['email'],
              payment_details['contact'],
              payment_details['error_code'],
              payment_details['created_at'],
              payment_details['card_type '],
              payment_details['card_network'],
              payment_details['card_last4'],
              payment_details['card_issuer'],
              payment_details['card_international'],
              payment_details['card_emi'],
              payment_details['card_sub_type'],
              payment_details['card_token_iin']
              )

    try:
        mycursor.execute(sql, values)

    except Exception as error:
        mydb.rollback()
        mydb.close()
        return error
    else:
        mydb.commit()
        mydb.close()
        return 0









