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
