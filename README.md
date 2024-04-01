# Authentication System in Python

![Thumbnail](https://github.com/Manavalan2517/Real-Time-Authentication-System-in-Python/blob/main/Samples/Real%20Time%20Authentication%20System%20in%20Python.jpg)

## This project is just a basic method of securing users data

This project provides a comprehensive user authentication and management system, consisting of three main Python files: `main.py`, `server.py`, and `client.py`. The system supports user registration, login, and account deletion, while ensuring secure password storage using bcrypt hashing. Additionally, the project includes a JSON file (`data.json`) to store user data.

## File Descriptions

1. `main.py`: A command-line interface (CLI) application that allows users to register, log in, and delete their accounts. The application uses the `questionary` library to create interactive prompts and the `bcrypt` library to securely hash and verify passwords.
2. `server.py`: A FastAPI-based server that exposes RESTful endpoints for user registration, login, and account deletion. The server also utilizes `bcrypt` for password hashing and verification, and stores user data in a JSON file.
3. `client.py`: A client application that interacts with the FastAPI server using the `requests` library. The client demonstrates how to register, log in, and delete user accounts by sending HTTP requests to the server's endpoints.

## Features

- User registration with password validation (minimum length, uppercase, lowercase, and numeric character requirements) and email validation.
- Secure password storage using bcrypt hashing.
- User login with case-insensitive username support.
- Account deletion for registered users.
- JSON-based data storage for user information.

## Requirements

- Python 3.6 or newer
- `uvicorn` (for running the FastAPI server)
- `fastapi`
- `bcrypt`
- `questionary` (for the CLI application)
- `requests` (for the client application)

## Getting Started

1. Install the required packages:
```bash
pip install uvicorn fastapi bcrypt questionary requests
```
2. Run the FastAPI server:
```bash
python server.py
```
The server will start listening on `http://localhost:8000`.

3. Use the CLI application (`main.py`) to use auth locally and the client (`client.py`) to interact with the server.

## Notes

- The CLI application (`main.py`) can be run independently of the server and uses its own instance of the JSON data file.
- The client application (`client.py`) communicates with the server (`server.py`) and shares the same JSON data file as the server.