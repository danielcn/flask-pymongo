import unittest

from app import app
from mongo import db 

class TestApi(unittest.TestCase):
    def test_app_home(self, mock_log_info):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(200, response.status_code)


    def test_add_user(self, mock_log_info):
        user_collection = mongo.db
        with app.test_client() as client:
            response = client.get("/")
            user_collection.insert({'name': 'Daniel', 'language': 'Python'})
            user_collection.insert({'name': 'Tiago', 'language': 'C'})
            self.assertEqual('<h1>User added</h1>', response.data)

    def test_find(self, mock_log_info):
        user_collection = mongo.db
        with app.test_client() as client:
            response = client.get("/find")
            user = user_collection.find_one({'name': 'Tiago'})
            self.assertEqual(f'<h1>User: { user["name"] } Language: { user["language"] } </h1>', response.data)
