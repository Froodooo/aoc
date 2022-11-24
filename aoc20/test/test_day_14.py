import unittest

import day14.day_14


class TestDay14(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day14.day_14.run_a('test/14_example_1.txt')
        self.assertEqual(output, 165)

    def test_run_a(self):
        output = day14.day_14.run_a('day14/14.txt')
        self.assertEqual(output, 12408060320841)

    def test_run_b_example_2(self):
        output = day14.day_14.run_b('test/14_example_2.txt')
        self.assertEqual(output, 208)
    
    def test_run_b(self):
        output = day14.day_14.run_b('day14/14.txt')
        self.assertEqual(output, 4466434626828)


if __name__ == '__main__':
    unittest.main()
