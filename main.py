import questionary
import json
from time import sleep
import bcrypt
import re
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

    def update_json(self, username, hashed_password, email):
        with open("data.json", "r+") as f:
            fdata = json.load(f)
            data = {username: {"password": hashed_password.decode(), "email": email}}
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

    def validate_email(self, email):
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, email):
            return "Please enter a valid email address."
        else:
            return True

    def register_user(self, username, password, email):
        if self.validate_username(username) and self.validate_password(password) and self.validate_email(email):
            hashed_password = self.hash_password(password)
            self.update_json(username, hashed_password, email)
            console.log("[bold green]Registration successful!")
            return True
        else:
            if not self.validate_username(username):
                console.print(f"[bold red]Username error: {self.validate_username(username)}")
            if not self.validate_password(password):
                console.print(f"[bold red]Password error: {self.validate_password(password)}")
            if not self.validate_email(email):
                console.print(f"[bold red]Email error: {self.validate_email(email)}")
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

    def delete_account(self, username):
        with open("data.json", "r+") as f:
            fdata = json.load(f)
            if username in fdata["gamedata"]:
                del fdata["gamedata"][username]
                f.seek(0)
                json.dump(fdata, f, indent=3)
                console.log("[bold green]Account deleted successfully!")
                return True
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
    # Email
    email = questionary.text("Enter your Email", validate=validateObj.validate_email).ask()

    # Registration logic
    if validateObj.register_user(username, password, email):
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


def delete_account():
    # Username
    username = questionary.text("Enter your Username").ask()
    # Password
    password = questionary.password("Enter your password").ask()

    # Delete account logic
    if validateObj.login_user(username, password):
        if validateObj.delete_account(username):
            console.log("[bold green]Account deleted successfully!")
        else:
            console.print("[bold red]Failed to delete account.")


# Choice to select login or register or delete account
choice = questionary.select(
    "What do you want to do?",
    choices=[
        "LOGIN",
        "REGISTER",
        "DELETE ACCOUNT"
    ]).ask()

# Checking
if choice == "REGISTER":
    register()
elif choice == "LOGIN":
    login()
elif choice == "DELETE ACCOUNT":
    delete_account()