# from blueprints.api import api_blueprint
from flask import Flask
from flask_cors import CORS
from errors.errors import ApiError
from flask import jsonify
import os
from flask_restful import Api
from blueprints.vistas import VistaOffer

APP_PORT =  int(os.getenv("APP_PORT", default=3000))

app = Flask(__name__)
app_context = app.app_context()
app_context.push()
# app.register_blueprint(api_blueprint)
cors = CORS(app)
api = Api(app)
api.add_resource(VistaOffer, '/rf004/posts/<string:postId>/offers')

# Manejador de errores
@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description,
    }
    return jsonify(response), err.code

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=APP_PORT)