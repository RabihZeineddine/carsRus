# Possibly unit test library
import unittest
import createAccountList as acc

class testAccountList(unittest.TestCase):
    def testConstructor(self):
        account = acc.account("JohnDoe1", "johndoe@gmail.com", "password", "John", "Doe")
        self.assertEqual(account.get_username(), "JohnDoe1")
        self.assertEqual(account.get_email(), "johndoe@gmail.com")
        self.assertEqual(account.get_password(), "password")
        self.assertEqual(account.get_username(), "John")
        self.assertEqual(account.get_username(), "Doe")

    def testSetters(self):
        account = acc.account("JohnDoe1", "johndoe@gmail.com", "password", "John", "Doe")
        account.change_email("janedoe@gmail.com")
        account.change_username("JaneDoe")
        account.change_password("pass1")
        account.change_name("Jane", "Doe")        
        self.assertEqual(account.get_username(), "JaneDoe")
        self.assertEqual(account.get_email(), "janedoe@gmail.com")
        self.assertEqual(account.get_password(), "pass1")
        self.assertEqual(account.get_username(), "Jane")
        self.assertEqual(account.get_username(), "Doe")
