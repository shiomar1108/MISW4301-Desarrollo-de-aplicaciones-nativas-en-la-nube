from flask import Blueprint, request
from flask.json import jsonify
from validators.validators import (
    validateToken,
    validateDates,
    validateSchema,
    validate_expiration_date,
)
from agregators.post import post_user_route_check, rf003_post_create
from agregators.routes import route_check
from errors.errors import RouteDateError, UserPostRouteError, ExpirationDateError
import traceback

rf003_blueprint = Blueprint("rf003", __name__)


@rf003_blueprint.route("/rf003/ping", methods=["GET"])
def health():
    return "pong"


@rf003_blueprint.route("/rf003/posts", methods=["POST"])
def createPost():
    try:
        head = request.headers
        data = request.get_json()
        user = validateToken(head)
        validateSchema(data)
        routeId = route_check(data, head)
        if not validate_expiration_date(data["expireAt"]):
            raise ExpirationDateError
        if not validateDates(data["plannedStartDate"], data["expireAt"]):
            raise RouteDateError
        if not post_user_route_check(routeId, user, head):
            raise UserPostRouteError
        result = rf003_post_create(routeId, data["expireAt"], head)
        return jsonify("test"), 200
    except RouteDateError as e:
        #rollback
        traceback.print_exc()
        raise RouteDateError(e)
    except UserPostRouteError as e:
        #rollback
        traceback.print_exc()
        raise UserPostRouteError(e)
