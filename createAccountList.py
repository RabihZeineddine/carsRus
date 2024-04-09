import re

class account:
    # user constructor creates a user with given info
    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    # set functions
    def change_username(self, username):
        self.username = username

    def change_email(self, email):
        self.email = email

    def change_password(self, password):
        self.password = password

    def change_name(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname

    # get functions
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_fullname(self):
        return self.first_name, self.last_name

    def get_firstname(self):
        return self.first_name
        
    def get_lastname(self):
        return self.last_name
        
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
    def verify_password(self, password):
        if password == self.password:
            print("Password verified successfully.")
            return True
        else:
            print("Incorrect password.")
            return False
    
    # Reset user password
    def reset_password(self, new_password):
        self.password = new_password

    # Returns user's name
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

user_list = []

def add_user():
    user_list.append(account)
