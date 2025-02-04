import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Brazilian Party Snacks', response.data)

    def test_snack_list(self):
        response = self.app.get('/snacks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_snack(self):
        response = self.app.post('/snacks', json={'name': 'Coxinha', 'price': 2.50})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Coxinha', response.data)

if __name__ == '__main__':
    unittest.main()