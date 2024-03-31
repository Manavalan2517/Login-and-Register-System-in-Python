import requests

# Define the base URL for the API
base_url = "http://localhost:8000"

# Define the API endpoint for registration
register_endpoint = "/register"

# Define the API endpoint for login
login_endpoint = "/login"

# Example usage for registration
# Replace 'username' and 'password' with your own desired values
username = "new_user"
password = "my_password"
registration_data = {"username": username, "password": password}

# Send a POST request to the registration endpoint
response = requests.post(base_url + register_endpoint, json=registration_data)

# Check the status code of the response to determine success
if response.status_code == 200:
    # Registration successful
    print("Registration successful!")
else:
    # Registration failed
    print("Registration failed. Error:", response.text)


# Example usage for login
# Replace 'username' and 'password' with your own credentials
login_data = {"username": username, "password": password}

# Send a POST request to the login endpoint
response = requests.post(base_url + login_endpoint, json=login_data)

# Check the status code of the response to determine success
if response.status_code == 200:
    # Login successful
    print("Login successful!")
else:
    # Login failed
    print("Login failed. Error:", response.text)
