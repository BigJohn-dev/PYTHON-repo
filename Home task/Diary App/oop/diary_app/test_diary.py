import unittest
from oop.diary_app.Diary import Diary

class MyTestCase(unittest.TestCase):

    def test_that_diary_isLocked(self):
        diary : Diary = Diary("username", "password", "bigJohn@gmail.com")
        self.assertTrue(diary.is_locked())

    def test_that_diary_isUnlocked(self):
        diary : Diary= Diary("username", "password", "bigJohn@gmail.com")
        diary.is_locked()
        self.assertFalse(diary.unlock("password"))

    def test_not_to_unlock_with_wrong_password(self):
        diary : Diary= Diary("username", "password", "bigJohn@gmail.com")
        diary.is_locked()
        self.assertRaises(ValueError, diary.unlock, "wrong_password")

    def test_to_add_entry(self):
        diary : Diary= Diary("username", "password", "bigJohn@gmail.com")
        diary.unlock("password")
        diary.add_entry()