import unittest
from os import getenv
from dotenv import load_dotenv
from commanderiot.helpers import Cursor, TagObject
load_dotenv()


class TestCursor(unittest.TestCase):
    #Check if the cursor is returning a List of Tag Object Class
    def test_return_type_of_tag_object(self):
        token = getenv('token')
        host = "https://app.kmccommander.com/api"
        cursor = Cursor(host, token, {'q': "device"})  # Initialize a cursor
        tags = cursor.results() # Return the results of the cursor
        print("Next Page ?  {cursor.nextPage}")
        for tagObject in tags:
            print(tagObject.id)
            self.assertIsInstance(tagObject, TagObject, msg="result is an Instance of Tag Object")
        while(cursor.nextPage): # This will keep running until there are no new results
            results = cursor.next() # Returns the next set of results and updated nextPage Property
            for tagObject in results:
                print(tagObject.id) # Hover over tagObject to see values available to you
                print(tagObject.tags)
                print(tagObject.tagTypes)
                # tagObject.update() Update Tag Object 
        