import re
import questionary
import json
from time import sleep
from rich.console import Console

console = Console()

class Validate:
  def __init__(self) -> None:
    try: # Check JSON File Exist or not
      f1 = open("data.json", "r+")
    except: # If not exist Create a new one
      f1 = open("data.json", "x")
      f1.close()
      f2 = open("data.json", "w")
      data = {"gamedata" : {}}
      json.dump(data, f2, indent=3)
      f2.close()

  # Updating Json file
  def update_json(self, username, password):
    f1 = open("data.json", "r+")
    fdata = json.load(f1)
    data = {username:{"password":password}}
    fdata["gamedata"].update(data)
    f2 = open("data.json", "w")
    json.dump(fdata, f2, indent=3)
    f2.close()
    f1.close()

  # Username Register
  def username_register(self, username):
      f1 = open("data.json", "r+")
      fdata = json.load(f1)
      for i,k in fdata["gamedata"].items():
        if i == username:
          return "User Already Exists --->> Try Sign In (or) Try another Username"
      if len(username) == 0:
        return "Please enter a value"
      elif re.search("[a-z]", username[0]) is None:
        return "Username must contain only lower-case letters"
      else:
        f1.close()
        return True
      
  # Username Login
  def username_login(self, username):
      usernamelist = []
      f1 = open("data.json", "r+")
      fdata = json.load(f1)
      for i,k in fdata["gamedata"].items():
         usernamelist.append(i)
      if username not in usernamelist:
         return "The Username you entered does not match your registered Username."
      if len(username) == 0:
        return "Please enter a value"
      elif re.search("[a-z]", username[0]) is None:
        return "Username must contain only lower-case letters"
      else:
        f1.close()
        return True
      
  # Password Register
  def password_register(self, password):
    if len(password) < 7:
      return "Password must be at least 7 characters"
    elif re.search("[0-9]", password) is None:
      return "Password must contain a number"
    elif re.search("[a-z]", password) is None:
      return "Password must contain an lower-case letter"
    elif re.search("[A-Z]", password) is None:
      return "Password must contain an upper-case letter"
    else:
      return True

  # Password Login
  def password_login(self, password):
    f1 = open("data.json", "r+")
    fdata = json.load(f1)
    for i,k in fdata["gamedata"].items():
        if k["password"] != password:
          return "The password you entered does not match your registered password."
    else:
      f1.close()
      return True

# Object
validateObj = Validate()

# Login or Register
def register():
    # Username
    username = questionary.text("Enter your Username", validate = validateObj.username_register).ask() 
    # Password
    password = questionary.password("Enter your password", validate = validateObj.password_register).ask()
    # Loading
    validateObj.update_json(username, password)
    with console.status("[bold green]Loading...") as status:
      sleep(1)
      console.log("Register Successful")
      sleep(1)
    console.log("Now login to your account")
    login()

def login():
    # Username
    username = questionary.text("Enter your Username", validate = validateObj.username_login).ask()
    # Password
    password = questionary.password("Enter your password", validate = validateObj.password_login).ask()
    # Loading
    with console.status("[bold green]Loading...") as status:
      sleep(1)
      console.log("Login Successful")

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