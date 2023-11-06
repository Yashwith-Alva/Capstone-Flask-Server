'''
This module interacts with the database.

Author: yashwith alva
Date: 6-11-2023
'''

import mysql.connector
from models.user import User

class UserService:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def create_user(self, user_id, password, restaurant_id):
        cursor = self.db_connection.cursor()
        insert_query = "INSERT INTO users" # Complete the Query
        data = (user_id, password)
        cursor.execute(insert_query, data)

