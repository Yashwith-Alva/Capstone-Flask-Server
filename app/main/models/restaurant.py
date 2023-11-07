'''
Represents restaurant table in the arfoodmenu database
'''

class Restaurant:
    def __init__(self, restaurant_id, restaurant_name, about, qr, address, locationLink):
        self.rid = restaurant_id
        self.resName = restaurant_name
        self.about = about
        self.qr = qr
        self.address = address
        self.locationLink = locationLink
        
    def __repr__(self) -> str:
        return f''' Restaurant Info:
                restaurant_id = '{self.rid}'
                restaurant_name = '{self.resName}'
                about = '{self.about}'
                qr = '{self.qr}'
                address = '{self.address}'
                location_link = '{self.locationLink}'
            '''