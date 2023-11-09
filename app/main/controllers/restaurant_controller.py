'''
A simplified interface used for routing
'''

from flask import jsonify
from app.main.services.restaurant_service import RestaurantService, makeResponse

class RestaurantController:
    def __init__(self, db_connection):
        self.restaurantService_ = RestaurantService(db_connection)

    # Create a new restaurant
    def create_restaurant(self, request):
        data = request.get_json()
        resName = data.get('resName')
        about = data.get('about')
        qr = data.get('qr')
        address = data.get('address')
        location_link = data.get('locationLink')
        
        if not resName:
            return makeResponse.bad_request("Server Error", "restaurant_name is required")
        
        return self.restaurantService_.create_restaurant(resName, about, qr, address, location_link)
        
    # Return all restaurants
    def get_all_restaurants(self):
        response = self.restaurantService_.get_all_restaurants()
        return response
        
    # Return restaurant by id
    def get_restaurant_by_id(self, id):
        response = self.restaurantService_.get_restaurant_by_id(id)
        return response
         
    # Return restaurant by qr
    def get_restaurant_by_qr(self, qr):
        response = self.restaurantService_.get_restaurant_by_qr(qr)
        return response
        