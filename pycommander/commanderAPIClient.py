"""
This library allows you to quickly initialize a the Commander Python API
"""

from .objects import Devices, Alarms, Schedules, Points, Projects, Trends, Networks

class CommanderAPIClient:
    def __init__(self, token, host="https://app.kmccommander.com/api"):
        """
            Initiate a API Class with a token.
            Optional Param of host, if working on non kmc or beta server
        """
        self.token = token
        self.host = host
        self.points = Points(self.host, self.token)
        self.devices = Devices(self.host, self.token)
        self.schedules = Schedules(self.host, self.token)
        self.alarms = Alarms(self.host, self.token)
        self.projects = Projects(self.host, self.token)
        self.networks = Networks(self.host, self.token)
        self.trends = Trends(self.host, self.token)


        