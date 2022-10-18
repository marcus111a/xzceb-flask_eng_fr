import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_null_etof(self):
        self.assertNotEqual(english_to_french('None'), '   ')
    def test_null_ftoe(self):
        self.assertNotEqual(french_to_english('None'), '   ')
    def test_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ =='__main__':
    unittest.main()