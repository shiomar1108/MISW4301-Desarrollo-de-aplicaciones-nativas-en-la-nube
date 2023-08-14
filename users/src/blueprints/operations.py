from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateUser
from models import UserSchema

# Definicion de esquemas
userSchema = UserSchema()

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods = ['POST'])
def create():
    data = request.get_json()
    result = CreateUser(data).execute()
    dateFormatted = str(result.createdAt).split('.')[0].replace(' ', 'T')
    return jsonify({ 'id': result.id, 'createdAt': dateFormatted })


