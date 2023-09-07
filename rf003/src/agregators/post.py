# Importación de dependencias
from flask.json import jsonify
import os
import requests


# Funcion que verifica que el usuario no haya creado otra publicacion para la misma ruta
def post_user_route_check(routeId, userId, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    result = requests.get(
        POSTS_PATH + "/posts?route=" + routeId + "&owner=" + userId, headers=headers
    )
    if 200 == result.status_code:
        return False
    return True


# Funcion para creacion de Post con los valores dados
def rf003_post_create(routeid, expireDate, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    data = jsonify({"routeId": routeid, "expireAt": expireDate})
    result = requests.post(POSTS_PATH + "/posts", json=data, headers=headers)
    return result.json()
