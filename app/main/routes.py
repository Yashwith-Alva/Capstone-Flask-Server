"""
This module is connected to the init file and hence gets exported down the hierarcy

Author: yashwith alva
Date: 6-11-2023
"""

from . import main_blueprint
from app.main.controllers import restaurant_controller
from flask import g
from flask import jsonify
from app.mysql_db import get_sqldb


# create an object out of the controller
#restaurantController_ = restaurant_controller.RestaurantController()

@main_blueprint.route('/restaurant', methods=['GET'])
def get_users():
    db_conn = get_sqldb()
    if db_conn is not None:
        restaurantController_= restaurant_controller.RestaurantController(db_conn)
        return restaurantController_.get_all_restaurants()
    else:
        return jsonify({'error' : 'No database connected'}), 505