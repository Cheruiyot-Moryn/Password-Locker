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
