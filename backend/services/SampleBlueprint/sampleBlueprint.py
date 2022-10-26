from flask import Blueprint
from flask import current_app
from flask import jsonify


sampleBlueprint = Blueprint('sampleBlueprint', __name__)

@sampleBlueprint.route('/sample_blueprint')
def sample_bluerprint():
    return jsonify({'message':'Hello from sample blueprint'})

@sampleBlueprint.route('/config')
def config():
    value = current_app.config["SAMPLE_TESTING"]
    return jsonify({'result':value})
