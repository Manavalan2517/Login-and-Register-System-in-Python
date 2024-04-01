import requests


class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        self.register_endpoint = "/register"
        self.login_endpoint = "/login"
        self.delete_account_endpoint = "/delete_account"

    def register(self, username, password, email):
        registration_data = {"username": username, "password": password, "email": email}
        response = requests.post(self.base_url + self.register_endpoint, json=registration_data)
        if response.status_code == 200:
            print("Registration successful!")
        else:
            print("Registration failed. Error:", response.text)

    def login(self, username, password):
        login_data = {"username": username, "password": password}
        response = requests.post(self.base_url + self.login_endpoint, json=login_data)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Login failed. Error:", response.text)

    def delete_account(self, username, password):
        delete_account_data = {"username": username, "password": password}
        response = requests.delete(self.base_url + self.delete_account_endpoint, json=delete_account_data)
        if response.status_code == 200:
            print("Account deletion successful!")
        else:
            print("Account deletion failed. Error:", response.text)


# Usage
user = Client("http://localhost:8000")
user.register("new_user", "my_password", "new_user@example.com")
user.login("new_user", "my_password")
user.delete_account("new_user", "my_password")
