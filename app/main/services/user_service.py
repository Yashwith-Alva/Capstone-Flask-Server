'''
This module interacts with the database.

Author: yashwith alva
Date: 6-11-2023
'''
from mysql.connector.errors import Error
from flask import jsonify
from app.main.models.user import User
from app.main.sqlErrorHandler import logSqlError
from app.utils.responseHandler import makeResponse

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
            return makeResponse.created("Created User successfully", user_id)
        
        except Error as err:
            logSqlError(err)
            desc = {"errno" : err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database Error", desc)
        
    # Update password using restaurant id
    def update_password(self, password, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM users WHERE rid = %s"
            cursor.execute(select_query, (restaurant_id,))
            row = cursor.fetchone()
            if not row:
                return makeResponse.data_not_found("No restaurant exist with that id")
            
            update_query = "UPDATE users SET usrpassword = %s WHERE rid = %s"
            values = (password, restaurant_id,)
            cursor.execute(update_query, values)
            self.db_connection.commit()
            cursor.close()
            updates = {"usrpassword" : password}
            return makeResponse.response_ok(updates)
            
        except Error as err:
            logSqlError(err)
            desc = {"errno" : err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database Error", desc)
              
    # Update user_id using restaurant_id
    def update_userId(self, user_id, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM users WHERE rid = %s"
            cursor.execute(select_query, (restaurant_id,))
            row = cursor.fetchone()
            if not row:
                return makeResponse.data_not_found("No restaurant exist with that id")
            
            update_query = "UPDATE users SET usrId = %s WHERE rid = %s"
            values = (user_id, restaurant_id,)
            cursor.execute(update_query, values)
            self.db_connection.commit()
            cursor.close()
            updates = {"usrId" : user_id}
            return makeResponse.response_ok(updates)
        
        except Error as err:
            logSqlError(err)
            desc = {"errno" : err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database Error", desc)

    def get_restaurant_id(self, user_id, password):
        try:
            cursor = self.db_connection.cursor()

            # Assuming you have a table named 'users' with columns 'usrId', 'usrpassword', and 'rid'
            select_query = "SELECT rid FROM users WHERE usrId = %s AND usrpassword = %s"
            cursor.execute(select_query, (user_id, password))
            result = cursor.fetchone()

            if result:
                restaurant_id = result[0]
                return makeResponse.success({"restaurant_id": restaurant_id})
            else:
                return makeResponse.not_found("User not found")

        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg": err.msg}
            return makeResponse.bad_request("Database Error", desc)

        finally:
            cursor.close()

