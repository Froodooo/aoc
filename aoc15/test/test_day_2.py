import unittest

import days.day2


class TestDay2(unittest.TestCase):
    def test_run_a_example_1(self):
        output = days.day2.run_a('input/2_example_1.txt')
        self.assertEqual(output, 58)

    def test_run_a_example_2(self):
        output = days.day2.run_a('input/2_example_2.txt')
        self.assertEqual(output, 43)

    def test_run_a(self):
        output = days.day2.run_a('input/2.txt')
        self.assertEqual(output, 1588178)

    def test_run_b_example_1(self):
        output = days.day2.run_b('input/2_example_1.txt')
        self.assertEqual(output, 34)

    def test_run_b_example_2(self):
        output = days.day2.run_b('input/2_example_2.txt')
        self.assertEqual(output, 14)

    def test_run_b(self):
        output = days.day2.run_b('input/2.txt')
        self.assertEqual(output, 3783758)


if __name__ == '__main__':
    unittest.main()
