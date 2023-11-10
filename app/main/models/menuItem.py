from enum import Enum

class ItemState(Enum):
    VERIFIED = 'verified'
    INPROGRESS = 'inprogress'
    REJECTED = 'rejected'

class MenuItem:
    def __init__(self, item_id, item_name, category, ingredient_info, restaurant_id, verified = ItemState.VERIFIED, item_uri = None):
        self.item_id = item_id
        self.item_name = item_name
        self.category = category
        self.ingredient_info = ingredient_info
        self.verified = verified
        self.restaurant_id = restaurant_id
        self.item_uri = item_uri
        
    def __repr__(self) -> str:
        return f""" item_name : {self.item_name},
            category : {self.category},
            ingredient_info : {self.ingredient_info},
            dish_model : {self.dish_model},
            verified(enum) : {self.verified.name.lower()}
            restaurant_id : {self.restaurant_id}
            item_uri : {self.item_uri}
        """
        