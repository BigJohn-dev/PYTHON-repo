import unittest
from Account import *

class TestAccount(unittest.TestCase):
    def test_get_balance(self, account=None):
        result = account.get_balance()


if __name__ == '__main__':
    unittest.main()
