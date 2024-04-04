class account:
    # user constructor creates a user with given information
    def __init__(user, username, email, password, first_name, last_name):
        user.username = username
        user.email = email
        user.password = password
        user.first_name = first_name
        user.last_name = last_name

    # set functions
    def change_username(user, username):
        user.username = username

    def change_email(user, email):
        user.email = email

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
        
    # Verify user's email 
    #for loop to compare all emails in data base to this one
    def verify_email(user, email):
        if email == user.email:
            print("Email verified successfully.")
            return True
        else:
            print("Incorrect email.")
            return False
        
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

def add_user()
    user_list.append(account)
