# Importación de dependencias
from flask.json import jsonify
import os
import traceback
import requests
from errors.errors import ApiError

# funcion que valida si el route existe
def route_check(data, headers):
    try:
        ROUTES_PATH = os.environ["ROUTES_PATH"]
        result = requests.get(
            ROUTES_PATH + "/routes?flight=" + data["flightId"], headers=headers
        )
        if 0 == len(result.text):
            body = jsonify(
                {
                    "flightId": data["flightId"],
                    "sourceAirportCode": data["origin"]["airportCode"],
                    "sourceCountry": data["origin"]["country"],
                    "destinyAirportCode": data["destiny"]["airportCode"],
                    "destinyCountry": data["destiny"]["country"],
                    "bagCost": data["bagCost"],
                    "plannedStartDate": data["plannedStartDate"],
                    "plannedEndDate": data["plannedEndDate"],
                }
            )
            creation = requests.post(
                ROUTES_PATH + "/routes", json=body, headers=headers
            )
            if 201 != creation.status_code:
                raise ApiError
            return creation.json()["id"]
        elif 200 == result.status_code:
            return result.json()["id"]
        else:
            raise ApiError
    except ApiError as e:
        traceback.print_exc()
        raise ApiError(e)
