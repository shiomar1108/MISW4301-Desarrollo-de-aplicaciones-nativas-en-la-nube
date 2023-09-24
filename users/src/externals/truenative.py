# Importación de dependencias
from commands.base_command import BaseCommannd
#import traceback
#from errors.errors import  InvalidToken, MissingToken, NotFound, InvalidUserPost
#from models.models import User
from externals.models import TrueNative, UserNative
import uuid
import os
import requests
from requests.structures import CaseInsensitiveDict
#import re
import json
from flask import abort, render_template, current_app
import logging


# Función que retorna la información del trayecto
def verifyUserExternal(userid, user, headers):
    TRUENATIVE_PATH = os.environ["TRUENATIVE_PATH"]
    USERS_PATH = os.environ["USERS_PATH"]
    SECRET_TOKEN = os.environ["SECRET_TOKEN"]
    
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer {SECRET_TOKEN}"
    # create user Native
    userNative = UserNative(
        email = user.get('email'),
        dni = user.get('dni'),
        fullName = user.get('fullName'),
        phone = user.get('phoneNumber')
    )
    identificador = str(uuid.uuid4())
    request = TrueNative(
        transactionIdentifier = identificador,
        userIdentifier = str(userid),
        userWebhook = USERS_PATH + '/users/native/callback',
        user = userNative.__dict__
    )
    
    print("********************************")
    print(str(json.dumps(request.__dict__)))
    print(request.__dict__)
    # call true Native
    result =  requests.post(TRUENATIVE_PATH+'/native/verify', json = str(json.dumps(request.__dict__)), headers=headers)
    #post = json.loads(result.json())
    print(result)
    return result.json()
