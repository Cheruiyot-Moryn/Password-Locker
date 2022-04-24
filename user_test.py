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