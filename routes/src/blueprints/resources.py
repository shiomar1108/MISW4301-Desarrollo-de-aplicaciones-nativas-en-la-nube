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
from validators.validators import validateToken, validateExistTokenHeader
from errors.errors import ApiError,  fligthExists, ValidateDates, InvalidToken, MissingToken, validateFlightError

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
    try:
        header = request.headers
        validateExistTokenHeader(header)
        user = validateToken(header)
        data = request.get_json()
        result = CreateRoute(data).execute()
        return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201
    except fligthExists as e:  # pragma: no cover
        return '', 412
    except InvalidToken as e:  # pragma: no cover
        return '', 403
    except MissingToken as e:  # pragma: no cover
        return '', 401

@routes_blueprint.route('/routes', methods=['GET'])
def queryflightId():
    try:
        header = request.headers
        user = validateToken(header) 
        args = request.args
        flight =  args.get('flight')
        result = QueryRoute(flight).execute()
        return jsonify(result), 200
    except InvalidToken as e:  # pragma: no cover
        return '', 403
    except MissingToken as e:  # pragma: no cover
        return '', 401
    except validateFlightError as e:
        return '', 400


@routes_blueprint.route('/routes/<string:id>', methods=['GET'])
def getRouteId(id):
    try:
        header = request.headers
        user = validateToken(header)
        result = GetRoute(id).execute()
        return jsonify({'id': result.id,'flightId':result.flightId,'sourceAirportCode': result.sourceAirportCode, 'sourceCountry': result.sourceCountry, 'destinyAirportCode': result.destinyAirportCode, 'destinyCountry': result.destinyCountry, 'bagCost': result.bagCost, 'plannedStartDate': result.plannedStartDate,'plannedEndDate':result.plannedEndDate, 'createdAt':result.createdAt}), 200
    except InvalidToken as e:  # pragma: no cover
        return '', 403
    except MissingToken as e:  # pragma: no cover
        return '', 401
    except IdNotUUID as e:
        return '', 400
    except NotFound as e:
        return '', 404

@routes_blueprint.route('/routes/<string:id>', methods=['DELETE'])
def deleteRoute(id):
    try:
        header = request.headers
        user = validateToken(header)
        DeleteRoute(id).execute()
        return jsonify({'msg': 'El trayecto fue eliminado.'}), 200
    except InvalidToken as e:  # pragma: no cover
        return '', 403
    except MissingToken as e:  # pragma: no cover
        return '', 401
    except IdNotUUID as e:
        return '', 400
    except NotFound as e:
        return '', 404