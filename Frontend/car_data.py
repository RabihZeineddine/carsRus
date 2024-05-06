import random
import string

def generate_vin():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(17))

car_types = ['Sedan', 'SUV', 'Compact', 'Electric', 'Hatchback', 'Coupe', 'Convertible', 'Van', 'Truck']

cars = [
    {
        "VIN": generate_vin(),
        "Make": "Ford",
        "Model": "Mustang",
        "Year": 2021,
        "Color": "Black",
        "Price": 35000,
        "Mileage": 5000,
        "Type": 'Coupe'
    },
    {
        "VIN": generate_vin(),
        "Make": "Audi",
        "Model": "A4",
        "Year": 2021,
        "Color": "Blue",
        "Price": 40000,
        "Mileage": 8000,
        "Type": 'Sedan'
    },
    {
        "VIN": generate_vin(),
        "Make": "Tesla",
        "Model": "Model 3",
        "Year": 2021,
        "Color": "Red",
        "Price": 48000,
        "Mileage": 3000,
        "Type": 'Electric'
    },
    {
        "VIN": generate_vin(),
        "Make": "BMW",
        "Model": "X5",
        "Year": 2020,
        "Color": "Silver",
        "Price": 50000,
        "Mileage": 10000,
        "Type": 'SUV'
    },
    {
        "VIN": generate_vin(),
        "Make": "Lexus",
        "Model": "RX",
        "Year": 2020,
        "Color": "Black",
        "Price": 55000,
        "Mileage": 12000,
        "Type": 'SUV'
    },
    {
        "VIN": generate_vin(),
        "Make": "Honda",
        "Model": "Civic",
        "Year": 2020,
        "Color": "Red",
        "Price": 25000,
        "Mileage": 15000,
        "Type": 'Sedan'
    },
    {
        "VIN": generate_vin(),
        "Make": "Mercedes",
        "Model": "C-Class",
        "Year": 2019,
        "Color": "Gray",
        "Price": 45000,
        "Mileage": 18000,
        "Type": 'Sedan'
    },
    {
        "VIN": "789321654",
        "Model": "Tundra",
        "Make": "Toyota",
        "Color": "Black",
        "Year": 2022,
        "Price": 29600,
        "Mileage": 21600,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Make": "Toyota",
        "Model": "Camry",
        "Year": 2019,
        "Color": "Blue",
        "Price": 28000,
        "Mileage": 20000,
        "Type": 'Sedan'
    },
    {
        "VIN": generate_vin(),
        "Make": "Chevrolet",
        "Model": "Camaro",
        "Year": 2018,
        "Color": "Yellow",
        "Price": 32000,
        "Mileage": 25000,
        "Type": 'Coupe'
    },
    {
        "VIN": generate_vin(),
        "Make": "Nissan",
        "Model": "Altima",
        "Year": 2017,
        "Color": "White",
        "Price": 22000,
        "Mileage": 35000,
        "Type": 'Sedan'
    },
    {
       "VIN": generate_vin(),
        "Model": "Civic",
        "Make": "Honda",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Accord",
        "Make": "Honda",
        "Color": "Blue",
        "Year": 2018,
        "Price": 23500,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "CR-V",
        "Make": "Honda",
        "Color": "Silver",
        "Year": 2019,
        "Price": 27800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Pilot",
        "Make": "Honda",
        "Color": "Black",
        "Year": 2017,
        "Price": 28200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Odyssey",
        "Make": "Honda",
        "Color": "White",
        "Year": 2022,
        "Price": 32500,
        "Mileage": 12500,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Odyssey",
        "Make": "Honda",
        "Color": "Red",
        "Year": 2023,
        "Price": 33200,
        "Mileage": 11500,
        "Type": "Van"
    },
    {   
        "VIN": generate_vin(),
        "Model": "Odyssey",
        "Make": "Honda",
        "Color": "Black",
        "Year": 2022,
        "Price": 34000,
        "Mileage": 13200,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Odyssey",
        "Make": "Honda",
        "Color": "Silver",
        "Year": 2017,
        "Price": 32700,
        "Mileage": 22200,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Odyssey",
        "Make": "Honda",
        "Color": "Blue",
        "Year": 2017,
        "Price": 33400,
        "Mileage": 23500,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Odyssey",
        "Make": "Honda",
        "Color": "Red",
        "Year": 2020,
        "Price": 32800,
        "Mileage": 24100,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Civic",
        "Make": "Honda",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Accord",
        "Make": "Honda",
        "Color": "Blue",
        "Year": 2018,
        "Price": 23500,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "CR-V",
        "Make": "Honda",
        "Color": "Silver",
        "Year": 2019,
        "Price": 27800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Pilot",
        "Make": "Honda",
        "Color": "Black",
        "Year": 2017,
        "Price": 28200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Corolla",
        "Make": "Toyota",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Camry",
        "Make": "Toyota",
        "Color": "Blue",
        "Year": 2018,
        "Price": 23500,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Sienna",
        "Make": "Toyota",
        "Color": "Blue",
        "Year": 2022,
        "Price": 21900,
        "Mileage": 9800,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Sienna",
        "Make": "Toyota",
        "Color": "Blue",
        "Year": 2020,
        "Price": 21400,
        "Mileage": 14500,
        "Type": "Van"
    },
    {
        "VIN": "456321987",
        "Model": "Sienna",
        "Make": "Toyota",
        "Color": "Gray",
        "Year": 2020,
        "Price": 22000,
        "Mileage": 16900,
        "Type": "Van"
    },

    {
        "VIN": generate_vin(),
        "Model": "Sienna",
        "Make": "Toyota",
        "Color": "Silver",
        "Year": 2018,
        "Price": 22300,
        "Mileage": 19500,
        "Type": "Van"
    },
    {
        "VIN": generate_vin(),
        "Model": "Rav4",
        "Make": "Toyota",
        "Color": "Silver",
        "Year": 2019,
        "Price": 27800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Highlander",
        "Make": "Toyota",
        "Color": "Black",
        "Year": 2017,
        "Price": 28200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": "987321654",
        "Model": "Tacoma",
        "Make": "Toyota",
        "Color": "Black",
        "Year": 2022,
        "Price": 29600,
        "Mileage": 21600,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Tacoma",
        "Make": "Toyota",
        "Color": "White",
        "Year": 2022,
        "Price": 32500,
        "Mileage": 12500,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Corolla",
        "Make": "Toyota",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Camry",
        "Make": "Toyota",
        "Color": "Blue",
        "Year": 2018,
        "Price": 23500,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Rav4",
        "Make": "Toyota",
        "Color": "Silver",
        "Year": 2019,
        "Price": 27800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Highlander",
        "Make": "Toyota",
        "Color": "Black",
        "Year": 2017,
        "Price": 28200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Tacoma",
        "Make": "Toyota",
        "Color": "White",
        "Year": 2022,
        "Price": 32500,
        "Mileage": 12500,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Altima",
        "Make": "Nissan",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Sentra",
        "Make": "Nissan",
        "Color": "Blue",
        "Year": 2018,
        "Price": 23500,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Rogue",
        "Make": "Nissan",
        "Color": "Silver",
        "Year": 2019,
        "Price": 27800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Murano",
        "Make": "Nissan",
        "Color": "Black",
        "Year": 2017,
        "Price": 28200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Frontier",
        "Make": "Nissan",
        "Color": "White",
        "Year": 2022,
        "Price": 32500,
        "Mileage": 12500,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Pathfinder",
        "Make": "Nissan",
        "Color": "Gray",
        "Year": 2023,
        "Price": 27000,
        "Mileage": 14500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Maxima",
        "Make": "Nissan",
        "Color": "Green",
        "Year": 2018,
        "Price": 21400,
        "Mileage": 19800,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Titan",
        "Make": "Nissan",
        "Color": "Red",
        "Year": 2021,
        "Price": 30900,
        "Mileage": 16200,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Altima",
        "Make": "Nissan",
        "Color": "Blue",
        "Year": 2017,
        "Price": 19800,
        "Mileage": 25000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Sentra",
        "Make": "Nissan",
        "Color": "Black",
        "Year": 2019,
        "Price": 24600,
        "Mileage": 17500,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Rogue",
        "Make": "Nissan",
        "Color": "White",
        "Year": 2020,
        "Price": 29000,
        "Mileage": 14000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Fusion",
        "Make": "Ford",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Focus",
        "Make": "Ford",
        "Color": "Blue",
        "Year": 2018,
        "Price": 23500,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Escape",
        "Make": "Ford",
        "Color": "Silver",
        "Year": 2019,
        "Price": 27800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Explorer",
        "Make": "Ford",
        "Color": "Black",
        "Year": 2017,
        "Price": 28200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "F-150",
        "Make": "Ford",
        "Color": "White",
        "Year": 2022,
        "Price": 32500,
        "Mileage": 12500,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Expedition",
        "Make": "Ford",
        "Color": "Gray",
        "Year": 2023,
        "Price": 27000,
        "Mileage": 14500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Mustang",
        "Make": "Ford",
        "Color": "Green",
        "Year": 2018,
        "Price": 21400,
        "Mileage": 19800,
        "Type": "Sports Car"
    },
    {
        "VIN": generate_vin(),
        "Model": "Ranger",
        "Make": "Ford",
        "Color": "Red",
        "Year": 2021,
        "Price": 30900,
        "Mileage": 16200,
        "Type": "Truck"
    },
    {
        "VIN": generate_vin(),
        "Model": "Fusion",
        "Make": "Ford",
        "Color": "Blue",
        "Year": 2017,
        "Price": 19800,
        "Mileage": 25000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Focus",
        "Make": "Ford",
        "Color": "Black",
        "Year": 2019,
        "Price": 24600,
        "Mileage": 17500,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Impreza",
        "Make": "Subaru",
        "Color": "Red",
        "Year": 2020,
        "Price": 25000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Outback",
        "Make": "Subaru",
        "Color": "Blue",
        "Year": 2018,
        "Price": 32500,
        "Mileage": 20000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Forester",
        "Make": "Subaru",
        "Color": "Silver",
        "Year": 2019,
        "Price": 29800,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Crosstrek",
        "Make": "Subaru",
        "Color": "Black",
        "Year": 2017,
        "Price": 27200,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Legacy",
        "Make": "Subaru",
        "Color": "White",
        "Year": 2022,
        "Price": 32000,
        "Mileage": 12500,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Ascent",
        "Make": "Subaru",
        "Color": "Gray",
        "Year": 2023,
        "Price": 38000,
        "Mileage": 14500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Impreza",
        "Make": "Subaru",
        "Color": "Green",
        "Year": 2018,
        "Price": 26500,
        "Mileage": 19800,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Outback",
        "Make": "Subaru",
        "Color": "Red",
        "Year": 2021,
        "Price": 33500,
        "Mileage": 16200,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Forester",
        "Make": "Subaru",
        "Color": "Blue",
        "Year": 2017,
        "Price": 28800,
        "Mileage": 25000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Crosstrek",
        "Make": "Subaru",
        "Color": "Black",
        "Year": 2019,
        "Price": 29800,
        "Mileage": 17500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "C-Class",
        "Make": "Mercedes",
        "Color": "Red",
        "Year": 2020,
        "Price": 45000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "E-Class",
        "Make": "Mercedes",
        "Color": "Blue",
        "Year": 2018,
        "Price": 55000,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "GLC-Class",
        "Make": "Mercedes",
        "Color": "Silver",
        "Year": 2019,
        "Price": 52000,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "GLE-Class",
        "Make": "Mercedes",
        "Color": "Black",
        "Year": 2017,
        "Price": 68000,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "A-Class",
        "Make": "Mercedes",
        "Color": "White",
        "Year": 2022,
        "Price": 39000,
        "Mileage": 12500,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "S-Class",
        "Make": "Mercedes",
        "Color": "Gray",
        "Year": 2023,
        "Price": 95000,
        "Mileage": 14500,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "C-Class",
        "Make": "Mercedes",
        "Color": "Green",
        "Year": 2018,
        "Price": 48000,
        "Mileage": 19800,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "GLC-Class",
        "Make": "Mercedes",
        "Color": "Red",
        "Year": 2021,
        "Price": 54000,
        "Mileage": 16200,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "E-Class",
        "Make": "Mercedes",
        "Color": "Blue",
        "Year": 2017,
        "Price": 58000,
        "Mileage": 25000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "GLE-Class",
        "Make": "Mercedes",
        "Color": "Black",
        "Year": 2019,
        "Price": 72000,
        "Mileage": 17500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "3 Series",
        "Make": "BMW",
        "Color": "Red",
        "Year": 2020,
        "Price": 48000,
        "Mileage": 15000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "5 Series",
        "Make": "BMW",
        "Color": "Blue",
        "Year": 2018,
        "Price": 58000,
        "Mileage": 20000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "X3",
        "Make": "BMW",
        "Color": "Silver",
        "Year": 2019,
        "Price": 55000,
        "Mileage": 18500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "X5",
        "Make": "BMW",
        "Color": "Black",
        "Year": 2017,
        "Price": 75000,
        "Mileage": 22000,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "2 Series",
        "Make": "BMW",
        "Color": "White",
        "Year": 2022,
        "Price": 42000,
        "Mileage": 12500,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "2 Series",
        "Make": "BMW",
        "Color": "Black",
        "Year": 2020,
        "Price": 44000,
        "Mileage": 15700,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "2 Series",
        "Make": "BMW",
        "Color": "Black",
        "Year": 2017,
        "Price": 45000,
        "Mileage": 21000,
        "Type": "Coupe"
    },

    {
        "VIN": generate_vin(),
        "Model": "7 Series",
        "Make": "BMW",
        "Color": "Gray",
        "Year": 2023,
        "Price": 92000,
        "Mileage": 14500,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "3 Series",
        "Make": "BMW",
        "Color": "Green",
        "Year": 2018,
        "Price": 52000,
        "Mileage": 19800,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "X3",
        "Make": "BMW",
        "Color": "Red",
        "Year": 2021,
        "Price": 58000,
        "Mileage": 16200,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "5 Series",
        "Make": "BMW",
        "Color": "Blue",
        "Year": 2017,
        "Price": 62000,
        "Mileage": 25000,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "X5",
        "Make": "BMW",
        "Color": "Black",
        "Year": 2019,
        "Price": 78000,
        "Mileage": 17500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model 3",
        "Make": "Tesla",
        "Color": "Red",
        "Year": 2020,
        "Price": 45000,
        "Mileage": 15000,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model S",
        "Make": "Tesla",
        "Color": "Blue",
        "Year": 2018,
        "Price": 85000,
        "Mileage": 20000,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model X",
        "Make": "Tesla",
        "Color": "Silver",
        "Year": 2019,
        "Price": 95000,
        "Mileage": 18500,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model Y",
        "Make": "Tesla",
        "Color": "Black",
        "Year": 2017,
        "Price": 55000,
        "Mileage": 22000,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Roadster",
        "Make": "Tesla",
        "Color": "White",
        "Year": 2022,
        "Price": 200000,
        "Mileage": 12500,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model 3",
        "Make": "Tesla",
        "Color": "Gray",
        "Year": 2023,
        "Price": 47000,
        "Mileage": 14500,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model S",
        "Make": "Tesla",
        "Color": "Green",
        "Year": 2018,
        "Price": 90000,
        "Mileage": 19800,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model X",
        "Make": "Tesla",
        "Color": "Red",
        "Year": 2021,
        "Price": 105000,
        "Mileage": 16200,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model Y",
        "Make": "Tesla",
        "Color": "Blue",
        "Year": 2017,
        "Price": 58000,
        "Mileage": 25000,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "Model 3",
        "Make": "Tesla",
        "Color": "Black",
        "Year": 2019,
        "Price": 49000,
        "Mileage": 19800,
        "Type": "Electric"
    },
    {
        "VIN": generate_vin(),
        "Model": "488 GTB",
        "Make": "Ferrari",
        "Color": "Red",
        "Year": 2020,
        "Price": 300000,
        "Mileage": 5000,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "812 Superfast",
        "Make": "Ferrari",
        "Color": "Yellow",
        "Year": 2018,
        "Price": 350000,
        "Mileage": 8000,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "SF90 Stradale",
        "Make": "Ferrari",
        "Color": "Black",
        "Year": 2021,
        "Price": 500000,
        "Mileage": 2000,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "Huracan",
        "Make": "Lamborghini",
        "Color": "Yellow",
        "Year": 2020,
        "Price": 250000,
        "Mileage": 5000,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "Portofino",
        "Make": "Ferrari",
        "Color": "Blue",
        "Year": 2019,
        "Price": 250000,
        "Mileage": 10000,
        "Type": "Convertible"
    },
    {
        "VIN": generate_vin(),
        "Model": "Aventador",
        "Make": "Lamborghini",
        "Color": "Blue",
        "Year": 2018,
        "Price": 400000,
        "Mileage": 8000,
        "Type": "Coupe"
    },
    {
        "VIN": generate_vin(),
        "Model": "718 Boxster",
        "Make": "Porsche",
        "Color": "White",
        "Year": 2020,
        "Price": 85000,
        "Mileage": 13000,
        "Type": "Convertible"
    },
    {
        "VIN": generate_vin(),
        "Model": "Beetle",
        "Make": "Volkswagen",
        "Color": "Green",
        "Year": 2018,
        "Price": 20000,
        "Mileage": 19800,
        "Type": "Convertible"
    },
    {
        "VIN": generate_vin(),
        "Model": "ID.4",
        "Make": "Volkswagen",
        "Color": "Red",
        "Year": 2021,
        "Price": 38000,
        "Mileage": 16200,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Golf GTI",
        "Make": "Volkswagen",
        "Color": "Blue",
        "Year": 2017,
        "Price": 30000,
        "Mileage": 25000,
        "Type": "Hatchback"
    },
    {
        "VIN": generate_vin(),
        "Model": "Jetta",
        "Make": "Volkswagen",
        "Color": "Black",
        "Year": 2019,
        "Price": 23000,
        "Mileage": 19800,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Passat",
        "Make": "Volkswagen",
        "Color": "White",
        "Year": 2020,
        "Price": 27000,
        "Mileage": 16200,
        "Type": "Sedan"
    },
    {
        "VIN": generate_vin(),
        "Model": "Tiguan",
        "Make": "Volkswagen",
        "Color": "Silver",
        "Year": 2018,
        "Price": 29000,
        "Mileage": 21300,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Atlas",
        "Make": "Volkswagen",
        "Color": "Red",
        "Year": 2022,
        "Price": 33000,
        "Mileage": 11500,
        "Type": "SUV"
    },
    {
        "VIN": generate_vin(),
        "Model": "Golf",
        "Make": "Volkswagen",
        "Color": "Black",
        "Year": 2020,
        "Price": 26000,
        "Mileage": 5000,
        "Type": "Hatchback"
    },
    {
        "VIN": generate_vin(),
        "Model": "Passat",
        "Make": "Volkswagen",
        "Color": "Gray",
        "Year": 2021,
        "Price": 28000,
        "Mileage": 15700,
        "Type": "Sedan"
    }
]
