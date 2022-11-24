import unittest

from day4.day_4 import Day4


class TestDay4(unittest.TestCase):
    def setUp(self):
        self.day = Day4()

    def test_run_a(self):
        output = self.day.run_a('test/4_example_1.txt')
        self.assertEqual(output, 2)

    def test_invalid_1(self):
        output = self.day.run_b('test/4_example_invalid_1.txt')
        self.assertEqual(output, 0)

    def test_valid_1(self):
        output = self.day.run_b('test/4_example_valid_1.txt')
        self.assertEqual(output, 4)


if __name__ == '__main__':
    unittest.main()
