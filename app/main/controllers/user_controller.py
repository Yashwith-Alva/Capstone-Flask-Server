'''
This module provides a straight forward interface to perform several operations.
'''

from flask import jsonify
from app.main.services.user_service import UserService

# Class which provides interface to routes
class UserController:
    def __init__(self, db_connection):
        self.userService_ = UserService(db_connection)
    
    # Add a new user
    def create_user(self, request):
        data = request.get_json()
        user_id = data.get('usrId')
        password = data.get('usrpassword')
        restaurant_id = data.get('rid')
        
        if not restaurant_id:
            return jsonify({'status' : 'error', 'message' : 'restaurant Id is required'}), 400
        res = self.userService_.create_user(user_id, password, restaurant_id)
        return res
        
    
    # Fetch all users
    def get_all_users(self):
        pass