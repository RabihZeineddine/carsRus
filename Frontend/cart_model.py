from car_data import cars

class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []
    
    def add_to_cart(self, car_id, quantity=1):
        self.items.append({'car_id': car_id, 'quantity': quantity})
    
    def remove_from_cart(self, car_id):
        self.items = [item for item in self.items if item['car_id'] != car_id]
    
    def get_total_price(self):
        total = 0
        for item in self.items:
            car = next((car for car in cars if car['VIN'] == item['car_id']), None)
            if car:
                total += car['Price'] * item['quantity']
        return total