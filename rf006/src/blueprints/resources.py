from flask import request, Blueprint
from flask.json import jsonify



tarjetaCredito_blueprint = Blueprint('tarjetaCredito', __name__)


@tarjetaCredito_blueprint.route('/credit-cards', methods=['POST'])
def create():
    pass

@tarjetaCredito_blueprint.route('/credit-cards', methods=['GET'])
def get():
    pass

@tarjetaCredito_blueprint.route('/credit-cards/ping', methods=['GET'])
def health():
    return "pong"

@tarjetaCredito_blueprint.route('/credit-cards/reset', methods=['POST'])
def reset():
    pass

@tarjetaCredito_blueprint.route('/native/cards', methods=['POST'])
def registartarjeta():
    pass

@tarjetaCredito_blueprint.route('/native/cards/<string:ruv>', methods=['GET'])
def verificarSolicitud(ruv):
    pass

@tarjetaCredito_blueprint.route('native/cards/log', methods=['GET'])
def listaSolicitudes():
    pass

@tarjetaCredito_blueprint.route('native/cards/log/<string:ruv>', methods=['GET'])
def detalleSolicitud(ruv):
    pass

@tarjetaCredito_blueprint.route('native/cards/log', methods=['DELETE'])
def deleteSolicitudes():
    pass