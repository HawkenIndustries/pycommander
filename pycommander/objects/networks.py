from ..helpers.commanderHTTPClient import CommanderHTTPClient

class Networks:
    def __init__(self, host, token):
        self.client = CommanderHTTPClient(host, token)
        self.q = {'q': 'network'}
    ## Read Functions

    def get_all_networks(self):
        networks = self.client.get_objects(self.q)
        return networks
    def get_network_details(self, network_id):
        network = self.client.json_get('/object/' + network_id)
        return network
    

    ## Create Functions

    def create_network(self, network):
        if(network['tags'] is None):
            raise Exception("Network object is missing tags")
        if(network["tagTypes"] is None):
            raise Exception("Network object is missing tagTypes")
        if(network["tags"]["subnet"] is None):
            raise Exception("A Subnet is required")
        if(network["tags"]["network"] is None or network["tags"]["network"] == False):
            raise Exception("Network object should have a network marker tag")

        new_network = self.client.json_post("/objects/", params=network)
        return new_network
    
    def update_network(self, network_id, network_obj):
        updated_network = self.client.json_post('/objects/' + network_id, params=network_obj)
        return updated_network
    
    def delete_network(self, network_id):
        network = self.client.json_delete('/networks/' + network_id)
        print("Deleted Network " + network_id)
        return network