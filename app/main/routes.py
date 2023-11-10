"""
This module is connected to the init file and hence gets exported down the hierarcy
- Module is divided into controller sections
- Module also has a util section which consist of API calls

Author: yashwith alva
Date: 6-11-2023
"""

from . import main_blueprint
from flask import jsonify, request
from app.mysql_db import get_sqldb
from app.utils.responseHandler import makeResponse
from app.main.controllers import restaurant_controller, user_controller, menuItem_controller, nutrition_controller


''''
All Useful Routes:

1. For RESTAURANT related:
    "/restaurant" : GET method will give all items
                  : POST method will create an item

    "/restaurant/<int:item_id>"          : GET method will fetch restaurant of that id.
    "/restaurant/qrcode/<string:qrcode>" : GET method will fetch restaurant with that qr code.
    
2. For USER related:
    "/user/register"        : POST method will create a new register
    "/update/user/userid"   : POST method will update userId using password and rid.
    "/update/user/password" : POST method will update password using userId and rid.

3. For MENU_ITEM related:
    "/restaurant/menu"      : GET method will get all the menu items irrespective of restaurant
                            : POST method will create a new menu item
    
    "/restaurant/menu/<int:rid>           : GET method will fetch menu_items of particular restaurant
    "/update/restaurant/menu/<int:item_id : POST method will update a menu_item of particular item_id

4. For NUTRITION related:
    "/restaurant/menu/nutrition" : GET method will fetch all the nutrition items
                                 : POST method will create a new nutrition item
                                 
    "/restaurant/menu/nutrition/<int:item_id> : GET method will fetch nutrition of that particular item
    "/update/restaurant/menu/nutrition        : POST method will update the particular nutrition
'''



############################################################################################
# RESTAURANT METHODS
############################################################################################

# [GET] All restaurant info
@main_blueprint.route('/restaurant', methods=['GET'])
def restaurant_methods():
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_= restaurant_controller.RestaurantController(db_conn)
        return restaurantController_.get_all_restaurants()
    else:
        return makeResponse.db_conn_error()
    
    
# [GET] Restaurant with Unique Id
# [POST] Update restaurant information with Id
@main_blueprint.route('/restaurant/<int:restaurant_id>', methods = ['GET'])
def restaurant_by_id(restaurant_id):
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        response =  restaurantController_.get_restaurant_by_id(restaurant_id)
        return response
    else:
        return makeResponse.db_conn_error()
    

# [GET] Restaurant with Unique QR
@main_blueprint.route('/restaurant/qrcode/<string:qr>', methods = ['GET'])
def get_restaurant_by_qr(qr):
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        response = restaurantController_.get_restaurant_by_qr(qr)
        return response
    else:
        return makeResponse.db_conn_error()
        
        
# [POST] Create a new Restaurant
@main_blueprint.route('/restaurant', methods=['POST'])
def create_restaurant():
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        response = restaurantController_.create_restaurant(request)
        return response
    else:
        return makeResponse.db_conn_error()



############################################################################################
# USER METHODS
############################################################################################

# [POST] UserId and Password and rId
@main_blueprint.route('/user/register', methods = ['POST'])
def create_user():
    db_conn = get_sqldb()
    if db_conn is not None:
        userController_ = user_controller.UserController(db_conn)
        response = userController_.create_user(request)
        return response
    else:
        return makeResponse.db_conn_error()

# [POST] UserId and restaurant_id
@main_blueprint.route('/update/user/userid', methods = ['POST'])
def update_userid():
    db_conn = get_sqldb()
    if db_conn is not None:
        userController_ = user_controller.UserController(db_conn)
        response = userController_.update_userId(request)
        return response
    else:
        return makeResponse.db_conn_error()

# [POST] Password and restaurant_id
@main_blueprint.route('/update/user/password', methods = ['POST'])
def update_password():
    db_conn = get_sqldb()
    if db_conn is not None:
        userController_ = user_controller.UserController(db_conn)
        response = userController_.update_password(request)
        return response
    else:
        return makeResponse.db_conn_error()



############################################################################################
# MENU Item METHODS
############################################################################################

# [POST] Create a menu Item
@main_blueprint.route("/restaurant/menu/", methods=['POST'])
def create_menu_item():
    db_conn = get_sqldb()
    if db_conn is not None:
        response = menuItem_controller.MenuItemController(db_conn).add_menuItem(request)
        return response
    else:
        return makeResponse.db_conn_error()

# [GET] Fetch all items
@main_blueprint.route("/restaurant/menu/", methods=['GET'])
def fetchAll_menu_items():
    db_conn = get_sqldb()
    if db_conn is not None:
        response = menuItem_controller.MenuItemController(db_conn).get_all_menuItems()
        return response
    else:
        return makeResponse.db_conn_error()

# [GET] Fetch particular menu by restaurant id
@main_blueprint.route("/restaurant/menu/<int:restaurant_id>", methods=['GET'])
def fetch_restaurant_menu(restaurant_id):
    db_conn = get_sqldb()
    if db_conn is not None:
        menuItemController_ = menuItem_controller.MenuItemController(db_conn)
        response = menuItemController_.get_restaurant_menu(restaurant_id)
        return response
    else:
        return makeResponse.db_conn_error()

# [POST] Update menu_item by item_id
@main_blueprint.route("/restaurant/menu/update", methods=['POST'])
def update_menu_item():
    db_conn = get_sqldb()
    if db_conn is not None:
        menuItemController_ = menuItem_controller.MenuItemController(db_conn)
        response = menuItemController_.update_menuItem_by_id(request)
        return response
    else:
        return makeResponse.db_conn_error()



############################################################################################
# NUTRITION METHODS
############################################################################################

# [POST] Create new nutrition
@main_blueprint.route("restaurant/menu/nutrition", methods = ['POST'])
def create_nutrition():
    db_conn = get_sqldb()
    if db_conn is not None:
        nutrtionController_ = nutrition_controller.NutritionController(db_conn)
        response = nutrtionController_.create_new_nutrition(request)
        return response
    else:
        return makeResponse.db_conn_error()
    
# [GET] Fetch all nutritions
@main_blueprint.route("restaurant/menu/nutrition", methods = ['GET'])
def fetchall_nutritions():
    db_conn = get_sqldb()
    if db_conn is not None:
        nutrtionController_ = nutrition_controller.NutritionController(db_conn)
        response = nutrtionController_.get_all_nutritions()
        return response
    else:
        return makeResponse.db_conn_error()

# [GET] Fetch nutrition based on item_id
@main_blueprint.route("/restaurant/menu/nutrition/<int:item_id>", methods=['GET'])
def fetch_nutrition_by_itemId(item_id):
    db_conn = get_sqldb()
    if db_conn is not None:
        nutrtionController_ = nutrition_controller.NutritionController(db_conn)
        response = nutrtionController_.get_nutrition_by_itemId(item_id)
        return response
    else:
        return makeResponse.db_conn_error()

# [POST] Update the nutrition of the particular item_id
@main_blueprint.route("/restaurant/menu/nutrition/update", methods = ['POST'])
def update_nutrition_by_itemId():
    db_conn = get_sqldb()
    if db_conn is not None:
        nutrtionController_ = nutrition_controller.NutritionController(db_conn)
        response = nutrtionController_.update_nutrtion_by_id(request)
        return response
    else:
        return makeResponse.db_conn_error()