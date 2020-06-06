import requests

class CommanderToken:
    def __init__(self, email, password, license_id="", host="https://app.kmccommander.com/api"):
        self.email = email
        self.password = password
        self.license_id = license_id
        self.host = host
    
    def get_token(self):
        credentials = {
            "email": self.email,
            "password": self.password
        }
        res = requests.post(self.host + '/login', credentials)
        jwtResponse = requests.get(self.host + '/setlicense/' + self.license_id, cookies = res.cookies)
        jwt = jwtResponse.json()['results'][0]
        return jwt