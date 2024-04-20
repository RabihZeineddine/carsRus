class Cars:
    def __init__(user, make, model, year, price, color, type, vin, favorites, milage = None):
        user.make = make
        user.model = model
        user.year = year
        user.price = price
        user.color = color
        user.type = type
        user.vin = vin

    #set functions
    def set_make(user, make):
        user.make = make

    def set_model(user, model):
        user.model = model

    def set_year(user, year):
        user.year = year
        
    def set_price(user, price):
        user.price = price

    def set_color(user, color):
        user.color = color

    def set_type(user, type):
        user.type = type

    def set_vin(user, vin):
        user.vin = vin

    def set_color(user, color):
        user.color = color

    def add_to_fav(user):
        user.favorites = True

    def remove_from_fav(user):
        user.favorites = False

    #get functions
    def get_make(user):
        return user.make

    def get_model(user):
        return user.model

    def get_year(user):
        return user.year

    def get_price(user):
        return user.price

    def get_color(user):
        return user.color

    def get_type(user):
        return user.type

    def get_vin(user):
        return user.vin

user_list = []

def add_car(car):
    user_list.append(car)
