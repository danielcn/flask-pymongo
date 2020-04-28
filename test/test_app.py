import unittest

from app import app
from mongo import db 

class TestApi(unittest.TestCase):
    def test_app_home(self, mock_log_info):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(200, response.status_code)

