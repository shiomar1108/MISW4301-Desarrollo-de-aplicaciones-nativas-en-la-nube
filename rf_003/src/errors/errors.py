# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"


class SequenceError(ApiError):
    code = 300
    description = "Alguno de los pasos fallo."
