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
            cursor.execute(select_query, data)
            self.db_connection.commit()
            nutrition_id = cursor.lastrowid()
            cursor.close()
            return makeResponse.created("Created a new Nutrition", nutrition_id)    
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
        
    # Update the existing nutrition info
    def update_nutrition_info(self, item_id, energy, protein, carbohydrate, fat, foodType):
        try:
            pass
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
        