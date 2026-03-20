import unittest
from calculator import Add

class TestCalculator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""),0)
    def test_one(self):
        self.assertEqual(Add("1"), 1)
    def test_two(self):
        self.assertEqual(Add("1,2"), 3)
    def test_multi(self):
        self.assertEqual(Add("1,2,3,12,1"), 19)
    def test_value(self):
        with self.assertRaises(ValueError):
            Add("1,a,2,3")
    def test_nowa_linia(self):
        self.assertEqual(Add("1\n2,3"),6)
    def test_nie(self):
        with self.assertRaises(ValueError):
            Add("1,\n")


if __name__ == '__main__':
    unittest.main()
