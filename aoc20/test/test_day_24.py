import unittest

import day24.day_24


class TestDay24(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day24.day_24.run_a('test/24_example_1.txt')
        self.assertEqual(output, 10)

    def test_run_b_example_1(self):
        output = day24.day_24.run_b('test/24_example_1.txt')
        self.assertEqual(output, 2208)


if __name__ == '__main__':
    unittest.main()
