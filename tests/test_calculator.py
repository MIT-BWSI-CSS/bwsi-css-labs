import unittest
from labs.lab_1.lab_1b import simple_calculator

class TestSanitize(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(simple_calculator("abc"), 0)  # expecting 0 for bad input

if __name__ == "__main__":
    unittest.main()
