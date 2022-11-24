import unittest

from day5.day_5 import Day5
from day5.day_5_alt import Day5Alt


class TestDay5(unittest.TestCase):
    def setUp(self):
        self.day = Day5()
        self.day_alt = Day5Alt()

    def test_run_example_1(self):
        output = self.day.run_a('test/5_example_1.txt')
        self.assertEqual(output, 357)
    
    def test_run_example_2(self):
        output = self.day.run_a('test/5_example_2.txt')
        self.assertEqual(output, 567)
    
    def test_run_example_3(self):
        output = self.day.run_a('test/5_example_3.txt')
        self.assertEqual(output, 119)
    
    def test_run_example_4(self):
        output = self.day.run_a('test/5_example_4.txt')
        self.assertEqual(output, 820)
    
    def test_run_a(self):
        output = self.day.run_a('day5/5.txt')
        self.assertEqual(output, 908)
    
    def test_run_b(self):
        output = self.day.run_b('day5/5.txt')
        self.assertEqual(output, 619)
    
    def test_run_a_alt(self):
        output = self.day_alt.run_a('day5/5.txt')
        self.assertEqual(output, 908)
    
    def test_run_b_alt(self):
        output = self.day_alt.run_b('day5/5.txt')
        self.assertEqual(output, 619)


if __name__ == '__main__':
    unittest.main()
