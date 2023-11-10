'''
This module interacts with the menu item database
-> Add Item
-> Remove Item
-> Update Item
-> 
'''
from mysql.connector.errors import Error
from app.main.models.menuItem import MenuItem, ItemState
from app.main.sqlErrorHandler import logSqlError
from app.utils.responseHandler import makeResponse

class MenuItemService:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    # Add menu item        
    def add_item(self, item_name, category, ingredient_info, rid):
        try:
            cursor = self.db_connection.cursor()
            # Check if an item with similar name exist.
            select_query = "SELECT * FROM menu_items WHERE itemName = %s AND rid = %s"
            data = (item_name, rid,)
            cursor.execute(select_query, data)
            row = cursor.fetchone()
            if row:
                return makeResponse.bad_request("Server Error", "Item already exist")
        
            create_query = "INSERT INTO menu_items (itemName, category, ingredient_info, rid) VALUES (%s, %s, %s, %s)"
            data = (item_name, category, ingredient_info, rid,)
            cursor.execute(create_query, data)
            self.db_connection.commit()
            item_id = cursor.lastrowid
            cursor.close()
            return makeResponse.created("Created new menu item", item_id)
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
    # Get all menu items
    def get_all_items(self):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            select_query = "SELECT * FROM menu_items"
            cursor.execute(select_query)
            results = cursor.fetchall()
            self.db_connection.commit()
            if not results:
                return makeResponse.data_not_found("No data found")
            menuItems = []
            for row in results: 
                menuItem = MenuItem(row['itemId'], row['itemName'], row['category'], row['ingredient_info'], row['verified'], row['rid'], row['item_uri'])
                menuItems.append(menuItem)
            cursor.close()
            menuItems_list = [{'itemId': row.item_id, 'itemName' : row.item_name, 'category' : row.category, 'ingredient_info': row.ingredient_info, 'verified' : row.verified, 'rid' : row.restaurant_id, 'item_uri' : row.item_uri } for row in menuItems]
            return makeResponse.response_ok(menuItems_list)
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
            
    # Get all items of a restaurant using rid
    def get_restaurant_menu(self, rid):
        try:
            cursor = self.db_connection.cursor(dictionary=True)        
            select_query = "SELECT * FROM menu_items WHERE rid = %s"
            cursor.execute(select_query, (rid,))
            items = cursor.fetchall()
            
            # Check if any items with that restaurant id exist.
            if not items:
                return makeResponse.data_not_found("No data exist for this restaurant")
            
            menuItems = []
            for row in items:
                menuItem = MenuItem(row['itemId'], row['itemName'], row['category'], row['ingredient_info'], row['verified'], row['rid'], row['item_uri'])
                menuItems.append(menuItem)
            cursor.close()
            menuItems_list = [{'itemId': row.item_id, 'itemName' : row.item_name, 'category' : row.category, 'ingredient_info': row.ingredient_info, 'verified' : row.verified, 'rid' : row.restaurant_id, 'item_uri' : row.item_uri } for row in menuItems]
            return makeResponse.response_ok(menuItems_list)
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
        
    # Update Menu Item info
    def update_menu_item(self, item_id, item_name, category, ingredient_info):
        try:
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM menu_items WHERE itemId = %s"
            cursor.execute(select_query, (item_id,))
            row = cursor.fetchone()
            if not row:
                return makeResponse.bad_request("Server error", "No such item exist")
                
            update_query = "UPDATE menu_items SET (itemName, category, ingredient_info) VALUES(%s, %s, %s) WHERE itemId = %s"
            data = (item_name, category, ingredient_info, item_id)
            cursor.execute(update_query, data)
            self.db_connection.commit()
            cursor.close()
            return makeResponse.response_ok(item_id)
        except Error as err:
            logSqlError(err)
            desc = {"errno": err.errno, "errmsg" : err.msg}
            return makeResponse.bad_request("Database error", desc)
