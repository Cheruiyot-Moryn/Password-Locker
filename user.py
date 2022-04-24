import string,random
import pyperclip


class User:
    '''
    Class that is creates and save new objects of user acccounts data
    '''
    users_list=[]
    password_list = []

    def __init__(self, firstname, lastname, account_name, password):
        '''
        Initializing the variables for the list of user data
        '''
        self.firstname=firstname
        self.lastname=lastname
        self.account_name=account_name
        self.password=password
