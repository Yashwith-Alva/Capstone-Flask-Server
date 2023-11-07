"""
This module is connected to the init file and hence gets exported down the hierarcy

Author: yashwith alva
Date: 6-11-2023
"""

from . import main_blueprint
from flask import jsonify, request
from markupsafe import escape
from app.mysql_db import get_sqldb
from app.main.controllers import restaurant_controller


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
        result =  restaurantController_.get_restaurant_by_id(restaurant_id)
        if result is not None:
            return result
    else:
        return jsonify({'error' : 'No database connected'}), 500
    

# [GET] Restaurant with Unique QR
@main_blueprint.route('/restaurant/qrcode/<string:qr>', methods = ['GET'])
def get_restaurant_by_qr(qr):
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_ = restaurant_controller.RestaurantController(db_conn)
        result = restaurantController_.get_restaurant_by_qr(qr)
        if result is not None:
            return result
        else:
            return jsonify({'error': 'No database is connected'}), 500
        