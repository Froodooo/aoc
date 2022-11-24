import unittest

import day15.day_15


class TestDay15(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day15.day_15.run_a('test/15_example_1.txt')
        self.assertEqual(output, 436)

    def test_run_a_example_2(self):
        output = day15.day_15.run_a('test/15_example_2.txt')
        self.assertEqual(output, 1)

    def test_run_a_example_3(self):
        output = day15.day_15.run_a('test/15_example_3.txt')
        self.assertEqual(output, 10)

    def test_run_a_example_4(self):
        output = day15.day_15.run_a('test/15_example_4.txt')
        self.assertEqual(output, 27)

    def test_run_a_example_5(self):
        output = day15.day_15.run_a('test/15_example_5.txt')
        self.assertEqual(output, 78)

    def test_run_a_example_6(self):
        output = day15.day_15.run_a('test/15_example_6.txt')
        self.assertEqual(output, 438)

    def test_run_a_example_7(self):
        output = day15.day_15.run_a('test/15_example_7.txt')
        self.assertEqual(output, 1836)

    def test_run_a(self):
        output = day15.day_15.run_a('day15/15.txt')
        self.assertEqual(output, 403)


if __name__ == '__main__':
    unittest.main()
