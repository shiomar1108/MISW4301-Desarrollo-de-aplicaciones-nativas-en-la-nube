# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from validators.validators import validateSchema
from models.models import db, TarjetaCredito
from sqlalchemy.exc import SQLAlchemyError
from utilities.utilities import formatDateTimeToUTC
import traceback


class CrearTarjetaCredito(BaseCommannd):
    def __init__(self):
        self.validateRequest()

   
    def validateRequest(self):
        pass

    
    def execute(self):
        try:
            pass
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        