import unittest

import day8.day_8


class TestDay8(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day8.day_8.run_a('test/8_example_1.txt')
        self.assertEqual(output, 5)

    def test_run_a(self):
        output = day8.day_8.run_a('day8/8.txt')
        self.assertEqual(output, 1930)
    
    def test_run_b_example_1(self):
        output = day8.day_8.run_b('test/8_example_1.txt')
        self.assertEqual(output, 8)
    
    def test_run_a(self):
        output = day8.day_8.run_b('day8/8.txt')
        self.assertEqual(output, 1688)


if __name__ == '__main__':
    unittest.main()
