import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    # Tests for englishToFrench method
    def test_englishToFrench_null_input(self):
        self.assertIsNone(english_to_french(None))

    def test_englishToFrench_hello_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    # Tests for frenchToEnglish method
    def test_frenchToEnglish_null_input(self):
        self.assertIsNone(french_to_english(None))

    def test_frenchToEnglish_bonjour_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
