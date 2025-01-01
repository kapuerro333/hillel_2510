import unittest

def count_unique_characters(message):
    if 'h' in message.lower():
        return "Found the letter 'h' or 'H'."
    else:
        return "No 'h' or 'H' in your message. Try again."

class TestUniqueCharacters(unittest.TestCase):
    def test_message_contains_h(self):
        message = "Hello"
        result = count_unique_characters(message)
        self.assertEqual(result, "Found the letter 'h' or 'H'.")

    def test_message_does_not_contain_h(self):
        message = "World"
        result = count_unique_characters(message)
        self.assertEqual(result, "No 'h' or 'H' in your message. Try again.")

    def test_message_all_uppercase_h(self):
        message = "HELLO"
        result = count_unique_characters(message)
        self.assertEqual(result, "Found the letter 'h' or 'H'.")

    def test_message_with_multiple_h(self):
        message = "Hahaha"
        result = count_unique_characters(message)
        self.assertEqual(result, "Found the letter 'h' or 'H'.")

    def test_edge_case_empty(self):
        message = ""
        result = count_unique_characters(message)
        self.assertEqual(result, "No 'h' or 'H' in your message. Try again.")

if __name__ == '__main__':
    unittest.main()