import unittest
from Morse_code import encrypt, decrypt

import unittest

class TestMorseCode(unittest.TestCase):
    def test_encrypt(self):
        """
        Test the encrypt function with various inputs.

        Standard inputs:
        - Test with "HELLO", "WORLD", "SOS", and "123".

        Edge cases and special characters:
        - Test with empty input, multiple words, special characters not in the Morse code dictionary, and alphanumeric characters.

        Additional test cases:
        - Test with multiple words, all letters, all letters contd., and mix of uppercase, lowercase, and spaces.
        """
        # Standard inputs
        self.assertEqual(encrypt("HELLO"), '.... . .-.. .-.. ---')
        self.assertEqual(encrypt("WORLD"), '.-- --- .-. .-.. -..')
        self.assertEqual(encrypt("SOS"), '... --- ...')
        self.assertEqual(encrypt("123"), '.---- ..--- ...--')
        
        # Edge cases and special characters
        self.assertEqual(encrypt(""), "")  # Empty input
        self.assertEqual(encrypt("TEST TEST"), '- . ... -/- . ... -')  # Multiple words
        self.assertEqual(encrypt("@#$"), "")  # Special characters not in the Morse code dictionary
        self.assertEqual(encrypt("TEST123"), '- . ... - .---- ..--- ...--')  # Alphanumeric characters
        
        # Additional test cases
        self.assertEqual(encrypt("HELLO WORLD"), '.... . .-.. .-.. ---/.-- --- .-. .-.. -..')  # Multiple words
        self.assertEqual(encrypt("A B C D E F G H I J K L M"), '.-/-.../-.-./-.././..-./--./..../../.---/-.-/.-../--')  # All letters
        self.assertEqual(encrypt("N O P Q R S T U V W X Y Z"), '-./---/.--./--.-/.-./.../-/..-/...-/.--/-..-/-.--/--..')  # All letters contd.
        self.assertEqual(encrypt("TESTING Morse Code"), '- . ... - .. -. --./-- --- .-. ... ./-.-. --- -.. .')  # Mix of uppercase, lowercase, and spaces

    def test_decrypt(self):
        """
        Test the decrypt function with various inputs.

        Standard inputs:
        - Test with ".... . .-.. .-.. ---", ".-- --- .-. .-.. -..", "... --- ...", and ".---- ..--- ...--".

        Edge cases and special characters:
        - Test with empty input, multiple words, and alphanumeric characters.

        Additional test cases:
        - Test with multiple words, all letters, all letters contd., and mix of uppercase, lowercase, and spaces.
        """
        # Standard inputs
        self.assertEqual(decrypt('.... . .-.. .-.. ---'), "HELLO")
        self.assertEqual(decrypt('.-- --- .-. .-.. -..'), "WORLD")
        self.assertEqual(decrypt('... --- ...'), "SOS")
        self.assertEqual(decrypt('.---- ..--- ...--'), "123")
        
        # Edge cases and special characters
        self.assertEqual(decrypt(''), "")  # Empty input
        self.assertEqual(decrypt('- . ... - / - . ... -'), "TEST TEST")  # Multiple words
        self.assertEqual(decrypt('.---- ..--- ...--'), "123")  # Alphanumeric characters
        
        # Additional test cases
        self.assertEqual(decrypt('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'), "HELLO WORLD")  # Multiple words
        self.assertEqual(decrypt('.-/-.../-.-./-.././..-./--./..../../.---/-.-/.-../--'), "A B C D E F G H I J K L M")  # All letters
        self.assertEqual(decrypt('-./---/.--./--.-/.-./.../-/..-/...-/.--/-..-/-.--/--..'), "N O P Q R S T U V W X Y Z")  # All letters contd.
        self.assertEqual(decrypt('- . ... - .. -. --./-- --- .-. ... ./-.-. --- -.. .'), "TESTING MORSE CODE")  # Mix of uppercase, lowercase, and spaces

if __name__ == "__main__":
    unittest.main()