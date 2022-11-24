import unittest

import days.day5


class TestDay4(unittest.TestCase):
    def test_run_a_example_1(self):
        output = days.day5.run_a('input/5_example_1.txt')
        self.assertEqual(output, 2)

    def test_run_b_example_2(self):
        output = days.day5.run_b('input/5_example_2.txt')
        self.assertEqual(output, 2)


if __name__ == '__main__':
    unittest.main()
