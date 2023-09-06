from flask import Blueprint, request
from flask.json import jsonify
from validators.validators import validateToken, validateDates
from agregators.post import post_user_route_check, rf003_post_create
from agregators.routes import route_check
from errors.errors import SequenceError
import traceback

rf003_blueprint = Blueprint("rf003", __name__)


@rf003_blueprint.route("/rf003/ping", methods=["GET"])
def health():
    return "pong"


@rf003_blueprint.route("/rf003/posts", methods=["POST"])
def createPost(id):
    try:
        head = request.headers
        data = request.args
        user = validateToken(head)
        routeId = route_check(data, head)
        if not validateDates(data["plannedStartDate"], data["expireAt"]):
            raise SequenceError
        if not post_user_route_check(routeId, user, head):
            # Reject Request
            raise SequenceError
        result = rf003_post_create(routeId, data["expireAt"], head)
        return jsonify("test"), 200
    except SequenceError as e:
        traceback.print_exc()
        raise SequenceError(e)
