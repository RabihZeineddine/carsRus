def createAccount(email, password, firstname, lastname):
    user = {
        "email": email,
        "password": password,
        "firstname": firstname,
        "lastname": lastname
    }
    return user
    
class Account:
    def __init__(user, email, password, first_name, last_name):
        user.email = email
        user.password = password
        user.first_name = first_name
        user.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def reset_password(self, new_password):
        self.password = new_password
