"""
This module provides services that interact with restaurant table
=> Restaurant Id is auto generated, hence not part of the computation
"""
import mysql.connector
from app.main.models.restaurant import Restaurant

class RestaurantService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Create a new Restaurant
    def create_restaurant(self, restaurant_name, about, qr, address, location_link):
        cursor = self.db_connection.cursor()
        insert_query = "INSERT INTO restaurant (resName, about, qr, address, locationLink) VALUES (%s, %s, %s, %s, %s)"
        data = (restaurant_name, about, qr, address, location_link)
        cursor.execute(insert_query, data)
        self.db_connection.commit()
        restaurant_id = cursor.lastrowid
        cursor.close()
        return restaurant_id
    
    # Fetch all restaurants from the table
    def get_all_restaurants(self):
        cursor = self.db_connection.cursor(dictionary=True)
        select_query = "SELECT * FROM restaurant"
        cursor.execute(select_query)
        restaurants = []
        for row in cursor.fetchall():
            print(row)
            restaurant = Restaurant(row['rid'], row['resName'], row['about'], row['qr'], row['address'], row['locationLink'])
            restaurants.append(restaurant)
        cursor.close()
        return restaurants
        
    # Fetch restaurant by Id
    def get_restaurant_by_id(self, restaurant_id):
        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM restaurant WHERE rid = %s"
        value = (restaurant_id)
        cursor.execute(select_query, value)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Restaurant(row['rid'], row['resName'], row['about'], row['qr'], row['address'], row['locationLink'])
        else:
            return None
        
        
    # Delete restaurant
    def delete_restaurant(self, restaurant_id):
        cursor = self.db_connection.cursor()
        delete_query = "DELETE FROM restaurant WHERE rid = %s"
        value = (restaurant_id)
        cursor.execute(delete_query, value)
        cursor.commit()
        cursor.close()
        
