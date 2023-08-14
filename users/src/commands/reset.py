# Importación de dependencias
import traceback
from errors import ApiError
from .base_command import BaseCommannd
from models import db, User

# Clase que contiene la logica de creción de usuarios
class ResetUsers(BaseCommannd):
    # Función que realiza creación del usuario
    def execute(self):
        try:
            db.session.query(User).delete()
            db.session.commit()
        except Exception as e:
            traceback.print_exc()
            raise ApiError(e)