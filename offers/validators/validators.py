# Importación de dependencias
from errors.errors import BadRequest
from jsonschema import validate
import traceback
import jsonschema

# Esquema para la creación de una Oferta
createOfferSchema = {
    "type": "object",
    "properties": {
        "postId": {"type": "string", "minimum": 4, "maximum": 64},
        "userId": {"type": "string", "minimum": 4, "maximum": 64},
        "description": {"type": "string", "minimum": 4, "maximum": 140},
        "size":  {"type": "string", "enum": ["LARGE", "MEDIUM", "SMALL"]},
        "fragile": {"type": "boolean"},
        "offer": {"type": "float"},
    },
    "required": ["postId", "userId", "description","size","fragile","offer"]
}

# Función que valida el request para la creación de usuarios
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest