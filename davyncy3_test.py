#!/usr/bin/env python
# encoding: utf-8
''''
davyncy_test.py - Unit tests for problem #2 of Counsyl Screen.

Author: Russell Mcloughlin (russ.mcl@gmail.com)
'''

import unittest
import davyncy3


class DavyncyTest(unittest.TestCase):
	'''
	def test_shred_text(self):
		res = ''
		inp = 'THE DOG JUMPED OVER THE\nHILL. IT WAS GREAT!'
		for sample in davyncy.shred_text(inp, 3, 7):
			self.assertGreaterEqual(len(sample), 3)
			self.assertLessEqual(len(sample), 7)
			
			res += sample
		
		self.assertEqual(len(res),len(inp))
	'''
	
	def test_calc_overlap(self):
		tests = """
		howdy dyno 2 howdyno
		russell grsdturuss 4 grsdturussell
		sweet adkfjdswe 3 adkfjdsweet
		fooling inglinz 3 foolinglinz
		foozballing ball 4 foozballing
		""".strip().splitlines()
		tests = map(lambda x: x.split(), tests)
		
		for t in tests:
			print t[0],t[1]
			self.assertEquals(davyncy3.calc_overlap(t[0],t[1]),(int(t[2]),t[3]))
		
if __name__ == '__main__':
	unittest.main()