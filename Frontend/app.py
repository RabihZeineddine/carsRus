from flask import Flask, render_template, request, redirect, url_for, session
from car_data import cars
from user_data import users

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = next((user for user in users if user['Email'] == email and user['Password'] == password), None)
        
        if user:
            session['user'] = user
            return redirect(url_for('index'))
        else:
            return "Invalid email or password. Please try again."
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match. Please try again." 
        
        new_user = {
            "isAdmin": False,
            "Email": email,
            "Password": password,
            "FirstName": first_name,
            "LastName": last_name
        }
        
        users.append(new_user)
        
        return redirect(url_for('login'))
    
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
        if filter_type == 'year':
            try:
                start_year, end_year = map(int, search_query.split(','))
                if start_year > end_year:
                    temp = start_year
                    start_year = end_year
                    end_year = temp
                filtered_cars = [car for car in filtered_cars if start_year <= car['Year'] <= end_year]
                filtered_cars = sorted(filtered_cars, key=lambda x: x['Year'])
            except (ValueError, TypeError):
                pass
        elif  filter_type == 'price':
            try:
                max_price = float(search_query)
                filtered_cars = [car for car in filtered_cars if float(car['Price']) <= max_price]
            except ValueError:
                pass
        elif filter_type == 'mileage':
            try:
                max_mileage = float(search_query)
                filtered_cars = [car for car in filtered_cars if float(car['Mileage']) <= max_mileage]
            except ValueError:
                pass
        elif filter_type == 'type':
            filtered_cars = [car for car in filtered_cars if search_query.lower() in car['Type'].lower()]
        else:
            filtered_cars = [car for car in filtered_cars if search_query.lower() in car['Make'].lower() or search_query.lower() in car['Model'].lower()]
    
    
    elif filter_type == 'make':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Make'])
    elif filter_type == 'model':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Model'])
    
    return render_template('search_results.html', cars=filtered_cars, search_query=search_query, filter_type=filter_type)

if __name__ == '__main__':
    app.run(debug=True)