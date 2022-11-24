import unittest

import day10.day_10


class TestDay10(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day10.day_10.run_a('test/10_example_1.txt')
        self.assertEqual(output, 35)

    def test_run_a_example_2(self):
        output = day10.day_10.run_a('test/10_example_2.txt')
        self.assertEqual(output, 220)

    def test_run_a(self):
        output = day10.day_10.run_a('day10/10.txt')
        self.assertEqual(output, 2170)

    def test_run_b_example_1(self):
        output = day10.day_10.run_b('test/10_example_1.txt')
        self.assertEqual(output, 8)

    def test_run_b_example_2(self):
        output = day10.day_10.run_b('test/10_example_2.txt')
        self.assertEqual(output, 19208)

    def test_run_b(self):
        output = day10.day_10.run_b('day10/10.txt')
        self.assertEqual(output, 24803586664192)


if __name__ == '__main__':
    unittest.main()
