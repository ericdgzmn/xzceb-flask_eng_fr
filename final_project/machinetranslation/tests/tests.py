import unittest
from translator import english_to_french, french_to_english

class Testtranslator(unittest.TestCase):
        def test1(self):
            self.assertEqual(english_to_french('hello'), 'Bonjour') #test for hello/bonjour
            self.assertEqual(english_to_french(' '), ' ') #test for null input

        def test2(self):
            self.assertEqual(french_to_english('bonjour'), 'Hello') #test for bonjour/hello
            self.assertEqual(french_to_english(' '), ' ') #test for null input

#if__name__=='__main__':
unittest.main()
