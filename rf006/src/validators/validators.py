# Importación de dependencias
from errors.errors import BadRequest, InvalidToken, MissingToken
from jsonschema import validate
import traceback
import jsonschema
import uuid
import requests
import os


registrarTarjetaSchema = {
    "type": "object",
    "card": {
        "type": "object",
        "properties": {
            "cardNumber": {"type": "string"},
            "cvv": {"type": "string"},
            "expirationDate":  {"type": "string"},
            "cardHolderName": {"type": "string"}
        },
        "required": ["cardNumber","cvv","expirationDate","cardHolderName"]  
    },
    "properties": {
        "transactionIdentifier": {"type": "string"}
    },       
    "required": ["transactionIdentifier"]
}


def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest
    

def validateToken(headers):
    USERS_PATH = os.environ["USERS_PATH"]
    # call user/me
    result =  requests.get(USERS_PATH+'/users/me', headers=headers)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()["id"]
        