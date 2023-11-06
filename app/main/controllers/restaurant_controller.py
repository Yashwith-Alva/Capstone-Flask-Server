'''
A simplified interface used for routing
'''

from flask import jsonify
from services.restaurant_service import RestaurantService

class RestaurantController:
    def __init__(self):
        self.restaurantService_ = RestaurantService()

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
    
    
    
        