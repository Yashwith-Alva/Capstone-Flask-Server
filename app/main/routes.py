"""
This module is connected to the init file and hence gets exported down the hierarcy
- Module is divided into controller sections
- Module also has a util section which consist of API calls

Author: yashwith alva
Date: 6-11-2023
"""

from . import main_blueprint
from flask import jsonify, request
from markupsafe import escape
from app.mysql_db import get_sqldb
from app.main.controllers import restaurant_controller
from app.main.controllers import user_controller



############################################################################################
# INTERFACE METHODS
############################################################################################

# [POST] Add new Restaurant
# [POST] Add new User and Menu with user_id, password, rid



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
        return jsonify({'error' : 'No database connected'}), 500
    
    
# [GET] Restaurant with Unique Id
# [POST] Update restaurant information with Id
@main_blueprint.route('/restaurant/<int:restaurant_id>', methods = ['GET'])
def restaurant_by_id(restaurant_id):
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        response =  restaurantController_.get_restaurant_by_id(restaurant_id)
        if response is not None:
            return response
    else:
        return jsonify({'error' : 'No database connected'}), 500
    

# [GET] Restaurant with Unique QR
@main_blueprint.route('/restaurant/qrcode/<string:qr>', methods = ['GET'])
def get_restaurant_by_qr(qr):
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        response = restaurantController_.get_restaurant_by_qr(qr)
        return response
    else:
        return jsonify({'error': 'No database is connected'}), 500
        
        
# [POST] Create a new Restaurant
@main_blueprint.route('/restaurant/register', methods=['POST'])
def create_restaurant():
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        response = restaurantController_.create_restaurant(request)
        return response
    else:
        return jsonify({'error': 'No database is connected'}), 500

############################################################################################
# USER METHODS
############################################################################################

# [GET] Fetch all user information

# [POST] UserId and Password and rId
# Check if rId already exists. Since there is a foreign key constraint this may crash
@main_blueprint.route('/user/register', methods = ['POST'])
def create_user():
    db_conn = get_sqldb()
    if db_conn is not None:
        userController_ = user_controller.UserController(db_conn)
        response = userController_.create_user(request)
        return response
    else:
        return jsonify({'error': 'No database is connected'})

############################################################################################
# MENU METHODS
############################################################################################

# [POST] Create a menu Item

############################################################################################
# MENU ITEMS METHODS
############################################################################################



############################################################################################
# NUTRITION METHODS
############################################################################################


