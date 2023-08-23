# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError,  fligthExists, ValidateDates, InvalidToken
from validators.validators import validateSchema, createRouteSchema
from models.models import db, Route
from commands.query import QueryRoute
from sqlalchemy.exc import SQLAlchemyError
import uuid
import hashlib
import traceback
from datetime import datetime

# Clase que contiene la logica de creción de rutas
class CreateRoute(BaseCommannd):
    def __init__(self, route):
        self.validateRequest(route)

    # Función que valida si existe un usuario con el email
    def validateDates(self, plannedStartDate, plannedEndDate):
        formatting = "%Y-%m-%dT%H:%M:%S.%fZ"
        date1 = datetime.strptime(plannedStartDate, formatting)
        date2 = datetime.strptime(plannedEndDate,formatting)
        if date1 > date2:
            raise ValidateDates  # pragma: no cover
        else:
            if date1 == date2:
                raise ValidateDates  # pragma: no cover
    
    #Funcion para vlaidar si existe un fligthID
    def existFligthId(self):
        result = QueryRoute(self.flightId).execute()
        if result.count() > 0:
            raise fligthExists 

    # Función que valida el request del servicio
    def validateRequest(self, routeJson):
        # Validacion del request
        validateSchema(routeJson, createRouteSchema)
        # Asignacion de variables
        self.flightId = routeJson['flightId']        
        self.sourceAirportCode = routeJson['sourceAirportCode']
        self.sourceCountry = routeJson['sourceCountry']
        self.destinyAirportCode = routeJson['destinyAirportCode']
        self.destinyCountry = routeJson['destinyCountry']
        self.bagCost = routeJson['bagCost']
        self.plannedStartDate = routeJson['plannedStartDate']
        self.plannedEndDate = routeJson['plannedEndDate']
        
        

    # Función que realiza creación del usuario
    def execute(self):
        try:
            self.validateDates(self.plannedStartDate, self.plannedEndDate)
            #validate flighId
            self.existFligthId()    
            newRoute = Route(
                flightId=self.flightId,
                sourceAirportCode=self.sourceAirportCode,
                sourceCountry=self.sourceCountry,
                destinyAirportCode=self.destinyAirportCode,
                destinyCountry=self.destinyCountry,
                bagCost=self.bagCost,
                plannedStartDate=self.plannedStartDate,
                plannedEndDate=self.plannedEndDate,                
            )
            db.session.add(newRoute)
            db.session.commit()
            return newRoute
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        except fligthExists as e:# pragma: no cover
            traceback.print_exc()
            raise fligthExists(e)
        except InvalidToken as e:# pragma: no cover
            traceback.print_exc()
            raise InvalidToken(e)
     