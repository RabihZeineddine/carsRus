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

@app.route('/search_results')
def search_results():
    return render_template('search_results.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)