import unittest

import day18.day_18


class TestDay18(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day18.day_18.run_a('test/18_example_1.txt')
        self.assertEqual(output, 71)

    def test_run_a_example_2(self):
        output = day18.day_18.run_a('test/18_example_2.txt')
        self.assertEqual(output, 51)

    def test_run_a_example_3(self):
        output = day18.day_18.run_a('test/18_example_3.txt')
        self.assertEqual(output, 26)

    def test_run_b_example_2(self):
        output = day18.day_18.run_b('test/18_example_2.txt')
        self.assertEqual(output, 51)

    def test_run_b_example_3(self):
        output = day18.day_18.run_b('test/18_example_3.txt')
        self.assertEqual(output, 46)


if __name__ == '__main__':
    unittest.main()
