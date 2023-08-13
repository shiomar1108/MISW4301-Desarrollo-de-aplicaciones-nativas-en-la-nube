# Importación de dependencias
import traceback
import jsonschema
from jsonschema import validate
from errors import BadRequest

# Esquemas
createUserSchema = {
    "type": "object",
    "properties": {
        "username": {"type": "string", "minimum": 4, "maximum": 64},
        "email": {"type": "string", "minimum": 6, "maximum": 64, "format": "email"},
        "phoneNumber": {"type": "string", "minimum": 7, "maximum": 12, "pattern": "^ *\d[\d ]*$"},
        "dni":  {"type": "string", "minimum": 3, "maximum": 20, "pattern": "^ *\d[\d ]*$"},
        "fullName": {"type": "string", "minimum": 3, "maximum": 100},
        "password": {"type": "string", "minimum": 4, "maximum": 64},
    },
    "required": ["username", "email", "password"]
}

# Función que valida el request para la creación de usuarios
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest