'''
A simplified interface used for routing
'''

from flask import jsonify
from app.main.services.restaurant_service import RestaurantService
import app.main.models.restaurant
from flask import g

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
            return jsonify({'error' : 'Restaurant name is required'}), 400
        
        restaurant_id = self.restaurantService_.create_restaurant(resName, about, qr, address, location_link)
        return jsonify({'message': 'Restaurant created Successfully', 'restaurant id': restaurant_id}), 201
    
    # Return all restaurants
    def get_all_restaurants(self):
        restaurants = self.restaurantService_.get_all_restaurants()
        restaurants_list = [{'rid':row.rid, 'resName': row.resName, 'about': row.about, 'qr': row.qr, 'address':row.address, 'locationLink': row.locationLink} for row in restaurants]
        return jsonify(restaurants_list), 200
    
    # Return restaurant by id
    def get_restaurant_by_id(self, id):
        restaurant = self.restaurantService_.get_restaurant_by_id(id)
        if restaurant:
            return jsonify(restaurant), 200
        else:
            return jsonify(), 404
        
    
    # Return restaurant by qr
    def get_restaurant_by_qr(self, qr):
        restaurant = self.restaurantService_.get_restaurant_by_qr(qr)
        if restaurant:
            return jsonify(restaurant), 200
        else:
            return jsonify(), 404
        