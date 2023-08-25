import traceback
from errors.errors import FligthExists
from commands.query import QueryRoute
from flask import abort, render_template, current_app

#Funcion para vlaidar si existe un fligthID
def validateExistFligthId(flightId):
    current_app.logger.info('Inicia validacion de validateExistFligthId')
    result = QueryRoute(flightId).execute()
    current_app.logger.info('despues de resultado')
    current_app.logger.info(result)
    if result is None:
        current_app.logger.info('No tiene resultados se genera error')
        #raise FligthExists
    else:
        current_app.logger.info('Si tiene resultados')
        return True