from flask import request, Blueprint
from flask.json import jsonify
import traceback
from flask import abort, render_template, current_app


rf05_blueprint = Blueprint('rf005', __name__)


@rf05_blueprint.route('/rf005/posts/ping', methods=['GET'])
def health():
    return "pong"

@rf05_blueprint.route('/rf005/posts/<string:id>', methods=['GET'])
def getPostById(id):
#    try:
#        header = request.headers
#        user = validateToken(header)
#        result = GetRoute(id).execute()
#        return jsonify({'id': result.id,'flightId':result.flightId,'sourceAirportCode': result.sourceAirportCode, 'sourceCountry': result.sourceCountry, 'destinyAirportCode': result.destinyAirportCode, 'destinyCountry': result.destinyCountry, 'bagCost': result.bagCost, 'plannedStartDate': result.plannedStartDate,'plannedEndDate':result.plannedEndDate, 'createdAt':result.createdAt}), 200
    return jsonify('test'), 200
#    except InvalidToken as e:  # pragma: no cover
#        return '', 401
#    except MissingToken as e:  # pragma: no cover
#        return '', 403
#    except IdNotUUID as e:
#        return '', 400
#    except NotFound as e:
#        return '', 404