from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateRoute
from commands.query import QueryRoute
from commands.reset import ResetRoutes
#from commands.authenticate import Authenticate
from queries.detail import GetRouteDetail
from commands.update import UpdateRoute
from utilities.utilities import formatDateTimeToUTC

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/routes/ping', methods=['GET'])
def health():
    return "pong"

@routes_blueprint.route('/routes/reset', methods=['POST'])
def reset():
    ResetRoutes().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})


@routes_blueprint.route('/routes', methods=['POST'])
def create():
    data = request.get_json()
    result = CreateRoute(data).execute()
    return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201


@routes_blueprint.route('/routes', methods=['GET'])
def queryflightId():    
    args = request.args
    flight =  args.get('flight')
    result = QueryRoute(flight).execute(flight)
    return jsonify(result), 200