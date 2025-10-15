import unittest
from Test_DemonSlayer import TestBasicFunctions

def suite():
    """
    Create a test suite combining all test cases from Test_DemonSlayer.
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load tests from your class using the loader
    suite.addTests(loader.loadTestsFromTestCase(TestBasicFunctions))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
