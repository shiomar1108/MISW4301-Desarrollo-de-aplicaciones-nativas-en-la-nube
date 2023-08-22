# Importación de dependencias
import traceback
import jsonschema
from jsonschema import validate
from errors.errors import BadRequest, IdNotUUID, InvalidToken, MissingToken
import uuid
import os
import requests


# Esquemas
# Esquema para la creación de usuarios
createRouteSchema = {
    "type": "object",
    "properties": {
        "flightId": {"type": "string", "minimum": 1, "maximum": 5},
        "sourceAirportCode": {"type": "string", "minimum": 3, "maximum": 3},
        "sourceCountry": {"type": "string", "minimum": 1, "maximum": 100},
        "destinyAirportCode":  {"type": "string", "minimum": 3, "maximum": 3},
        "destinyCountry": {"type": "string", "minimum": 1, "maximum": 100},
        "bagCost": {"type": "integer"},
        "plannedStartDate": {"type": "string","minimum": 1, "maximum": 100},
        "plannedEndDate": {"type": "string","minimum": 1, "maximum": 100 },
    },
    "required": ["flightId", "sourceAirportCode", "sourceCountry", "destinyAirportCode"
                ,"destinyCountry","bagCost","plannedStartDate","plannedEndDate"]
}



# Función que valida el request para la creación de usuarios
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest

# Función que valida el id en formato UUID
def validateIDsUUID(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        traceback.print_exc()
        raise IdNotUUID

# Función que valida los headers
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
        