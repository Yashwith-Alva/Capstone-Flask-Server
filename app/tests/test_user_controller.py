import unittest
from unittest.mock import patch, MagicMock
from app import create_app

class Test_User_Controller(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app().test_client()
    
    def test_add_user(self):
        user_data = {
            "usrId": "test5",
            "usrpassword": "t_pwd_5",
            "rid": 9
        }
        
        response = self.app.post("/user/register", json=user_data)
        self.assertEqual(response.status_code, 201)
        
    def test_add_restaurant(self):
        restaurant_data = {
            "resName": "ABC",
            "about": "ABC restaurant",
            "qr": "ABC2023",
            "address": "Electronic City",
            "locationLink": "https://ABC.com"
        }
        
        response = self.app.post("/restaurant", json=restaurant_data)
        self.assertEqual(response.status_code, 201)
    
    def test_get_restaurant(self):
        response = self.app.get("/restaurant")
        self.assertEqual(response.status_code, 200)
        
    def test_get_menuItem(self):
        response = self.app.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)