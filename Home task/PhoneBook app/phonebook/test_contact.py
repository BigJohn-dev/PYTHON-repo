import unittest
from contact import Contact



class Testcontact(unittest.TestCase):

    def test_for_phone_book_setUP(self):
        self.contact = Contact("John", "Doe", "12345678900","bigjohn@gmail.com")
        self.assertEqual(self.contact.first_name, "John")
        self.assertEqual(self.contact.last_name, "Doe")
        self.assertEqual(self.contact.phone_number, "12345678900")
        self.assertEqual(self.contact.email, "bigjohn@gmail.com")

    def test_that_first_name_setUp_is_not_empty(self):
        with self.assertRaises(ValueError):
           Contact(" ", "Doe", "12345678900", "bigjohn@gmail.com")

if __name__ == '__main__':
    unittest.main()
