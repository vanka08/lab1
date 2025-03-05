import unittest
import defput

class TestStringFunctions(unittest.TestCase):

    def test_is_string(self):
        self.assertTrue(defput.is_string(""))
        self.assertFalse(defput.is_string("Python"))

    def test_reverse_string(self):
        self.assertEqual(defput.reverse_string("hello"), "olleh")
        self.assertEqual(defput.reverse_string("Python"), "nohtyP")
        self.assertEqual(defput.reverse_string("12345"), "54321")

    def test_is_palindrome(self):
        self.assertTrue(defput.is_palindrome("Тропа налево повела на порт"))
        self.assertTrue(defput.is_palindrome("race car"))
        self.assertFalse(defput.is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(defput.count_vowels("оловянный"), 4)
        self.assertEqual(defput.count_vowels("Привет, Андрей"), 4)
        self.assertEqual(defput.count_vowels("aeiou"), 5)

    def test_remove_duplicates(self):
        self.assertEqual(defput.remove_first_occurrence("hello"), "helo")
        self.assertEqual(defput.remove_first_occurrence("Python"), "Python")
        self.assertEqual(defput.remove_first_occurrence("aabbcc"), "abc")

if __name__ == '__main__':
    unittest.main()