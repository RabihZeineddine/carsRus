class Cars:
    def __init__(self, make, model, year, price, color, type, vin, favorites, milage = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.type = type
        self.vin = vin

    #set functions
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year
        
    def set_price(self, price):
        self.price = price

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_vin(self, vin):
        self.vin = vin

    def set_color(self, color):
        self.color = color

    def add_to_fav(self):
        self.favorites = True

    def remove_from_fav(self):
        self.favorites = False

    #get functions
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_vin(self):
        return self.vin

self_list = []

def add_car(car):
    self_list.append(car)
