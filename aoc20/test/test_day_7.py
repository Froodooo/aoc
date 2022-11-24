import unittest

import day7.day_7


class TestDay7(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day7.day_7.run_a('test/7_example_1.txt')
        self.assertEqual(output, 4)

    def test_run_b_example_1(self):
        output = day7.day_7.run_b('test/7_example_1.txt')
        self.assertEqual(output, 32)

    def test_run_b_example_2(self):
        output = day7.day_7.run_b('test/7_example_2.txt')
        self.assertEqual(output, 126)


if __name__ == '__main__':
    unittest.main()
