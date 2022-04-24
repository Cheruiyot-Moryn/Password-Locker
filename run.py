from ast import If
import string,random,time
from unittest.mock import _NameArgsKwargs
from httplib2 import Credentials
import pyperclip
from credential import Credential
from user import User

def create_credential(identity, user_name, password):

    new_cred = Credential(identity, user_name,password)
    return new_cred

def save_credential(credential):
    '''
    Function that saves user credentials
    '''
    credential.save_credential()

def authenticate(name,password):
    '''
    Function that authenticates for signing in
    '''
    return Credential.authenticate_credential(name,password)

def create_data(firstname, lastname, account_name, password):
    
    new_user = User(firstname, lastname, account_name, password)
    return new_user

def save_account(data):
  
    data.save_account()

def generate_password(length):
    
    return User.password_generator(length)

def cred_data_exists(number):
    
    return Credential.cred_data_exists(number)

def data_exists(number):
    
    return User.data_exists(number)

def display_data(user_number,data_number):
    
    return User.display_data(user_number,data_number)

def account_exist(name):
    
    return User.account_exist(name)

def copy_password(number,count):
    User.copy_password(number,count)

def main():
    while True:
        print("Welcome to password locker write LG or SU to start")
        print("LG -or- SU")
        option=input()
        if option == "SU":
              print ("Create Account")
              print("-"*10)
              
              print("Enter your first name ...")
              firstname=input()
              print("Enter your last name ...")
              lastname=input()
              print("Enter your username ...")
              username=input()
              print("Enter your password ...")
              userpassword=input()
              save_credential(create_credential(firstname,lastname,userpassword))
              print("Your account was created successfully. Here are the details")
              print("-"*10)
              print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
              print ("\nUse Login to your account with your details")
              print("\n \n")

        elif option =="LG":
              print(" your username..")
              loginUsername=input()
              print(" your password..")
              loginpassword=input()
              if find_user(loginPassword):
                  print("\n")
                  print("you can create multiple accounts or also view them")
                  print(","*80)
                  print("AC -or- VC")
                  choose= input()
                  print("\n")
                  if choose == "AC":
                      print("Generate password or create new password?")
                      decision=input()
                      if decision=="G":
                          characters=string.ascii_letters + string.digits
                          accountpassword="".join(random.choices(characters)for x in range(random.randint(6,16)))
                          print(f"Password:{accountpassword}")
                      elif decision=="C":
                          print("Enter password")
                          accountpassword=input()
                      else:
                          print("please put in a valid choice")
                          save_account(create_account(user,username,accountpassword))
                          print("\n")
                          print(f"Username:{username} \nAccountname;{username} \npassword:{accountpassword}")
        elif choose == "VC":
                      if find_user(username):
                          print("Here is a list of your created accounts: ")
                          print("-"*30)
                          for user in display_user():
                              print(f"account: {user.accountname} \npassword: {user.accountpassword} \n\n")
                          else: 
                          print("Invalid Credentials")
            else: 
                      print("Try again")
                      print("\n")
        else:
                  print("Incorrect try again")
                  print("\n")
    else:
                  print("Choose a valid option")
                  print("\n")
if _NameArgsKwargs == '_main_':
    main()
