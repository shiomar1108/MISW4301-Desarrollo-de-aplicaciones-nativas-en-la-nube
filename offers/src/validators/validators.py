# Importación de dependencias
from errors.errors import BadRequest, OfferFieldCreateError, IdNotUUID
from jsonschema import validate
import traceback
import jsonschema
import uuid

# Esquemas para la creación de una Oferta
createOfferSchema = {
    "type": "object",
    "properties": {
        "postId": {"type": "string"},
        "description": {"type": "string"},
        "size":  {"type": "string"},
        "fragile": {"type": "boolean"},
        "offer": {"type": "number"},
    },
    "required": ["postId","description","size","fragile","offer"]
}

OfferFieldsSchema = {
    "type": "object",
    "properties": {
        "postId": {"type": "string", "minimum": 4, "maximum": 64},
        "description": {"type": "string", "minimum": 4, "maximum": 140},
        "size":  {"type": "string", "enum": ["LARGE", "MEDIUM", "SMALL"]},
        "fragile": {"type": "boolean"},
        "offer": {"type": "number", "minimum": 0},
    },
    "required": ["postId","description","size","fragile","offer"]
}

# Función que valida el request para la creación de usuarios
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest
    
# Función que valida el request para la creación de usuarios
def validateFieldSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise OfferFieldCreateError
    
# Función que valida el id en formato UUID
def validateIDsUUID(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        traceback.print_exc()
        raise IdNotUUID