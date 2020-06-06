from ..helpers.commanderHTTPClient import CommanderHTTPClient

class Points:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'point'}
    ## Read Functions
    def get_points_by_query(self, query_string=""):
        '''
            :param: query_string 
            :type: string
        '''
        params = {'q': 'point' + ("" if not query_string else query_string)}
        objects = self.client.get_objects(params)
        return objects
    
    def get_points_by_ids(self, ids):
        """
            Get a list of point objects by passign in array of ids

            :param ids List of ids
            :type ids: List
        """
        points = self.client.json_post('/points', {"ids": ids})
        return points
    
    def get_points_for_device(self, device_id):
        """
            Returns a list of points associated with a device

            :param device_id UUID of devices
            :type :device_id string        
        """

        points = self.client.json_post('/points', {"deviceId": device_id, "type": "curVal"})
        return points
    
    def get_all_point_for_project(self):
        """
            Returns a list of points associated with the project
        """
        points = self.client.json_get('/points?ms=true&type=curVal&page=')
        return points
    
    def get_point_trend_data_by_id(self, point_id):
        """
            Returns trend data for current rolling hour

            :param point_id UUID of the point       
        """

        trends = self.client.json_post('/points/{}/trends'.format(point_id))
        return trends
    
    def set_point_value_by_id(self, point_id, cur_val):
        """
            Returns point object with newly set curval if any
            :param point_id UUID of the point
            :cur_val  Desired value of the point
        """
        point = self.client.json_post('/points/{}'.format(point_id), params={'curVal': cur_val})
        return point




        