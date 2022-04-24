class Credential:

    credential_list=[]

    '''
    class that generates new instances of credentials
    '''
    def __init__(self, identity, user_name, password):
        '''
        Initializing the variables for the list of credentials
        '''
        self.identity=identity
        self.user_name=user_name
        self.password=password
    
    def save_credential(self):
        '''
        Function to create  and save log in credentials for users
        '''
        Credential.credential_list.append(self)