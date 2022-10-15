# MVP for TechDocs
# It contains the Flask server setup (with dependencies in requirements.txt)
# The file structure has src directory with app.py file
# the src directory has templates directory which has index.html


from distutils.log import debug
from flask import Flask, jsonify, render_template
import socket

app= Flask(__name__)

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
	app.run(host='0.0.0.0',debug= True, port=5000)
