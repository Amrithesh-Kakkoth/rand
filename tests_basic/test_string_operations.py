import unittest


class TestStringOperations(unittest.TestCase):
    """Test basic string operations."""
    
    def test_string_concatenation(self):
        """Test string concatenation."""
        self.assertEqual("hello" + " world", "hello world")
        self.assertEqual("" + "test", "test")
        self.assertEqual("a" + "b" + "c", "abc")
    
    def test_string_length(self):
        """Test string length calculation."""
        self.assertEqual(len("hello"), 5)
        self.assertEqual(len(""), 0)
        self.assertEqual(len("test string"), 11)
    
    def test_string_case_conversion(self):
        """Test string case conversion methods."""
        test_string = "Hello World"
        self.assertEqual(test_string.upper(), "HELLO WORLD")
        self.assertEqual(test_string.lower(), "hello world")
        self.assertEqual("hello world".title(), "Hello World")
    
    def test_string_contains(self):
        """Test string containment checks."""
        text = "The quick brown fox"
        self.assertIn("quick", text)
        self.assertIn("fox", text)
        self.assertNotIn("cat", text)
        self.assertTrue(text.startswith("The"))
        self.assertTrue(text.endswith("fox"))


if __name__ == '__main__':
    unittest.main()