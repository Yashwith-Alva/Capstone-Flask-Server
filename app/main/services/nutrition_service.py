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
        Check if the item exist
        Create a new nutrition with nutrition_id = item_id.
        Using item_id update the menu item to hold this item_id.
        '''
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM menu_items WHERE itemId = %s"
            cursor.execute(select_query, (item_id,))
            row = cursor.fetchone()
            if not row:
                return makeResponse.bad_request("Server Error", "No such item exist")
            
            result = self.construct_nutrition_info(item_id, energy, protein, carbohydrate, fat, foodType)
            if result == -1:
                return makeResponse.bad_request("Database error", "Something went wrong while creating new nutrition")
            
            result = self.update_menu_nutrition(item_id)
            if result == -1:
                return makeResponse.bad_request("Database error", "Something went wrong while attaching food with it's nutrtion")
            
            return makeResponse.created("Created a new Nutrition", item_id)    
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
    # Update the existing nutrition info
    def update_nutrition_info(self, item_id, energy, protein, carbohydrate, fat, foodType):
        pass
        
        
    # Create a new restaurant id
    def construct_nutrition_info(self, item_id, energy, protein, carbohydrate, fat, foodType):
        try:
            cursor = self.db_connection.cursor()
            create_query = "INSERT INTO nutrition (nutritionId, energy, protein, carbohydrate, fat, foodType) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (item_id, energy, protein, carbohydrate, fat, foodType)
            cursor.execute(create_query, data)
            self.db_connection.execute()
            return 1
        except Error as err:
            logSqlError(err)
            return -1
        
  
    # Update the menu_items.nutritionId with the item_id.
    def update_menu_nutrition(self, item_id):
        try:
            cursor = self.db_connection.cursor()
            update_query = ""
            data = (item_id, item_id,)
            cursor.execute(update_query, data)
            self.db_connection.execute()
            return 2
        except Error as err:
            logSqlError(err)
            return -1
            