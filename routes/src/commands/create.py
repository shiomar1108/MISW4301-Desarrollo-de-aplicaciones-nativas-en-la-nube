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
class CreateRoute(BaseCommannd):
    def __init__(self, route):
        self.validateRequest(route)

    # Función que valida si existe un usuario con el email
    def validateDates(self, plannedStartDate, plannedEndDate):
        formatting = "%d-%m-%Y %I:%M:%S %p"

        if datetime.strptime(plannedStartDate,formatting) > datetime.strptime(plannedEndDate,formatting):
            raise UserEmailExists  # pragma: no cover
        else:
            if datetime.strptime(plannedStartDate) == datetime.strptime(plannedEndDate):
                raise UserEmailExists  # pragma: no cover
        
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
            #self.validateDates(self.plannedStartDate, self.plannedEndDate)            
            salt = uuid.uuid4().hex
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
     