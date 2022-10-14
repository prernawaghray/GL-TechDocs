from app import app
import boto3
import botocore
import jwt
from functools import wraps
from flask import jsonify
from flask import request
import mysql.connector as db
import json
from botocore.exceptions import ClientError
# from flask_limiter import Limiter
# from flask_limiter import get_remote_address

username = app.config['SQL_USERNAME']
password = app.config["SQL_PASSWORD"]
host = app.config['SQL_HOST']
s3_bucket = app.config["S3_BUCKET"]
secret_key = app.config["SECRET_KEY"]
aws_access_key = app.config['AWS_ACCESS_KEY']
aws_access_secret_key = app.config['AWS_ACCESS_SECRET']
extensions = app.config["ALLOWED_EXTENSIONS"]
try:
    connection=db.connect(
        user = username,
        password = password,
        host = host,
        database = "techDocs"
    )
except:
    print('something went wrong')


try:
    
    s3 = boto3.client(
        "s3",
        aws_access_key_id = aws_access_key,
        aws_secret_access_key = aws_access_secret_key
    )
except:
    print('something went wrong')



def authentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify(message='token missing')
        try:
            data = jwt.decode(token, secret_key ,algorithms=["HS256"])
            query = ("SELECT user_email FROM user_authentication WHERE user_id=(%s)")
            user_id = data['user_id']
            cursor = connection.cursor()
            cursor.execute(query,(user_id,))
            current_user_email = cursor.fetchall()[0][0]
            if not current_user_email:
                return jsonify(message='invalid token')
        except:
            return jsonify(message='something went wrong')
        
        return f(user_id, *args, **kwargs)
    return decorated

    
@app.route('/')
def healthcheck():
    return jsonify(health ='good')
    
def allowed_files(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() \
            in extensions
            
@app.route('/upload', methods=['POST'])
@authentication
def upload(user_id):
    if request.method == 'POST':
        file = request.files['file']
        file_name = secure_filename((file.filename))
        s3_object = user_id+'/'+file_name
        resp = check_object(s3_bucket, user_id)
        if 'CommonPrefixes' not in resp:
            s3.put_object(Bucket=s3_bucket,Key=user_id)

        status = send_to_s3(file,s3_bucket,s3_object)
        
        #TODO: Update the database
        if status:
            pass
        else:
            #return jsonify(message='something went wrong')
            pass

def check_object(bucket,key):
    path = path.rstrip('/')
    resp = s3.list_objects(Bucket=bucket, Prefix=key, Delimiter='/', MaxKeys=1)
    return resp

def send_to_s3(file,bucket_name,s3_object,acl='public-read'):
    try:
        response = s3.upload_file(file,bucket_name,s3_object)
    except ClientError as e:
        print(e)
        return False
    return True