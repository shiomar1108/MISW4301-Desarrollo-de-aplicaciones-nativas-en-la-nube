# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log."
    
# Clase que contiene la estructura de error por defecto
class UserNameExists(ApiError):
    code = 412
    description = "El username ya se encuentra registrado."

class UserEmailExists(ApiError):
    code = 412
    description = "El email ya se encuentra registrado."

# Clase que contiene la estructura de un error de tipo Bad Request
class BadRequest(ApiError):
    code = 400
    description = "Párametros de entrada invalidos."