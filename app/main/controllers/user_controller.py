'''
This module provides a straight forward interface to perform several operations.
'''

from flask import jsonify
from app.main.services.user_service import UserService, makeResponse

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
            return makeResponse.bad_request("Server Error", "restaurant_id is required")
        response = self.userService_.create_user(user_id, password, restaurant_id)
        return response
        
    
    # Update user id
    def update_userId(self, request):
        data = request.get_json()
        user_id = data.get('usrId')
        restaurant_id = data.get('rid')
        
        if not restaurant_id:
            return makeResponse.bad_request("Server Error", "restaurant_id is required")
        response = self.userService_.update_userId(user_id, restaurant_id)
        return response
        
        
    # Update password
    def update_password(self, request):
        data = request.get_json()
        password = data.get('usrpassword')
        restaurant_id = data.get('rid')
        
        if not restaurant_id:
            return makeResponse.bad_request("Server Error", "restaurant_id is required")
        response = self.userService_.update_password(password, restaurant_id)
        return response
    
    # Return restaurant id
    def get_restaurant_id(self, user_id, password):
        if not user_id or not password:
            return makeResponse.bad_request("Server Error", "userId and password are required")

        # Assuming you have a method named get_restaurant_id in your service
        response = self.userService_.get_restaurant_id(user_id, password)
        return response

