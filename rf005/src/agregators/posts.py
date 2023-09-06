# Importación de dependencias
import traceback
from errors.errors import  InvalidToken, MissingToken
from models.models import db, Post
import uuid
import os
import requests
import re
import json

# Función que valida los headers
def getPostById(id,headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    # call post/id
    result =  requests.get(POSTS_PATH+'/posts/'+id, headers=headers)
    post = json.loads(result)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()