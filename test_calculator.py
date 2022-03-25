import calculator

import unittest

class calculator_test(unittest.TestCase):
    def test_add(self):
        a = 98
        b = 78
        c = calculator.add(a, b)
        self.assertEqual(a+b, c)

    def test_sub(self):
        a = 78
        b = 34
        c = calculator.sub(a, b)
        self.assertEqual(a-b, c)

    def test_mul(self):
        a = 23
        b = 34
        c = calculator.mul(a, b)
        self.assertEqual(a*b, c)

    def test_div(self):
        a = 23
        b = 34
        c = calculator.div(a, b)
        self.assertEqual(a/b, c)
if __name__=="__main__":
    unittest.main()