import random
import string

def generate_vin():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(17))

car_types = ['Sedan', 'SUV', 'Compact', 'Electric', 'Hatchback', 'Coupe', 'Convertible', 'Minivan', 'Truck']


cars = [
    {
        "VIN": generate_vin(),
        "Make": "Honda",
        "Model": "Civic",
        "Year": 2020,
        "Color": "Red",
        "Price": 25000,
        "Mileage": 15000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Toyota",
        "Model": "Camry",
        "Year": 2019,
        "Color": "Blue",
        "Price": 28000,
        "Mileage": 20000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Ford",
        "Model": "Mustang",
        "Year": 2021,
        "Color": "Black",
        "Price": 35000,
        "Mileage": 5000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Chevrolet",
        "Model": "Camaro",
        "Year": 2018,
        "Color": "Yellow",
        "Price": 32000,
        "Mileage": 25000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Nissan",
        "Model": "Altima",
        "Year": 2017,
        "Color": "White",
        "Price": 22000,
        "Mileage": 35000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "BMW",
        "Model": "X5",
        "Year": 2020,
        "Color": "Silver",
        "Price": 50000,
        "Mileage": 10000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Mercedes",
        "Model": "C-Class",
        "Year": 2019,
        "Color": "Gray",
        "Price": 45000,
        "Mileage": 18000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Audi",
        "Model": "A4",
        "Year": 2021,
        "Color": "Blue",
        "Price": 40000,
        "Mileage": 8000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Lexus",
        "Model": "RX",
        "Year": 2020,
        "Color": "Black",
        "Price": 55000,
        "Mileage": 12000,
        "Type": random.choice(car_types)
    },
    {
        "VIN": generate_vin(),
        "Make": "Tesla",
        "Model": "Model 3",
        "Year": 2021,
        "Color": "Red",
        "Price": 48000,
        "Mileage": 3000,
        "Type": random.choice(car_types)
    }
]