'''
This module interacts with the database.

Author: yashwith alva
Date: 6-11-2023
'''
from mysql.connector.errors import Error
from flask import jsonify
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
            return jsonify({
                "status" : "success",
                "message" : "Created User successfully",
                "data" : user_id
            }), 201
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "error",
                "message" : mssg
            }), 400
        
    # Update password using restaurant id
    def update_password(self, password, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM users WHERE rid = %s"
            cursor.execute(select_query, (restaurant_id,))
            row = cursor.fetchone()
            
            if not row:
                return jsonify({
                    "status" : "error",
                    "message" : "No restaurant exist with that id"
                }), 400
            
            update_query = "UPDATE users SET usrpassword = %s WHERE rid = %s"
            values = (password, restaurant_id,)
            cursor.execute(update_query, values)
            self.db_connection.commit()
            cursor.close()
            return jsonify({
                "status" : "success",
                "message" : "Successfully updated password",
                "data" : restaurant_id
            })
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "error",
                "message" : mssg
            })
              
              
    # Update user_id using restaurant_id
    def update_userId(self, user_id, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            update_query = "UPDATE users SET usrId = %s WHERE rid = %s"
            values = (user_id, restaurant_id,)
            cursor.execute(update_query, values)
            self.db_connection.commit()
            cursor.close()
            return jsonify({
                "status" : "success",
                "message" : "Successfully updated user id",
                "data" : restaurant_id
            })
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "error",
                "message" : mssg
            })

