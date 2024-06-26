from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from car_data import cars
from email.mime.text import MIMEText
import json, random, string, atexit, smtplib, time

# flask stuff
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# render home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get email and password entered by user
        email = request.form['email']
        password = request.form['password']
        
        # load users from user.json
        users = load_users()
        # finds user with matching email and password
        user = next((user for user in users if user['Email'] == email and user['Password'] == password), None)
        
        # checks session data against user input fields
        if user:
            session['user'] = user
            return redirect(url_for('index'))
        # error if no matching user found
        else:
            return "Invalid email or password. Please redirect back and try again."
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # removes user from session
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # gets user account signup information
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # check if passwords match
        if password != confirm_password:
            return "Passwords do not match. Please try again." 
        
        # creates new user object
        new_user = {
            "isAdmin": False,
            "Email": email,
            "Password": password,
            "FirstName": first_name,
            "LastName": last_name
        }
        
        # add new user to list
        users = load_users()
        users.append(new_user)
        save_users(users)
        
        # then render the login screen after account creation
        return redirect(url_for('login'))
    
    # render signup screen
    return render_template('signup.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # get email from form and load user data
        email = request.form.get('email')
        users = load_users()

        # find user with provided email
        user = next((user for user in users if user['Email'] == email), None)

        #if user found re-render with reset password prompt
        if user:
            return render_template('forgot-password.html', email=email)
        else:
            return "Email not found. Please redirect back."
    # render for GET requests
    return render_template('forgot-password.html')

@app.route('/reset-password', methods=['POST'])
def reset_password():
    # get email, password, and password confirmation from forms
    email = request.form.get('email')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    
    # compare new password and password confirmation
    if new_password != confirm_password:
        return "Passwords do not match. Please Redirect Back"
    
    # load user data, find the user with provided email
    users = load_users() 
    user = next((user for user in users if user['Email'] == email), None)

    # if user found, update password and save user data
    if user:
        user['Password'] = new_password
        save_users(users)  # save the updated user data
        return "Password has been reset successfully.Redirect back to the main page."
    else:
        return "User not found. Please Redirect back."
    

@app.route('/search-results')
def search_results():
    # get search query, filter type, and page number requests
    search_query = request.args.get('query', '')
    filter_type = request.args.get('filter', '')
    page = request.args.get('page', 1, type=int)
    
    #initialize filtered car list with all cars
    filtered_cars = cars
    
    # apply filters based on search query/filter type
    if search_query:
        # filter cars by year range
        if filter_type == 'year':
            try:
                start_year, end_year = map(int, search_query.split(','))
                if start_year > end_year:
                    temp = start_year
                    start_year = end_year
                    end_year = temp
                filtered_cars = [car for car in filtered_cars if start_year <= car['Year'] <= end_year]
                filtered_cars = sorted(filtered_cars, key=lambda car: car['Year'])  # Sort by year
            except (ValueError, TypeError):
                pass
        # filter cars by max price
        elif filter_type == 'price':
            try:
                max_price = float(search_query)
                filtered_cars = [car for car in filtered_cars if float(car['Price']) <= max_price]
                filtered_cars = sorted(filtered_cars, key=lambda car: car['Price'], reverse=True)
            except ValueError:
                pass
        # filter cars by max mileage
        elif filter_type == 'mileage':
            try:
                max_mileage = float(search_query)
                filtered_cars = [car for car in filtered_cars if float(car['Mileage']) <= max_mileage]
                filtered_cars = sorted(filtered_cars, key=lambda car: car['Mileage'], reverse=True)
            except ValueError:
                pass
        # filter cars by type
        elif filter_type == 'type':
            filtered_cars = [car for car in filtered_cars if search_query.lower() in car['Type'].lower()]
        else:
            filtered_cars = [car for car in filtered_cars if search_query.lower() in car['Make'].lower() or search_query.lower() in car['Model'].lower()]

    # sort cars by make or model if no search query provided
    elif filter_type == 'make':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Make'])
    elif filter_type == 'model':
        filtered_cars = sorted(filtered_cars, key=lambda car: car['Model'])
    
    # pagination logic
    cars_per_page = 10
    total_pages = (len(filtered_cars) + cars_per_page - 1) // cars_per_page
    
    start_index = (page - 1) * cars_per_page
    end_index = start_index + cars_per_page
    paginated_cars = filtered_cars[start_index:end_index]
    
    # render search results template with filtered and paged cars
    return render_template('search_results.html', cars=paginated_cars, search_query=search_query,
                           filter_type=filter_type, page=page, total_pages=total_pages)

@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    if request.method == 'POST':
        # get the VIN of the car to add to favorites from the form data
        vin = request.form.get('vin')
        if vin:
            # Check if the car with the same VIN is already in favorites
                with open('favorites.json', 'r') as file:
                    favorites = json.load(file)
                    for car in favorites:
                        if car['VIN'] == vin:
                            # Car with the same VIN already exists, no need to add
                            return redirect(url_for('favorites'))
                
                # If car with VIN not found in favorites, add it
                for car in cars:
                    if car['VIN'] == vin:
                        with open('favorites.json', 'r+') as file:
                            favorites.append(car)
                            file.seek(0)
                            json.dump(favorites, file, indent=4)
                            file.truncate()
                        break
    
    # load favorites from the JSON file
    with open('favorites.json', 'r') as file:
        favorites = json.load(file)
    
    # render loaded favorites page
    return render_template('favorites.html', favorites=favorites) 

@app.route('/clear-favorites', methods=['POST'])
def clear_favorites():
    # clear the favorites by overwriting the favorites.json file with an empty array
    with open('favorites.json', 'w') as file:
        json.dump([], file)
        return redirect(url_for('favorites'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # get the VIN of the car from the form data
        vin = request.form.get('vin')
        # find the car with the matching VIN
        car = next((car for car in cars if car['VIN'] == vin), None)
        if car:
            # Render the checkout template with the selected car
            return render_template('checkout.html', car=car)
    # if no car is selected or request is GET, redirect to the search results page
    return redirect(url_for('search_results'))

@app.route('/process-checkout', methods=['POST'])
def process_checkout():
    # get the form data from the checkout form
    vin = request.form.get('vin')
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')

    # Store purchased car in session before redirecting to next page
    purchased_car = next((car for car in cars if car['VIN'] == vin), None)
    session['purchased_car'] = purchased_car

    # Generate a random confirmation number
    confirmation_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    session['confirmation_number'] = confirmation_number

    # Send purchase confirmation email
    send_confirmation_email(email, confirmation_number)
    
    # Process the checkout data, then redirect to the thank you screen
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    # get purchased car in session
    car = session.get('purchased_car') 
    # get confirmation number
    confirmation_number = session.get('confirmation_number') 
    # render thank you page with purchased car and confirmation number
    return render_template('thank_you.html', car=car, confirmation_number=confirmation_number)

def clear_json_on_exit():
    # Clear the favorites.json file when the server exits
    with open('favorites.json', 'w') as file:
        json.dump([], file)

# function to send confirmation email to customer, should be called upon pressing 'place order'
def send_confirmation_email(recipient, confirmation_number):
    # main email message
    msg = MIMEText(f"Dear Customer,\n\nThank you for your purchase. Your confirmation number is: #{confirmation_number}\n\nWe hope you enjoy your new ride\n\nBest wishes,\n\nThe Cars-R-Us Team")
    # subject
    msg['Subject'] = "Cars-R-Us Purchase Confirmation"
    # sender's email address (cars r us)
    sender = 'CarsRUsBot@zohomail.com'
    msg['From'] = sender
    # set the receipient's email address
    msg['To'] = recipient
    # create SMTP SSL/TLS connection to zoho mail server
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    # login to the sender's email account
    server.login(sender, 'pg7g p0e6 wzm7')
    # send the email
    server.sendmail(sender, recipient, msg.as_string())
    # close the smtp connection
    server.quit()
    # print a message to confirm that the email was sent
    print("Email sent to " + recipient)

# function to load in list of users from users.json
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# function to append new user to users.json
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

# Register the clear_json_on_exit function to be called on server exit
atexit.register(clear_json_on_exit)

if __name__ == '__main__':
    app.run(debug=True)