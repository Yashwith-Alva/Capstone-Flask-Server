"""
This module provides services that interact with restaurant table
=> Restaurant Id is auto generated, hence not part of the computation
"""
from flask import jsonify, make_response
from mysql.connector.errors import Error
from app.main.models.restaurant import Restaurant
from app.main.sqlErrorHandler import logSqlError

class RestaurantService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Create a new Restaurant
    def create_restaurant(self, restaurant_name, about, qr, address, location_link):
        try:
            cursor = self.db_connection.cursor()
            insert_query = "INSERT INTO restaurant (resName, about, qr, address, locationLink) VALUES (%s, %s, %s, %s, %s)"
            data = (restaurant_name, about, qr, address, location_link,)
            cursor.execute(insert_query, data)
            self.db_connection.commit()
            restaurant_id = cursor.lastrowid
            cursor.close()
            return jsonify({
                "status" : "success",
                "message" : "Created restaurant successfully",
                "data" : restaurant_id
            }), 201
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "error",
                "message": mssg,
            }), 400
        
    # Fetch all restaurants from the table
    #TODO : restaurants_list = [{'rid':row.rid, 'resName': row.resName, 'about': row.about, 'qr': row.qr, 'address':row.address, 'locationLink': row.locationLink} for row in restaurants]
    def get_all_restaurants(self):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            select_query = "SELECT * FROM restaurant"
            cursor.execute(select_query)
            restaurants = []
            for row in cursor.fetchall():
                restaurant = Restaurant(row['rid'], row['resName'], row['about'], row['qr'], row['address'], row['locationLink'])
                restaurants.append(restaurant)
            cursor.close()
            restaurants_list = [{'rid':row.rid, 'resName': row.resName, 'about': row.about, 'qr': row.qr, 'address':row.address, 'locationLink': row.locationLink} for row in restaurants]
            
            return jsonify({
                "status" : "success",
                "data" : restaurants_list
            }), 200

        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "error",
                "message" : mssg
            }), 400
            
    # Fetch restaurant by Id
    def get_restaurant_by_id(self, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM restaurant WHERE rid = %s"
            value = (restaurant_id,)
            cursor.execute(select_query, value)
            restaurant = cursor.fetchone()
            cursor.close()
            if restaurant:
                return jsonify({
                    "status" : "success", 
                    "data" : restaurant
                }), 200
            else:
                return jsonify({
                    "status" : "success",
                    "message" : "Data not found",
                    "data" : None
                }), 404
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "success",
                "message" : mssg
            }), 400
            
    # Fetch restaurant information by QR code
    def get_restaurant_by_qr(self, qr):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM restaurant WHERE qr = %s"
            value = (qr,)
            cursor.execute(select_query, value)
            restaurant = cursor.fetchone()
            cursor.close()
            if restaurant:
                return jsonify({
                    "status" : "success", 
                    "data" : restaurant
                }), 200
            else:
                return jsonify({
                    "status" : "success",
                    "message" : "Data not found",
                    "data" : None
                }), 404
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "success",
                "message" : mssg
            }), 400    
        
    # Delete restaurant
    def delete_restaurant(self, restaurant_id):
        try:
            cursor = self.db_connection.cursor()
            delete_query = "DELETE FROM restaurant WHERE rid = %s"
            value = (restaurant_id)
            cursor.execute(delete_query, value)
            cursor.commit()
            cursor.close()
            return jsonify({
                "status" : "success",
                "message" : "Deleted a restaurant",
                "data" : restaurant_id
            })
        except Error as err:
            logSqlError(err)
            mssg = {"errno" : err.errno, "errmsg" : err.msg}
            return jsonify({
                "status" : "success",
                "message" : mssg
            }), 400   
