from flask import Flask
from flask import send_from_directory
from authlib.integrations.flask_client import OAuth

app = Flask(__name__,instance_relative_config=True,static_url_path='')


app.config['SECRET_KEY'] = 'secret_key'
'''OAuth Configuration'''
oauth = OAuth()
oauth.init_app(app)
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
            name='google',
            client_id= "43033882869-6u8msl41v0oi764cajeer3e9bf60cj2j.apps.googleusercontent.com",
            client_secret = "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",
            server_metadata_url=CONF_URL,
            client_kwargs={
                'scope': 'openid email profile'
            }
        )


@app.route('/site.webmanifest')
def manifest():
    return send_from_directory('static', 'site.webmanifest')


from app import views
