import unittest

import day25.day_25


class TestDay25(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day25.day_25.run_a('test/25_example_1.txt')
        self.assertEqual(output, 14897079)


if __name__ == '__main__':
    unittest.main()
