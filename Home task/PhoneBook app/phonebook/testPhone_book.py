import unittest
from phonebook.phone_book import PhoneBook


class TestPhoneBook(unittest.TestCase):

    def test_for_phone_book_setUP(self):
        phone : PhoneBook = PhoneBook("first_name", "last_name", "12345678900", "bigjohn@gmail.com")
        self.assertEqual(phone.get_first_name, "first_name")
        self.assertEqual(phone.get_last_name, "last_name")
        self.assertEqual(phone.get_phone_number, "12345678900")
        self.assertEqual(phone.get_email, "bigjohn@gmail.com")

    def test_that_setUp_is_not_empty(self):
        phone: PhoneBook = PhoneBook("first_name", "last_name", "12345678900", "bigjohn@gmail.com")
        self.assertRaises(ValueError, phone.get_first_name, " ")
        self.assertRaises(ValueError, phone.get_last_name, " ")
        self.assertRaises(ValueError, phone.get_phone_number, " ")
        self.assertRaises(ValueError, phone.get_email, " ")

