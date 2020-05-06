from ..helpers.commanderHTTPClient import CommanderHTTPClient

class Schedules:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'schedule'}
    ## Read Functions
    ## Read Functions

    def get_all_schedules(self):
        devices = self.client.get_objects(self.q)
        return devices
    
    def create_schedule(self, schedule_object):
        """
            Create an schedule for the project
            :param schedule_object  schedule Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#7549d641-dee7-aa4e-34d5-f58188f72ba1
        """
        schedule = self.client.json_post('/objects/', params=schedule_object)
        return schedule
    
    def update_schedule(self, schedule_id, schedule_object):
        """
            Update an schedule for the project
            schedule_id Id of schedule object
            :param schedule_object  schedule Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#743e6adf-3766-5a65-1bab-76132b49d2d4
        """
        schedule = self.client.json_post('/objects/{}'.format(schedule_id), params=schedule_object)
        return schedule
    
    def delete_schedule(self, schedule_id):
        """
            Deletes an schedule in the project
        """
        schedule = self.client.json_delete('/objects/{}'.format(schedule_id))
        return schedule
    
