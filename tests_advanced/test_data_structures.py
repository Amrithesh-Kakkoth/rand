import unittest


class TestDataStructures(unittest.TestCase):
    """Test operations on various data structures."""
    
    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3, 4, 5]
        
        # Test append
        test_list.append(6)
        self.assertEqual(test_list[-1], 6)
        
        # Test remove
        test_list.remove(3)
        self.assertNotIn(3, test_list)
        
        # Test list comprehension
        squared = [x**2 for x in [1, 2, 3, 4]]
        self.assertEqual(squared, [1, 4, 9, 16])
    
    def test_dictionary_operations(self):
        """Test dictionary operations."""
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        
        # Test key access
        self.assertEqual(test_dict['a'], 1)
        
        # Test key addition
        test_dict['d'] = 4
        self.assertIn('d', test_dict)
        self.assertEqual(test_dict['d'], 4)
        
        # Test keys and values
        self.assertEqual(len(test_dict.keys()), 4)
        self.assertIn(2, test_dict.values())
    
    def test_set_operations(self):
        """Test set operations."""
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        
        # Test union
        union_result = set1.union(set2)
        expected_union = {1, 2, 3, 4, 5, 6}
        self.assertEqual(union_result, expected_union)
        
        # Test intersection
        intersection_result = set1.intersection(set2)
        expected_intersection = {3, 4}
        self.assertEqual(intersection_result, expected_intersection)
        
        # Test difference
        diff_result = set1.difference(set2)
        expected_diff = {1, 2}
        self.assertEqual(diff_result, expected_diff)


if __name__ == '__main__':
    unittest.main()