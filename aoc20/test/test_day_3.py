import unittest

from day3.day_3 import Day3


class TestDay3(unittest.TestCase):
    def setUp(self):
        self.day = Day3()

    def test_run_a(self):
        output = self.day.run_a('test/3_example_1.txt')
        self.assertEqual(output, 7)
    
    def test_run_b(self):
        output = self.day.run_b('test/3_example_1.txt')
        self.assertEqual(output, 336)


if __name__ == '__main__':
    unittest.main()
