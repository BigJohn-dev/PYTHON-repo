import unittest
import ce_string


class Testce_string(unittest.TestCase):

    def test_to_return_word_with_default_suffix(self):
        self.assertEqual('joyce', ce_string.new_word('joy'))

    def test_to_return_word_with_default_at_center(self):
        self.assertEqual('helceloo', ce_string.new_word('helloo'))

    def test_to_return_word_with_default_at_center_if_word_length_is_equal_after_separation(self):
        self.assertEqual('helceloo', ce_string.new_word('helloo'))

    def test_to_return_word_with_default_at_suffix_if_word_length_is_not_equal_after_separation(self):
        self.assertEqual('helloce', ce_string.new_word('hello'))

if __name__ == '__main__':
    unittest.main()
