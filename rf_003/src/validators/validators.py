import traceback
from errors.errors import InvalidToken, MissingToken
import os
import requests
from datetime import datetime


# Función que valida los headers
def validateToken(headers):
    USERS_PATH = os.environ["USERS_PATH"]
    # call user/me
    result = requests.get(USERS_PATH + "/users/me", headers=headers)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()["id"]


def validateDates(dateFlight, dateExpirePost):
    formatting = "%Y-%m-%dT%H:%M:%S.%fZ"
    dateF = datetime.strptime(dateFlight, formatting)
    dateP = datetime.strptime(dateExpirePost, formatting)
    actualDate = datetime.now()
    if (dateF > actualDate) and (dateP > actualDate) and (dateF >= dateP):
        return True
    else:
        return False
