from ..helpers.commanderHTTPClient import CommanderHTTPClient

class Alarms:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'alarm'}
    ## Read Functions

    ## Read Functions

    def get_all_alarms(self):
        alarms = self.client.get_objects(self.q)
        return alarms
    
    def create_alarm(self, alarm_object):
        """
            Create an alarm for the project
            :param alarm_object  Alarm Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#743e6adf-3766-5a65-1bab-76132b49d2d4
        """
        alarm = self.client.json_post('/objects/', params=alarm_object)
        return alarm
    
    def update_alarm(self, alarm_id, alarm_object):
        """
            Update an alarm for the project
            alarm_id Id of alarm object
            :param alarm_object  Alarm Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#743e6adf-3766-5a65-1bab-76132b49d2d4
        """
        alarm = self.client.json_post('/objects/{}'.format(alarm_id), params=alarm_object)
        return alarm
    
    def delete_alarm(self, alarm_id):
        """
            Deletes an alarm in the project
        """
        alarm = self.client.json_delete('/objects/{}'.format(alarm_id))
        return alarm
    
    def get_alarms_by_time_frame(self, time_frame, date):
        """
            Returns a list of alarm objects for the given date and timeframe
            :param time_frame Any of ('min', 'hour', 'day')
            :param date  Date in the format of YYYY/DD/MM
        """
        
        params = {
            "q": "alarmInstance",
            "page": 0,
            "timeFrame": time_frame,
            "date": date
        }
        alarms = self.client.get_objects(params=params)
        return alarms

    
