#!/bin/env python

import unittest

class TestMathErrors(unittest.TestCase):
    """
      For each test, make an adjustment so that the value of 'x' will
      equal the value of 'answer'
    """
    
    def test_00(self):
        x = 1 + 0
        answer = 1
        self.assertEqual(x, answer)

    def test_01(self):
        x = 100 * 2
        answer = 200
        self.assertEqual(x, answer)

    def test_02(self):
        x = 0
        for i in range(4):
            x += i
        answer = 10
        self.assertEqual(x, answer)
        
    def test_03(self):
        x = 3 + 2 - 3.
        answer = 2
        self.assertEqual(x, answer)

    def test_04(self):
        x = 2 * 8
        answer = 16
        self.assertEqual(x, answer)

    def test_05(self):
        grocery_list = {
            'eggs': 1,
            'bread': 1,
            'cheese': 1,
        }
        x = sum(grocery_list.values())
        answer = 3
        self.assertEqual(x, answer)
            
if __name__ == '__main__':
    unittest.main()
