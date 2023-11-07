'''
This module interacts with the database.

Author: yashwith alva
Date: 6-11-2023
'''
from mysql.connector.errors import Error
from app.main.models.user import User
from app.main.sqlErrorHandler import logSqlError

class UserService:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    # Create a User
    def create_user(self, user_id, password, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            insert_query = "INSERT INTO users (usrId, usrpassword, rid) VALUES (%s, %s, %s)"
            data = (user_id, password, restaurant_id,)
            cursor.execute(insert_query, data)
            self.db_connection.commit()
            cursor.close()
            return 1
        except Error as err:
            logSqlError(err)
            return err.msg
        
    # Fetch all users
    def get_users(self):
        pass
                

