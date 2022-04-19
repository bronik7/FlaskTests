from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            req = c.get("/")
            self.assertEqual(req.status_code, 200)
            self.assertEqual(json.loads(req.get_data()), {'message': "Hello World!"})
