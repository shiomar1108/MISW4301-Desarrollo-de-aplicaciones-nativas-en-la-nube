from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateOffer
from commands.reset import ResetOffers
from commands.delete import DeleteOffer
from commands.get import GetOffer
from utilities.utilities import formatDateTimeToUTC

offers_blueprint = Blueprint('offers', __name__)

@offers_blueprint.route('/offers/ping', methods=['GET'])
def health():
    return "pong"

@offers_blueprint.route('/offers/reset', methods=['POST'])
def reset():
    ResetOffers().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})

@offers_blueprint.route('/offers', methods=['POST'])
def create():
    data = request.get_json()
    result = CreateOffer(data).execute()
    return jsonify({'id': result.id,'userId': result.userId, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201

@offers_blueprint.route('/offers/<string:id>', methods=['DELETE'])
def delete(id):
    DeleteOffer(id).execute()
    return jsonify({'msg': 'La oferta fue eliminada'}), 200

@offers_blueprint.route('/offers/<string:id>', methods=['GET'])
def get(id):
    result = GetOffer(id).execute()
    return jsonify({'id': result.id, 'postId': result.postId, 'description': result.description, 'size': result.size, 'fragile': result.fragile, 'offer': result.offer, 'createdAt': result.createdAt, 'userId': result.userId}), 200

