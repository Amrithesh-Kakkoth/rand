import unittest


class TestAlgorithms(unittest.TestCase):
    """Test various algorithm implementations."""
    
    def test_sorting_algorithms(self):
        """Test sorting functionality."""
        unsorted_list = [64, 34, 25, 12, 22, 11, 90]
        expected_sorted = [11, 12, 22, 25, 34, 64, 90]
        
        # Test built-in sort
        test_list = unsorted_list.copy()
        test_list.sort()
        self.assertEqual(test_list, expected_sorted)
        
        # Test sorted function
        sorted_result = sorted(unsorted_list)
        self.assertEqual(sorted_result, expected_sorted)
    
    def test_search_algorithms(self):
        """Test search functionality."""
        test_list = [1, 3, 5, 7, 9, 11, 13, 15]
        
        # Test linear search concept
        target = 7
        found_index = test_list.index(target) if target in test_list else -1
        self.assertEqual(found_index, 3)
        
        # Test element not found
        target_not_found = 8
        is_found = target_not_found in test_list
        self.assertFalse(is_found)
    
    def test_fibonacci_sequence(self):
        """Test Fibonacci sequence generation."""
        def fibonacci(n):
            """Generate Fibonacci sequence up to n terms."""
            if n <= 0:
                return []
            elif n == 1:
                return [0]
            elif n == 2:
                return [0, 1]
            else:
                fib = [0, 1]
                for i in range(2, n):
                    fib.append(fib[i-1] + fib[i-2])
                return fib
        
        # Test various Fibonacci sequences
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
    
    def test_factorial_calculation(self):
        """Test factorial calculation."""
        def factorial(n):
            """Calculate factorial of n."""
            if n < 0:
                raise ValueError("Factorial not defined for negative numbers")
            if n == 0 or n == 1:
                return 1
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        
        # Test factorial calculations
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        
        # Test negative input
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == '__main__':
    unittest.main()