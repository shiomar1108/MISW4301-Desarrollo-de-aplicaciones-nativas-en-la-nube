from flask import request, Blueprint
from flask.json import jsonify



tarjetaCredito_blueprint = Blueprint('tarjetaCredito', __name__)


@tarjetaCredito_blueprint.route('/native/cards', methods=['POST'])
def registar():
    pass

@tarjetaCredito_blueprint.route('/native/cards/<string:ruv>', methods=['GET'])
def verificar(ruv):
    pass

@tarjetaCredito_blueprint.route('native/cards/log', methods=['GET'])
def solicitudes():
    pass

@tarjetaCredito_blueprint.route('native/cards/log/<string:ruv>', methods=['GET'])
def estado(ruv):
    pass

@tarjetaCredito_blueprint.route('native/cards/log', methods=['DELETE'])
def reset():
    pass