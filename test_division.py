#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from Division import div


class TestDivision(unittest.TestCase):

	def test_div(self):
		self.assertEqual(div(10,2),5)

	def test_div(self):
		self.assertEqual(div(2,2),1)
	
	def test_div(self):
		self.assertEqual(div(0,2),0)
	
	def test_div(self):
		self.assertEqual(div(10,2,4),5)

if __name__ == "__main__:
	unittest.main()


