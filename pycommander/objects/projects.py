from ..helpers.commanderHTTPClient import CommanderHTTPClient

class Projects:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'project'}
    ## Read Functions
    
    def get_update_logs(self, timestamp):
        """
            Get a list of project update logs
            :param timestamp Unix (epoch) value of time ex: datetime.datetime(2012,4,1,0,0).timestamp()
        """
        params = {
            "page": None,
            "start": timestamp
        }
        logs = self.client.json_get('/project/logs', params=params)
        return logs