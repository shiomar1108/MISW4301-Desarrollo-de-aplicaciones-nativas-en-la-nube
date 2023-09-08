from flask import request, Blueprint
from flask.json import jsonify
from agregators.posts import agregator
import traceback
from flask import abort, render_template, current_app


rf05_blueprint = Blueprint('rf005', __name__)


@rf05_blueprint.route('/rf005/posts/ping', methods=['GET'])
def health():
    return "pong"

@rf05_blueprint.route('/rf005/posts/<string:id>', methods=['GET'])
def getInfoPostById(id):
#    try:
    header = request.headers
#        user = validateToken(header)
    result = agregator(id, header)        
    return jsonify(result), 200
#    except InvalidToken as e:  # pragma: no cover
#        return '', 401
#    except MissingToken as e:  # pragma: no cover
#        return '', 403
#    except IdNotUUID as e:
#        return '', 400
#    except NotFound as e:
#        return '', 404