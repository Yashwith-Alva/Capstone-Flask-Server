from flask import jsonify
from app.main.services.menuItem_service import MenuItemService, makeResponse

class MenuItemController:
    def __init__(self, db_connection):
        self.menuItemService_ = MenuItemService(db_connection)
        
    # Add a new Item
    def add_menuItem(self, request):
        data = request.get_json()
        item_name = data.get('itemName')
        category = data.get('category')
        ingredient_info = data.get('ingredient_info')
        verified = data.get('verified')
        rid = data.get('rid')
        item_uri = data.get('item_uri')
        
        if not item_name:
            return makeResponse.bad_request("Server Error", "Menu Item Name is required")
        elif not rid:
            return makeResponse.bad_request("Server Error", "Restaurant Id is required")
        
        return self.menuItemService_.add_item(item_name, category, ingredient_info, rid)
    
    # Get all items
    def get_all_menuItems(self):
        return self.menuItemService_.get_all_items()
    
    # Get items belonging to particular restaurant id
    def get_restaurant_menu(self, resaturant_id):
        return self.menuItemService_.get_restaurant_menu(resaturant_id)
        
    # Update menu_item of a using item_id
    def update_menuItem_by_id(self, request):
        data = request.get_json()
        item_id = data.get('itemId')
        item_name = data.get('itemName')
        category = data.get('category')
        ingredient_info = data.get('ingredient_info')
        rid = data.get('rid')
        
        if not item_id or not rid:
            return makeResponse.bad_request("Server Error", "Item id and rid is required")
            
        return self.menuItemService_.update_menu_item(item_id, item_name, category, ingredient_info, rid)
           
        
        