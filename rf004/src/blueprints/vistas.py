from flask_restful import Resource
from flask import request, Response
from commands import create
import json

# from validators.validators import validateToken

class VistaOffer(Resource):

    def post(self, postId):
        # validateToken(request.headers)
        newOfferObj = create.CreateOffer(postId=postId, post_request_json=request.get_json(), headers=request.headers)
        newOffer_response = newOfferObj.execute()          
        if newOffer_response.status_code == 201:
            data = {"id": newOffer_response.json()["id"], "userId": newOffer_response.json()["userId"], "createdAt": newOffer_response.json()["createdAt"], "postId": postId}
            resp = Response(response=json.dumps({"data": data, "msg": "offer created successfully"}), status=201, mimetype='application/json')
        else:
            resp = Response(response=json.dumps({"data": {}, "msg": newOffer_response.reason}, status=newOffer_response.status_code), mimetype='application/json')    
        return resp



