from .commanderHTTPClient import CommanderHTTPClient
from .tagObject import TagObject

class Cursor():
    def __init__(self, host, token, params, method="GET"):
        self.nextPage = True
        self.page = ""
        self.params = params
        self.method = method
        self.client = CommanderHTTPClient(host, token)
    def results(self):
        """
        :returns List of Tag Object Classes
        :rtype List[TagObject]
        """
        self.params['page'] = self.page
        response = self.client.json_get('/objects', self.params)
        results = []
        self.nextPage = True if response['nextPage'] else False
        self.page = "" if response['nextPage'] is None else response['nextPage']
        for to in response['results']:
            results.append(TagObject(to))
        return results
    def next(self):
        """
        :returns List of Tag Object Classes
        :rtype List[TagObject]
        """
        self.params['page'] = self.page
        response = self.client.json_get('/objects', self.params)
        results = []
        self.nextPage = True if response['nextPage'] else False
        self.page = "" if response['nextPage'] is None else response['nextPage']
        for to in response['results']:
            results.append(TagObject(to))
        return results
