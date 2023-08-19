# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError,  UserEmailExists
from validators.validators import validateSchema, createRouteSchema
from models.models import db, Route
from sqlalchemy.exc import SQLAlchemyError
import uuid
import hashlib
import traceback
from datetime import datetime



# Clase que contiene la logica de creción de rutas
class QueryRoute(BaseCommannd):
    def __init__(self,flightId):
        self.validateRequest(flightId)


    # Función que valida el request del servicio
    def validateRequest(self,flightId):
        # Validacion del request
        if flightId is None:
            raise UserEmailExists  # pragma: no cover
        
        


    # Función que realiza creación del usuario
    def execute(self,flightId):
        try:
            routeToConsult = Route.query.filter(Route.flightId == flightId).first()    
            print(routeToConsult)
            newRoute = Route(
                flightId=routeToConsult.flightId,
                sourceAirportCode=routeToConsult.sourceAirportCode,
                sourceCountry=routeToConsult.sourceCountry,
                destinyAirportCode=routeToConsult.destinyAirportCode,
                destinyCountry=routeToConsult.destinyCountry,
                bagCost=routeToConsult.bagCost,
                plannedStartDate=routeToConsult.plannedStartDate,
                plannedEndDate=routeToConsult.plannedEndDate,
                createdAt=routeToConsult.createdAt                
            )
            
            return newRoute
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
     