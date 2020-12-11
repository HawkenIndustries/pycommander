
class TagObject:
    def __init__(self, tagDict):
        self.tags = tagDict['tags']
        self.tagTypes = tagDict['tagTypes']
        self.id = self.tags['id']
    def update(self,options):
        """ Update TagObject based on options
        """