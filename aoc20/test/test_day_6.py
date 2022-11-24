import unittest

from day6.day_6 import Day6


class TestDay6(unittest.TestCase):
    def setUp(self):
        self.day = Day6()

    def test_run_a_example_1(self):
        output = self.day.run_a('test/6_example_1.txt')
        self.assertEqual(output, 11)

    def test_run_b_example_1(self):
        output = self.day.run_b('test/6_example_1.txt')
        self.assertEqual(output, 6)

    def test_run_a(self):
        output = self.day.run_a('day6/6.txt')
        self.assertEqual(output, 6387)

    def test_run_b(self):
        output = self.day.run_b('day6/6.txt')
        self.assertEqual(output, 3039)


if __name__ == '__main__':
    unittest.main()
