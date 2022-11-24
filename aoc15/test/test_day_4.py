import unittest

import days.day4


class TestDay4(unittest.TestCase):
    def test_run_a_example_1(self):
        output = days.day4.run_a('input/4_example_1.txt')
        self.assertEqual(output, 609043)

    def test_run_a_example_2(self):
        output = days.day4.run_a('input/4_example_2.txt')
        self.assertEqual(output, 1048970)


if __name__ == '__main__':
    unittest.main()
