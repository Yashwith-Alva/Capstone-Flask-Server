'''
Represents restaurant table in the arfoodmenu database
'''

class Restaurant:
    def __init__(self, restaurant_id, restaurant_name, about, qr, address, location_link):
        self.restaurant_id = restaurant_id
        self.restaurant_name = restaurant_name
        self.about = about
        self.qr = qr
        self.address = address
        self.location_link = location_link
        
    def __repr__(self) -> str:
        return f''' Restaurant Info:
                restaurant_id = '{self.restaurant_id}'
                restaurant_name = '{self.restaurant_name}'
                about = '{self.about}'
                qr = '{self.qr}'
                address = '{self.address}'
                location_link = '{self.location_link}'
            '''