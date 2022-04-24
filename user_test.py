from collections import UserString
from os import uname_result
import unittest
from user import User

class Testuser(unittest.TestCase):

 def setUp(self):

        self.new_user = User("Moureen","Cheruiyot","8005")

def test_init(self):

    self.assertEqual(self.new_user.user_name,"Moureen")

    self.assertEqual(self.new_user.password,"8005")

def test_save_user(self):

    self.new_contact.save_contact()
    test_user = User("Test","user","0729321741","test@user.com")
    test_user.save_user()

    self.new_user.delete_user()
    self.assertEqual(len(UserString.user_list,1))
    
if uname_result =='main':
    unittest.main()        