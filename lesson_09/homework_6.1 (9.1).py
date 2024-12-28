import unittest
from unittest.mock import patch

def count_unique_characters(sentence):
    unique_chars = set(sentence)
    return len(unique_chars)

def count_total_characters(sentence):
    return len(sentence)

sentence = input("Напишіть речення : ")
print(sentence)

symbols = count_total_characters(sentence)
print(f"Загальна кількість символів: {symbols}")
count_unique = count_unique_characters(sentence)
print(f"Є {count_unique} унікальних символів.")

class TestUniqueCharacters(unittest.TestCase):
    @patch('builtins.input', return_value="Hello World!")
    def test_unique_characters(self, mock_input):
        sentence = input("Напишіть речення : ")
        unique_chars = set(sentence)
        self.assertEqual(count_unique_characters(sentence), len(unique_chars))

    @patch('builtins.input', return_value="QA Automation Python!")
    def test_total_characters(self, mock_input):
        sentence = input("Напишіть речення : ")
        total_chars = len(sentence)
        self.assertEqual(count_total_characters(sentence), total_chars)

if __name__ == '__main__':
    unittest.main()