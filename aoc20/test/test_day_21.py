import unittest

import day21.day_21


class TestDay21(unittest.TestCase):
    def test_run_a_example_1(self):
        output = day21.day_21.run_a('test/21_example_1.txt')
        self.assertEqual(output, 5)
    
    def test_run_a(self):
        output = day21.day_21.run_a('day21/21.txt')
        self.assertEqual(output, 1679)
    
    def test_run_b_example_1(self):
        output = day21.day_21.run_b('test/21_example_1.txt')
        self.assertEqual(output, 'mxmxvkd,sqjhc,fvjkl')
    
    def test_run_b(self):
        output = day21.day_21.run_b('day21/21.txt')
        self.assertEqual(
            output, 'lmxt,rggkbpj,mxf,gpxmf,nmtzlj,dlkxsxg,fvqg,dxzq')


if __name__ == '__main__':
    unittest.main()
