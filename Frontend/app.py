from flask import Flask, render_template, request
from car_data import cars

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/search-results')
def search_results():
    search_query = request.args.get('query', '')
    filter_type = request.args.get('filter', '')
    
    filtered_cars = cars
    
    if search_query:
        filtered_cars = [car for car in filtered_cars if search_query.lower() in car['Make'].lower() or search_query.lower() in car['Model'].lower()]
    
    if filter_type == 'year':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Year'], reverse=True)
    elif filter_type == 'make':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Make'])
    elif filter_type == 'model':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Model'])
    elif filter_type == 'price':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Price'])
    elif filter_type == 'mileage':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Mileage'])
    
    return render_template('search_results.html', cars=filtered_cars, search_query=search_query, filter_type=filter_type)

# @app.route('/search_results')
# def search_results():
#     return render_template('search_results.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)