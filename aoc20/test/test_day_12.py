import unittest

import day12.day_12


class TestDay12(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day12.day_12.run_a('test/12_example_1.txt')
        self.assertEqual(output, 25)

    def test_run_a(self):
        output = day12.day_12.run_a('day12/12.txt')
        self.assertEqual(output, 1710)

    def test_run_b_example_1(self):
        output = day12.day_12.run_b('test/12_example_1.txt')
        self.assertEqual(output, 286)

    def test_run_b(self):
        output = day12.day_12.run_b('day12/12.txt')
        self.assertEqual(output, 62045)


if __name__ == '__main__':
    unittest.main()
