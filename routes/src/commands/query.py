# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, validateFlightError  
from validators.validators import validateSchema, createRouteSchema, validateFlight
from models.models import db, Route
from sqlalchemy.exc import SQLAlchemyError
import uuid
import hashlib
import traceback
import json
from datetime import datetime


def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2

# Clase que contiene la logica de Consulta de rutas
class QueryRoute(BaseCommannd):
    def __init__(self, flightId):        
        self.flightId = flightId

    # Función que realiza creación del usuario
    def execute(self):
        try:
            if self.flightId is None:
                validateFlight(flightId)
                routeList = Route.query.all()
            else:
                routeList = Route.query.filter(Route.flightId == self.flightId)
            print(routeList) 
            return  dict_helper(routeList)
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
     