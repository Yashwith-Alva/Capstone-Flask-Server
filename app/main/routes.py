"""
This module is connected to the init file and hence gets exported down the hierarcy

Author: yashwith alva
Date: 6-11-2023
"""

from . import main_blueprint
from main.controllers import restaurant_controller

# create an object out of the controller
restaurantController = restaurant_controller()

@main_blueprint.route('/resturant', methods=['GET'])
def get_users():
    return restaurantController.get_all_restaurants()