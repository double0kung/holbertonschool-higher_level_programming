import unittest
import requests
import json

class TestFlaskAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'

    def test_home_route(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_data_route_empty(self):
        response = requests.get(f"{self.BASE_URL}/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_user(self):
        user_data = {
            "username": "john",
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        }
        response = requests.post(f"{self.BASE_URL}/add_user", json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "User added")
        self.assertEqual(response.json()["user"], user_data)

    def test_data_route_after_adding(self):
        response = requests.get(f"{self.BASE_URL}/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["john"])

    def test_get_user(self):
        response = requests.get(f"{self.BASE_URL}/users/john")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "john")

    def test_get_nonexistent_user(self):
        response = requests.get(f"{self.BASE_URL}/users/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "User not found"})

    def test_status_route(self):
        response = requests.get(f"{self.BASE_URL}/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_add_user_without_username(self):
        user_data = {
            "name": "Jane Doe",
            "age": 25,
            "city": "Los Angeles"
        }
        response = requests.post(f"{self.BASE_URL}/add_user", json=user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Username is required"})

    def test_add_duplicate_user(self):
        user_data = {
            "username": "john",
            "name": "John Smith",
            "age": 35,
            "city": "Chicago"
        }
        response = requests.post(f"{self.BASE_URL}/add_user", json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "User added")

if __name__ == '__main__':
    unittest.main()
