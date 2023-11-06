'''
Model represents the user table of arfoodmenu database

Author: yashwith alva
Date: 6-11-2023
'''
class User:
    def __init__(self, user_id, user_password, restaurant_id):
        self.user_id = user_id
        self.user_password = user_password
        self.restaurant_id = restaurant_id
    
    def __repr__(self) -> str:
        return f'''User
                user_id = '{self.user_id}' 
                password = '{self.user_password}'
                restaurant_id = '{self.restaurant_id}
            '''
    