#!/bin/env python

import unittest

class TestMathErrors(unittest.TestCase):
    def test_00(self):
        x = 1 + 1
        answer = 2
        self.assertEqual(x, answer)

if __name__ == '__main__':
    unittest.main()
