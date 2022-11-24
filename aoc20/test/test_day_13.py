import unittest

import day13.day_13


class TestDay13(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day13.day_13.run_a('test/13_example_1.txt')
        self.assertEqual(output, 295)

    def test_run_a(self):
        output = day13.day_13.run_a('day13/13.txt')
        self.assertEqual(output, 370)

    def test_run_b_example_1(self):
        output = day13.day_13.run_b('test/13_example_1.txt')
        self.assertEqual(output, 1068781)

    def test_run_b_example_2(self):
        output = day13.day_13.run_b('test/13_example_2.txt')
        self.assertEqual(output, 3417)

    def test_run_b_example_3(self):
        output = day13.day_13.run_b('test/13_example_3.txt')
        self.assertEqual(output, 754018)

    def test_run_b_example_4(self):
        output = day13.day_13.run_b('test/13_example_4.txt')
        self.assertEqual(output, 779210)

    def test_run_b_example_5(self):
        output = day13.day_13.run_b('test/13_example_5.txt')
        self.assertEqual(output, 1261476)

    def test_run_b_example_6(self):
        output = day13.day_13.run_b('test/13_example_6.txt')
        self.assertEqual(output, 1202161486)

    # def test_run_b(self):
    #     output = day13.day_13.run_b('day13/13.txt')
    #     self.assertEqual(output, 894954360381385)


if __name__ == '__main__':
    unittest.main()
