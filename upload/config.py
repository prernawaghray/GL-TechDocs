import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
env = os.path.join(basedir,'.env.local')
if os.path.exists(env):
    load_dotenv(env)

class Config(object):
    DEBUG=False

class DevConfig(Config):
    FLASK_ENV='developement'
    DEBUG=True
    SQL_HOST='localhost'
    SQL_USERNAME=os.environ.get('SQL_USERNAME')
    SQL_PASSWORD=os.environ.get('SQL_PASSWORD')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY=os.environ.get('AWS_ACCESS_KEY')
    AWS_ACCESS_SECRET=os.environ.get('AWS_ACCESS_SECRET')
    ALLOWED_EXTENSIONS={'tex','docs','ppt'}
    S3_BUCKET="S3 Bucket name"
    S3_LOCATION = "http://{}.s3.amazonaws.com/".format(S3_BUCKET)

    
class ProdConfig(Config):
    FLASK_ENV='production'
    DEBUG=False