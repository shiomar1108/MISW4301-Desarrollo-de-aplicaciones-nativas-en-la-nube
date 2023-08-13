from flask import request, Blueprint
from commands.create import CreateUser
from models import UserSchema

# Definicion de esquemas
userSchema = UserSchema()

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods = ['POST'])
def create():
    data = request.get_json()
    result = CreateUser(data).execute()
    # return jsonify({ 'sum': str(result), 'version': os.environ["VERSION"] })
    return userSchema.dump(result), 201


