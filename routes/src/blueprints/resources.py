from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateRoute
from commands.query import QueryRoute
from commands.reset import ResetRoutes
from commands.get import GetRoute
from commands.delete import DeleteRoute
from queries.detail import GetRouteDetail
from commands.update import UpdateRoute
from utilities.utilities import formatDateTimeToUTC
from validators.validators import validateToken

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
    header = request.headers
    user = validateToken(header)
    data = request.get_json()
    result = CreateRoute(data).execute()
    return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201


@routes_blueprint.route('/routes', methods=['GET'])
def queryflightId():
    header = request.headers
    user = validateToken(header) 
    args = request.args
    flight =  args.get('flight')
    result = QueryRoute(flight).execute()
    return jsonify(result), 200


@routes_blueprint.route('/routes/<string:id>', methods=['GET'])
def getRouteId(id):
    header = request.headers
    user = validateToken(header)
    result = GetRoute(id).execute()
    return jsonify({'id': result.id,'flightId':result.flightId,'sourceAirportCode': result.sourceAirportCode, 'sourceCountry': result.sourceCountry, 'destinyAirportCode': result.destinyAirportCode, 'destinyCountry': result.destinyCountry, 'bagCost': result.bagCost, 'plannedStartDate': result.plannedStartDate,'plannedEndDate':result.plannedEndDate, 'createdAt':result.createdAt}), 200
    #return jsonify(result), 200

@routes_blueprint.route('/routes/<string:id>', methods=['DELETE'])
def deleteRoute(id):
    header = request.headers
    user = validateToken(header)
    DeleteRoute(id).execute()
    return jsonify({'msg': 'El trayecto fue eliminado.'}), 200