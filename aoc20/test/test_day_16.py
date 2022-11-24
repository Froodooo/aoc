import unittest

import day16.day_16


class TestDay16(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day16.day_16.run_a('test/16_example_1.txt')
        self.assertEqual(output, 71)


if __name__ == '__main__':
    unittest.main()
