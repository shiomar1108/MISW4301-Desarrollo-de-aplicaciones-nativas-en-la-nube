import requests
import os


class RF003CreateRouteRollback:
    def __init__(self):
        self.flag = False

    def clear_flag(self):
        self.flag = False

    def set_flag(self):
        self.flag = True

    def execute(self, header, routeId):
        if self.flag:
            ROUTES_PATH = os.environ["ROUTES_PATH"]
            result = requests.delete(
                ROUTES_PATH + "/routes/" + routeId, headers=header
            )
