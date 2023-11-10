from enum import Enum

class FoodType(Enum):
    VEG  = 'VEG'
    NONVEG = 'NON-VEG'

class Nutrition:
    def __init__(self, nutritionId, energy, protein, carbohydrate, fat, foodType):
        self.nutrition_id = nutritionId
        self.energy = energy
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat
        self.foodType = foodType
        
    def __repr__(self) -> str:
        return f'''
            nutritionId : {self.nutrition_id}
            energy : {self.energy}
            protein : {self.protein}
            carbohydrate : {self.carbohydrate}
            fat : {self.fat}
            foodType : {self.veg}
            '''