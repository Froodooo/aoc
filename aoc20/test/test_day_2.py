import unittest

from day2.day_2 import Day2


class TestDay2(unittest.TestCase):
    def setUp(self):
        self.day = Day2()

    def test_run_a(self):
        output = self.day.run_a('test/2_example_1.txt')
        self.assertEqual(output, 2)
    
    def test_run_b(self):
        output = self.day.run_b('test/2_example_1.txt')
        self.assertEqual(output, 1)


if __name__ == '__main__':
    unittest.main()
