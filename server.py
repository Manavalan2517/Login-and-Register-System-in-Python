import uvicorn
import bcrypt
import json
import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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
                return username not in fdata["gamedata"]

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
            return True
        else:
            return False

    def login_user(self, username, password):
        username = username.lower()  # Allow case-insensitive login
        with open("data.json", "r") as f:
            fdata = json.load(f)
            if username in fdata["gamedata"]:
                hashed_password = fdata["gamedata"][username]["password"].encode()
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    return True
            return False

    def delete_account(self, username):
        with open("data.json", "r+") as f:
            fdata = json.load(f)
            if username in fdata["gamedata"]:
                del fdata["gamedata"][username]
                f.seek(0)
                json.dump(fdata, f, indent=3)
                return True
            return False

# Define request body models
class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str

class LoginRequest(BaseModel):
    username: str
    password: str

class DeleteAccountRequest(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(request: RegisterRequest):
    username = request.username
    password = request.password
    email = request.email
    validate_obj = Validate()
    if validate_obj.validate_username(username) and validate_obj.validate_password(password) and validate_obj.validate_email(email):
        hashed_password = validate_obj.hash_password(password)
        validate_obj.update_json(username, hashed_password, email)
        return {"message": "Registration successful!"}
    else:
        error_message = ""
        if not validate_obj.validate_username(username):
            error_message += f"Username error: {validate_obj.validate_username(username)}"
        if not validate_obj.validate_password(password):
            error_message += f" Password error: {validate_obj.validate_password(password)}"
        if not validate_obj.validate_email(email):
            error_message += f" Email error: {validate_obj.validate_email(email)}"
        raise HTTPException(status_code=400, detail=error_message)

@app.post("/login")
def login(request: LoginRequest):
    username = request.username.lower()
    password = request.password
    validate_obj = Validate()
    if validate_obj.login_user(username, password):
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password.")

@app.delete("/delete_account")
def delete_account(request: DeleteAccountRequest):
    username = request.username.lower()
    password = request.password
    validate_obj = Validate()
    if validate_obj.login_user(username, password):
        if validate_obj.delete_account(username):
            return {"message": "Account deleted successfully!"}
        else:
            raise HTTPException(status_code=500, detail="Failed to delete account.")
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password.")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
