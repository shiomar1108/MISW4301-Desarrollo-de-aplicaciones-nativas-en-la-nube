from flask import Blueprint
from flask_restful import Api
from blueprints.vistas import VistaOffer


api_blueprint = Blueprint('vistas', __name__)
api = Api(api_blueprint)
api.add_resource(VistaOffer, '/rf004/posts/<string:postId>/offers')