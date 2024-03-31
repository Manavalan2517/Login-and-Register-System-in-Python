import questionary
import json
from time import sleep
import bcrypt  # Or Argon2 for stronger hashing
from rich.console import Console

console = Console()

class Validate:
    def __init__(self) -> None:
        try:
            # Check JSON File Exist or not
            with open("data.json", "r+") as f1:
                pass
        except FileNotFoundError:
            # If not exist create a new one
            with open("data.json", "w") as f1:
                data = {"gamedata": {}}
                json.dump(data, f1, indent=3)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def update_json(self, username, hashed_password):
        with open("data.json", "r+") as f:
            fdata = json.load(f)
            data = {username: {"password": hashed_password.decode()}}
            fdata["gamedata"].update(data)
            f.seek(0)  # Move to the beginning of the file
            json.dump(fdata, f, indent=3)

    def validate_username(self, username):
        if len(username) == 0:
            return "Please enter a username."
        elif not username.islower():
            return "Username must contain only lowercase letters."
        else:
            with open("data.json", "r") as f:
                fdata = json.load(f)
                if username in fdata["gamedata"]:
                    return "User already exists"
                else:
                    return True

    def validate_password(self, password):
        if len(password) < 7:
            return "Password must be at least 7 characters."
        elif not any(char.isdigit() for char in password):
            return "Password must contain a number."
        elif not any(char.islower() for char in password):
            return "Password must contain a lowercase letter."
        elif not any(char.isupper() for char in password):
            return "Password must contain an uppercase letter."
        else:
            return True

    def register_user(self, username, password):
        if self.validate_username(username) and self.validate_password(password):
            hashed_password = self.hash_password(password)
            self.update_json(username, hashed_password)
            console.log("[bold green]Registration successful!")
            return True
        else:
            if not self.validate_username(username):
                console.print(f"[bold red]Username error: {self.validate_username(username)}")
            if not self.validate_password(password):
                console.print(f"[bold red]Password error: {self.validate_password(password)}")
            return False

    def login_user(self, username, password):
        username = username.lower()  # Allow case-insensitive login
        with open("data.json", "r") as f:
            fdata = json.load(f)
            if username in fdata["gamedata"]:
                hashed_password = fdata["gamedata"][username]["password"].encode()
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    console.log("[bold green]Login successful!")
                    return True
                else:
                    console.print("[bold red]Incorrect password.")
            else:
                console.print(f"[bold red]Username '{username}' not found.")
        return False

# Object
validateObj = Validate()

# Login or Register
def register():
    # Username
    username = questionary.text("Enter your Username", validate=validateObj.validate_username).ask()
    # Password
    password = questionary.password("Enter your password", validate=validateObj.validate_password).ask()

    # Registration logic
    if validateObj.register_user(username, password):
        sleep(1)
        login()

def login():
    # Username
    username = questionary.text("Enter your Username").ask()
    # Password
    password = questionary.password("Enter your password").ask()

    # Login logic
    if validateObj.login_user(username, password):
        sleep(1)
        console.log("[bold green]Welcome back!")
        # Implement actions after successful login (e.g., game menu)

# Choice to select login or register
choice = questionary.select(
  "What do you want to do?",
  choices=[
      "LOGIN",
      "REGISTER"
  ]).ask()

# Checking
if choice == "REGISTER":
  register()
if choice == "LOGIN":
  login()