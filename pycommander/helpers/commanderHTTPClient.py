import requests
from urllib.parse import urlencode

class CommanderHTTPClient:
    def __init__(self, host, token):
        self.host = host
        self.token = token
    
    def __session(self):
        client = requests.Session()
        client.headers = {"Authorization": "Bearer " + self.token}
        return client
    
    def get_objects(self, params):
        session = self.__session()
        res = session.get(self.host + '/objects', params=urlencode(params))
        session.close()
        if res.status_code == 401:
            raise Exception("Invalid Token")
        if res.status_code == 200:
            return res.json()
    
    def json_get(self, url, params={}):
        session = self.__session()
        res = session.get(self.host + url, params=params)
        session.close()
        if res.status_code == 401:
            raise Exception("Invalid Token")
        if res.status_code == 200:
            return res.json()

    def json_post(self, url, params={}):
        session = self.__session()
        res = session.post(self.host + url, json=params)
        session.close()
        if res.status_code == 401:
            raise Exception("Invalid Token")
        if res.status_code == 200:
            return res.json()
    def json_delete(self, url):
        session = self.__session()
        res = session.delete(self.host + url)
        session.close()
        if res.status_code == 401:
            raise Exception("Invalid Token")
        if res.status_code == 200:
            return res.json()