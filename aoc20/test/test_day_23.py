import unittest

import day23.day_23


class TestDay23(unittest.TestCase):
    def test_run_a_example_1a(self):
        output = day23.day_23.run_a('test/23_example_1.txt', 10)
        self.assertEqual(output, '92658374')
    
    def test_run_a_example_1b(self):
        output = day23.day_23.run_a('test/23_example_1.txt', 100)
        self.assertEqual(output, '67384529')

    def test_run_a(self):
        output = day23.day_23.run_a('day23/23.txt', 100)
        self.assertEqual(output, '24987653')
    
    # def test_run_b_example_1(self):
    #     output = day23.day_23.run_b('test/23_example_1.txt', 10000000)
    #     self.assertEqual(output, 149245887792)


if __name__ == '__main__':
    unittest.main()
