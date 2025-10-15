# Test_DemonSlayer.py

import unittest
from DemonSlayer import add, subtract

class TestBasicFunctions(unittest.TestCase):
    
    def test_add(self):
        """
        Test case to check if the add function works correctly.
        It checks the addition of positive, negative, and zero numbers.
        """
        # Test adding positive numbers
        self.assertEqual(add(2, 3), 5)  
        
        # Test adding a positive and a negative number
        self.assertEqual(add(-2, 3), 1)  
        
        # Test adding two negative numbers
        self.assertEqual(add(-2, -3), -5)
        
        # Test adding zero
        self.assertEqual(add(0, 0), 0)
        
    def test_subtract(self):
        """
        Test case to check if the subtract function works correctly.
        It checks subtraction of positive, negative, and zero numbers.
        """
        # Test subtracting positive numbers
        self.assertEqual(subtract(5, 3), 2) 
        
        # Test subtracting a negative number from a positive
        self.assertEqual(subtract(5, -3), 8)
        
        # Test subtracting two negative numbers
        self.assertEqual(subtract(-5, -3), -2)
        
        # Test subtracting from zero
        self.assertEqual(subtract(0, 5), -5)

    def test_invalid_input(self):
        """
        Test case to handle invalid input, checking if the functions 
        raise appropriate errors for non-numeric inputs.
        """
        # Test invalid input for addition
        with self.assertRaises(TypeError):
            add("a", 3)  # Should raise a TypeError
        
        # Test invalid input for subtraction
        with self.assertRaises(TypeError):
            subtract(5, "b")  # Should raise a TypeError

# Run the tests
if __name__ == "__main__":
    unittest.main()
