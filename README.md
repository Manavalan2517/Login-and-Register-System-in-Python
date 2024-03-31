# Real-Time Authentication System in Python

![Thumbnail]()

This Python script is a comprehensive solution for managing user authentication, which includes both registration and login functionalities. It utilizes a local JSON file to store user credentials securely.

## Features

- **User Registration**: Securely register with a username and password.
- **User Login**: Log in with existing credentials.
- **Data Storage**: User data is stored in a JSON file, ensuring persistence across sessions.
- **Input Validation**: Robust validation for both usernames and passwords during registration and login.

## Modules Used

- `re`: For regular expressions, ensuring input validation.
- `questionary`: To prompt users for input in an interactive manner.
- `json`: For handling JSON file operations.
- `time`: Specifically, `sleep` for simulating processing time.
- `rich.console`: To enhance the terminal output with rich text and formatting.

## Requirements

- Python 3.x
- `re` module for regular expressions
- `questionary` module for interactive user prompts
- `json` module for handling JSON operations
- `rich` module for rich text and formatted console output
- `time` module for sleep function

## How It Works

### Validate Class

The `Validate` class is the core of the input validation and JSON file management:

- `__init__`: Checks for the existence of `data.json` and creates it if necessary, initializing with a `gamedata` object.
- `update_json`: Updates the JSON file with new user credentials.
- `username_register`: Validates new usernames during registration.
- `username_login`: Validates usernames during login.
- `password_register`: Validates new passwords during registration.
- `password_login`: Validates passwords during login.

An instance of this class, `validateObj`, is used throughout the script to perform validations.

### Registration and Login Functions

- `register()`: Manages the registration process, including user prompts and JSON file updating.
- `login()`: Manages the login process with user prompts and validation checks.

### User Interaction

Users are prompted to choose between 'LOGIN' and 'REGISTER'. The script then proceeds with the corresponding function based on the user's choice.

## Getting Started

To use this script:

1. Clone the repository.
2. Run the script in a terminal.
3. Choose 'REGISTER' to create a new account or 'LOGIN' to access an existing one.

Enjoy a seamless and secure authentication experience!