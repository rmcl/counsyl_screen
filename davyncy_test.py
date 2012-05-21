#!/usr/bin/env python
# encoding: utf-8
''''
davyncy_test.py - Unit tests for problem #2 of Counsyl Screen.

Author: Russell Mcloughlin (russ.mcl@gmail.com)
'''

import unittest
import davyncy3
#from davyncy3 import FragmentOverlap


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
	
	def test_fragment_overlap_add_frag(self):
		fo = FragmentOverlap()
		fo.add_fragment('ABCD', 1)
		fo.add_fragment('CDEFG', 2)
		fo.add_fragment('EFGHI', 3)
		
	def test_fragment_overlap_get_pair_largest_overlap(self):
		fo = FragmentOverlap()
		fo.add_fragment('ABCD', 1)
		fo.add_fragment('CDEFG', 2)
		fo.add_fragment('EFGHI', 3)
		
		print fo.get_pair_largest_overlap()
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
	def test_calc_overlap2(self):
		t1 = "ity, she ran across the field\n\nafter it, and fortunately was just in ti"
		t2 =" iosity, she ran across the field\n\nafter it, and fortunately was just in tim"
		
		print davyncy3.calc_overlap(t1,t2)
if __name__ == '__main__':
	unittest.main()