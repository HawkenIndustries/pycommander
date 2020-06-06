from ..helpers.commanderHTTPClient import CommanderHTTPClient

class Trends:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'trendSetting'}
    ## Read Functions



    def get_all_trends_settings(self):
        devices = self.client.get_objects(self.q)
        return devices
    
    def create_trend_settings(self, trend_object):
        """
            Create an trend for the project
            :param trend_object  trend Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#d4b79184-c18e-5923-1ac7-1827d74abfb7
        """
        trend = self.client.json_post('/objects/', params=trend_object)
        return trend
    
    def delete_trend(self, trend_id):
        """
            Deletes an trend in the project
            :param trend_id ID of trend object
        """
        trend = self.client.json_delete('/objects/{}'.format(trend_id))
        return trend
    
