from flask import Flask
from flask import send_from_directory
from authlib.integrations.flask_client import OAuth

app = Flask(__name__,instance_relative_config=True,static_url_path='')

app.config['SECRET_KEY'] = 'secret_key'


'''OAuth Configuration'''
oauth = OAuth()
oauth.init_app(app)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''

oauth.register(
            name='google',
            client_id= GOOGLE_CLIENT_ID,
            client_secret = GOOGLE_CLIENT_SECRET,
            server_metadata_url=CONF_URL,
            client_kwargs={
                'scope': 'openid email profile'
            }
        )


@app.route('/site.webmanifest')
def manifest():
    return send_from_directory('static', 'site.webmanifest')


from app import views
