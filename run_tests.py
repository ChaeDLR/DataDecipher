import data_decipher
from tests import DataProcessTests
import unittest

if __name__ == "__main__":
    data_tests = DataProcessTests()
    suite = unittest.TestSuite()
    tests = unittest.TestLoader()
    suite.addTests(tests.loadTestsFromTestCase(DataProcessTests))
    unittest.TextTestRunner().run(suite)
