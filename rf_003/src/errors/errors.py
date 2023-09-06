# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"


class SequenceError(ApiError):
    code = 418 
    description = "I'm a teapot - Alguno de los pasos fallo."
