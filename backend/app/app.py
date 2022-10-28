# MVP for TechDocs
# It contains the Flask server setup (with dependencies in requirements.txt)
# The file structure has src directory with app.py file
# the src directory has templates directory which has index.html


from distutils.log import debug
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify, render_template
import socket
import yaml
import sys
from flask_cors import CORS
sys.path.append('../')
from services.FileManager.FileManager import fileManagerBlueprint
from services.SampleBlueprint.sampleBlueprint import sampleBlueprint
#from services.FileManager_2.FileManager_2 import fileManager_2
from services.UserAuthentication.Login import userLogin_bp
from services.UserAuthentication.Logout import userLogout_bp
from services.UserProfileManagement.getprofile import getUserProfile_bp
from services.UserProfileManagement.updateprofile import updateUserProfile_bp
from services.ForgotPassword.forgotpassword import forgotpassword_bp
from services.ForgotPassword.mail import mail_bp

with open('../config.yaml') as stream:
    configs = yaml.safe_load(stream)

from services.DocumentVersionManager.DocumentVersionManager import documentVersionManagerBlueprint
from services.UserHistoryManager.UserHistoryManager import userHistoryManagerBlueprint

app= Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

app.register_blueprint(documentVersionManagerBlueprint)
app.register_blueprint(userHistoryManagerBlueprint)
bcrypt = Bcrypt(app)
app.register_blueprint(fileManagerBlueprint)
#app.register_blueprint(fileManager_2)
app.register_blueprint(sampleBlueprint)
app.register_blueprint(userLogin_bp)
app.register_blueprint(userLogout_bp)
app.register_blueprint(getUserProfile_bp)
app.register_blueprint(updateUserProfile_bp)
app.register_blueprint(forgotpassword_bp)
app.register_blueprint(mail_bp)

app.config['ENV'] = configs["FLASK_ENV"]
app.config['SAMPLE_TESTING'] = "test success"
app.config["SECRET"] = "secret"

# This function get the hostname and IP deatils of server, required for microservices
def fetchDetails():
	hostname = socket.gethostname()
	host_ip = socket.gethostbyname(hostname)
	return str(hostname) , str(host_ip)

# This is main / landing page API 
@app.route("/")
def hello_world():
	return "<p> home page</p>"

# This is for endpoint "Health" to healthcheck the container health in microservices
@app.route("/health")
def health():
	return jsonify(Status ="UP")

# Endpoint for dynamic page 
@app.route("/details")
def details():
	hostname, ip = fetchDetails()
	return render_template('index.html', HOSTNAME=hostname, IP=ip)



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True, port=5000)
