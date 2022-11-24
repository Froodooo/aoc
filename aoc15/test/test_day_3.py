import unittest

import days.day3


class TestDay3(unittest.TestCase):
    def test_run_a_example_1(self):
        output = days.day3.run_a('input/3_example_1.txt')
        self.assertEqual(output, 2)

    def test_run_a_example_2(self):
        output = days.day3.run_a('input/3_example_2.txt')
        self.assertEqual(output, 4)

    def test_run_a(self):
        output = days.day3.run_a('input/3.txt')
        self.assertEqual(output, 2565)

    def test_run_b_example_1(self):
        output = days.day3.run_b('input/3_example_2.txt')
        self.assertEqual(output, 3)

    def test_run_b_example_3(self):
        output = days.day3.run_b('input/3_example_3.txt')
        self.assertEqual(output, 11)

    def test_run_b(self):
        output = days.day3.run_b('input/3.txt')
        self.assertEqual(output, 2639)


if __name__ == '__main__':
    unittest.main()
