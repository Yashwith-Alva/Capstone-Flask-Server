'''
A simplified interface used for routing
'''

from flask import jsonify
from services.restaurant_service import RestaurantService
import main.models.restaurant

class RestaurantController:
    def __init__(self):
        self.restaurantService_ = RestaurantService()

    # Create a new restaurant
    def create_restaurant(self, request):
        data = request.get_json()
        resName = data.get('resName')
        about = data.get('about')
        qr = data.get('qr')
        address = data.get('address')
        location_link = data.get('locationLink')
        
        if not resName:
            return jsonify({'error' : 'Restaurant name is required'}), 400
        
        restaurant_id = self.restaurantService_.create_restaurant(resName, about, qr, address, location_link)
        return jsonify({'message': 'Restaurant created Successfully', 'restaurant id': restaurant_id}), 201
    
    # Return all restaurants
    def get_all_restaurants(self):
        restaurants = self.restaurantService_.get_all_restaurants()
        restaurants_list = [{'rid':row.restaurant_id, 'resName': row.restaurant_name, 'about': row.about, 'qr': row.qr, 'address':row.address, 'locationLink': row.locationLink} for row in restaurants]
        return jsonify(restaurants_list), 200
    
    