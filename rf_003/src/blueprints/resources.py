from flask import Blueprint
from flask.json import jsonify

rf003_blueprint = Blueprint('rf003', __name__)


@rf003_blueprint.route('/rf003/posts/ping', methods=['GET'])
def health():
    return "pong"

@rf003_blueprint.route('/rf003/posts', methods=['POST'])
def createPost(id):
    return jsonify('test'), 200
