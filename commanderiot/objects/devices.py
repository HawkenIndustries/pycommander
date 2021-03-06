from ..helpers.commanderHTTPClient import CommanderHTTPClient
from ..helpers.cursor import Cursor

class Devices:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'device'}
        self.cursor = Cursor(host, token, {"q": "device"})

    def get_devices(self):
        """
        :returns Cursor of devices
        :rtype Cursor
        """
        return self.cursor
    def get_device_details(self, network_id, device_id):
        device = self.client.json_post('/networks/{}/devices/{}/details'.format(network_id, device_id))
        return device
    def get_device_objects(self, network_id, device_id):
        device = self.client.json_post('/networks/{}/devices/{}/objects'.format(network_id, device_id))
        return device

    def get_all_connections(self):
        connections = self.client.get_objects({"q": "connection"})
        return connections
    
    def get_devices_by_model_name(self, model_name):
        params = {"q": "device and modelName=="+ model_name}
        devices = self.client.get_objects(params=params)
        return devices
    
    
    def delete_device(self, device_id):
        device = self.client.json_delete('/devices/' + device_id)
        print("Deleted device " + device_id)
        return device