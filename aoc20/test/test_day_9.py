import unittest

import day9.day_9


class TestDay9(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day9.day_9.run_a('test/9_example_1.txt', 5)
        self.assertEqual(output, 127)

    def test_run_b_example_1(self):
        output = day9.day_9.run_b('test/9_example_1.txt', 5)
        self.assertEqual(output, 62)

    def test_run_a(self):
        output = day9.day_9.run_a('day9/9.txt', 25)
        self.assertEqual(output, 1492208709)

    def test_run_b(self):
        output = day9.day_9.run_b('day9/9.txt', 25)
        self.assertEqual(output, 238243506)


if __name__ == '__main__':
    unittest.main()
