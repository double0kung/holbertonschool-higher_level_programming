import unittest
import json
from task_04_flask import app, users

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 
        users.clear()  # Reset users before each test

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to the Flask API!")

    def test_data_route_empty(self):
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [])

    def test_add_user(self):
        user_data = {
            "username": "john",
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        }
        response = self.app.post('/add_user', json=user_data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], "User added")
        self.assertEqual(response_data["user"], user_data)

    def test_data_route_after_adding(self):
        self.test_add_user()  # Add a user first
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), ["john"])

    def test_get_user(self):
        self.test_add_user()  # Add a user first
        response = self.app.get('/users/john')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["username"], "john")

    def test_get_nonexistent_user(self):
        response = self.app.get('/users/doesnotexist')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data), {"error": "User not found"})

    def test_status_route(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "OK")

    def test_add_user_without_username(self):
        user_data = {
            "name": "Jane Doe",
            "age": 25,
            "city": "Los Angeles"
        }
        response = self.app.post('/add_user', json=user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"error": "Username is required"})

    def test_add_duplicate_user(self):
        self.test_add_user()  # Add a user first
        user_data = {
            "username": "john",
            "name": "John Smith",
            "age": 35,
            "city": "Chicago"
        }
        response = self.app.post('/add_user', json=user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"error": "Username already exists"})

if __name__ == '__main__':
    unittest.main()
