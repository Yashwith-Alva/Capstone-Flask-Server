from flask import jsonify
from app.main.services.nutrition_service import NutritionService, FoodType
from app.utils.responseHandler import makeResponse

class NutritionController:
    def __init__(self, db_connection):
        self.nutritionService_ = NutritionService(db_connection)
        
    # Create a new nutrition
    def create_new_nutrition(self, request):
        data = request.get_json()
        item_id = data.get('itemId')
        energy = data.get('energy')
        protein = data.get('protein')
        carbohydrate = data.get('carbohydrate')
        fat = data.get('fat')
        foodType = data.get('foodType')
        
        if not item_id or not foodType:
            makeResponse.bad_request("Server Error", "Item id and foodType are must")
            
        return self.nutritionService_.create_nutrition(item_id, energy, protein, carbohydrate, fat, foodType)
    
    # Get all nutrition items
    def get_all_nutritions(self):
        return self.nutritionService_.get_all_nutrition()
    
    # Get nutrition by item_id
    def get_nutrition_by_itemId(self, item_id):
        if not item_id:
            return makeResponse.bad_request("Server error", "No item_id")
        return self.nutritionService_.get_nutrition_by_id(item_id)
    
    # Update nutrition by item_id
    def update_nutrtion_by_id(self, request):
        data = request.get_json()
        item_id = data.get('itemId')
        energy = data.get('energy')
        protein = data.get('protein')
        carbohydrate = data.get('carbohydrate')
        fat = data.get('fat')
        foodType = data.get('foodType')
        
        if not item_id:
            makeResponse.bad_request("Server Error", "Item id and foodType are must")
        
        return self.nutritionService_.update_nutrition_info(item_id, energy, protein, carbohydrate, fat, foodType)
    