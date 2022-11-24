import unittest

import day22.day_22


class TestDay22(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day22.day_22.run_a('test/22_example_1.txt')
        self.assertEqual(output, 306)

    def test_run_a(self):
        output = day22.day_22.run_a('day22/22.txt')
        self.assertEqual(output, 35818)

    def test_run_b_example_1(self):
        output = day22.day_22.run_b('test/22_example_1.txt')
        self.assertEqual(output, 291)


if __name__ == '__main__':
    unittest.main()
