class account:
    def __init__(user, email, password, first_name, last_name):
        user.email = email
        user.password = password
        user.first_name = first_name
        user.last_name = last_name

    def get_full_name(user):
        return f"{user.first_name} {user.last_name}"

    def reset_password(user, new_password):
        user.password = new_password

def createAccount(email, password, firstname, lastname):
    user = {
        "email": email,
        "password": password,
        "firstname": firstname,
        "lastname": lastname
    }
    return user

user_list = []

def add_user()
    user_list.append(account)
