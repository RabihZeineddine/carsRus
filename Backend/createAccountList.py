import re

class account:
    # user constructor creates a user with given info
    def __init__(user, username, email, confirmEmail, password, first_name, last_name):
        user.username = username
        user.email = email
        user.confirmEmail= false
        user.password = password
        user.first_name = first_name
        user.last_name = last_name

    # set functions
    def change_username(user, username):
        user.username = username

    def change_email(user, email):
        user.email = email

    def confirm_Email(user, confirmation)
        user.confirmEmail = confirmation

    def change_password(user, password):
        user.password = password

    def change_name(user, firstname, lastname):
        user.first_name = firstname
        user.last_name = lastname

    # get functions
    def get_username(user):
        return user.username

    def get_email(user):
        return user.email

    def get_password(user):
        return user.password

    def get_fullname(user):
        return user.first_name, user.last_name

    def get_firstname(user):
        return user.first_name
        
    def get_lastname(user):
        return user.last_name
        
    # Verify user's email address is valid
    # Note: Will be updated later when the database and front end give a better
    # vision of what is needed to implement this function.
    def verify_email(email):
        # Valid Email register expression pattern
        pattern = '^[a-zA-Z0-9][a-zA-Z0-9.-]*@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    
        if re.search(email, pattern):
            print('Email is valid:', email)
        else:
            print('Email is invalid:', email)
        
    # Verify user's password
    def verify_password(user, password):
        if password == user.password:
            print("Password verified successfully.")
            return True
        else:
            print("Incorrect password.")
            return False
    
    # Reset user password
    def reset_password(user, new_password):
        user.password = new_password

    # Returns user's name
    def get_full_name(user):
        return f"{user.first_name} {user.last_name}"

user_list = []

def add_user():
    user_list.append(account)
