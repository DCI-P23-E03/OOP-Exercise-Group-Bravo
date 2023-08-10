class User:

    # first the constructor
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.new_password = "keynote1234"

    # instance method
    def register_user(self):
        print(f"You have registered {self.username} with password: {self.password} and email address: {self.email}")

    # instance method
    def login_user(self):
        print(f"Congratulations {self.username}!!! Your login with the password: {self.password} was successful")

    # instance method
    def change_password(self):
        print(f"Your old password: {self.password} has been changed to {self.new_password}")



user_info = User("john123", "pass123", "john@example.com")
user_info.register_user()
user_info.login_user()
user_info.change_password()