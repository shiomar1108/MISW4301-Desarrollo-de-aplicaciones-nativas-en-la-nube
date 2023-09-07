import json
from flask import request, Blueprint, Response
from commands.create import CreateOffer
from validators.validators import validateToken


rf004_blueprint = Blueprint('rf004', __name__)

# Recurso que expone la funcionalidad healthcheck
@rf004_blueprint.route('/rf004/ping', methods=['GET'])
def health():
    return "pong"

# Recurso que expone la funcionalidad creacion de ofertas
@rf004_blueprint.route('/rf004/posts/<string:postId>/offers', methods=['POST'])
def create(postId):
    validateToken(request.headers)
    newOfferObj = CreateOffer(postId=postId, post_request_json=request.get_json(), headers=request.headers)
    newOffer_response = newOfferObj.execute()          
    if newOffer_response.status_code == 201:
        data = {"id": newOffer_response.json()["id"], "userId": newOffer_response.json()["userId"], "createdAt": newOffer_response.json()["createdAt"], "postId": postId}
        resp = Response(response=json.dumps({"data": data, "msg": "offer created successfully"}), status=201, mimetype='application/json')
    else:
        resp = Response(response=json.dumps({"data": {}, "msg": newOffer_response.reason}, status=newOffer_response.status_code), mimetype='application/json')    
    return resp