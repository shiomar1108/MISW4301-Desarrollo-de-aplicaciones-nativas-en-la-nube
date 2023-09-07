import requests
import os


class RF003CreateRouteRollback:
    def __init__(self, header):
        self.flag = False
        self.header = header

    def clear_flag(self):
        self.flag = False

    def set_flag(self, routeId):
        self.flag = True
        self.routeId = routeId

    def execute(self):
        if self.flag:
            ROUTES_PATH = os.environ["ROUTES_PATH"]
            result = requests.delete(
                ROUTES_PATH + "/routes/" + self.routeId, headers=self.header
            )
