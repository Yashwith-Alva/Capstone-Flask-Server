'''
Used to interact with the nutrition table in the database.
All methods necessary:
    1. Create Nutrition element by id
    2. Update Nutrition element by id
    3. Get all nutrition items
    4. Update all nutrition items by id
'''

from mysql.connector.errors import Error
from app.main.models.nutrition import Nutrition, FoodType
from app.main.sqlErrorHandler import logSqlError
from app.utils.responseHandler import makeResponse

class NutritionService:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    # Create an nutrition using itemId.
    def create_nutrition(self, item_id, energy, protein, carbohydrate, fat, foodType):
        '''
        Check if the item exist in menu table.
        If it exist, then add the nutrition table.
        '''
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM menu_items WHERE itemId = %s"
            cursor.execute(select_query, (item_id,))
            row = cursor.fetchone()
            if not row:
                return makeResponse.bad_request("Server Error", "No such item exist")
            
            create_query = "INSERT INTO nutrition (energy, protein, carbohydrate, fat, foodType, itemId) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (energy, protein, carbohydrate, fat, foodType, item_id,)
            cursor.execute(create_query, data)
            nutrition_id = cursor.lastrowid
            self.db_connection.commit()
            cursor.close()
            return makeResponse.created("Created a new Nutrition", nutrition_id)    
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
    # Update the existing nutrition info based on item_id
    def update_nutrition_info(self, item_id, energy, protein, carbohydrate, fat, foodType):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM nutrition WHERE itemId = %s"
            cursor.execute(select_query, (item_id,))
            row = cursor.fetchone()
            print(f"row: {row}")
            if not row:
                return makeResponse.bad_request("Server Error", "No such item exist")
                
            update_query = "UPDATE nutrition SET energy = %s, protein = %s, carbohydrate = %s, fat = %s, foodType = %s WHERE itemId = %s"
            data = (energy, protein, carbohydrate, fat, foodType, item_id)
            cursor.execute(update_query, data)
            self.db_connection.commit()
            cursor.close()
            updates = {"itemId" : item_id}
            return makeResponse.response_ok(updates)
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
    # Get nutrition based on item_id
    def get_nutrition_by_id(self, item_id):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            select_query = "SELECT * FROM nutrition WHERE itemId = %s"
            cursor.execute(select_query, (item_id,))
            nutrition = cursor.fetchone()
            self.db_connection.commit()
            cursor.close()
            
            if nutrition:
                return makeResponse.response_ok(nutrition)
            else:
                return makeResponse.data_not_found(f"No data found for itemId {item_id}")
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
            
    # Get all nutrition items
    def get_all_nutrition(self):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            select_query = "SELECT * FROM nutrition"
            cursor.execute(select_query)
            results = cursor.fetchall()
            self.db_connection.commit()
            if not results:
                return makeResponse.data_not_found("No data found for nutrition")
            nutrition_items = []
            for row in results:
                nutrition_items.append(row)
            return makeResponse.response_ok(nutrition_items)
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)

