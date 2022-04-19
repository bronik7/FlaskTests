from unittest import TestCase
from app import app
import json
class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            req = c.get("/")
            self.assertEqual(req.status_code,200)
            self.assertEqual(json.loads(req.get_data()), {'message': "Hello World!"})