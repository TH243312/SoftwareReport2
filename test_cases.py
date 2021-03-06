#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

	#以下作成したテストケース

        def test_sample5 (self):
                self.assertEqual (-1, calc(1,999.99))

        def test_sample6 (self):
                self.assertEqual (-1, calc(1.5,990.99))

        def test_sample7 (self):
                self.assertEqual (-1, calc(1.5,999))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1,990.99))

        def test_sample9 (self):
                self.assertEqual (-1, calc('a',999))

        def test_samplea (self):
                self.assertEqual (-1, calc(1,'b'))

        def test_sampleb (self):
                self.assertEqual (999, calc(1.00,999.00))

        def test_samplec (self):
                self.assertEqual (999, calc("1","999"))


