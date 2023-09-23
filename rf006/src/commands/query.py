from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, TarjetaCredito
from sqlalchemy.exc import SQLAlchemyError
import traceback


class TarjetaCreditoOnProcess(BaseCommannd):
    def __init__(self, status):
        self.status = status
                    
    def execute(self):
        try:
            cards_on_process = TarjetaCredito.query.filter(TarjetaCredito.status == self.status)
            return cards_on_process
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        