import unittest


class TestMathOperations(unittest.TestCase):
    """Test basic mathematical operations."""
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(2 + 3, 5)
        self.assertEqual(10 + (-5), 5)
        self.assertEqual(0 + 0, 0)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(10 - 3, 7)
        self.assertEqual(5 - 5, 0)
        self.assertEqual(0 - 10, -10)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(4 * 5, 20)
        self.assertEqual(3 * 0, 0)
        self.assertEqual(-2 * 3, -6)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(10 / 2, 5.0)
        self.assertEqual(9 / 3, 3.0)
        with self.assertRaises(ZeroDivisionError):
            10 / 0


if __name__ == '__main__':
    unittest.main()