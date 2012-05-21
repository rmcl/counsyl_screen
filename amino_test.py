#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Russell Mcloughlin on 2012-05-16.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import unittest
import amino

class AminoTest(unittest.TestCase):
    '''Test cases for amino.py'''
    
    def test_is_single_sub(self):
        '''Test single sub method output.'''
        tests = """
        russell rassell
        bob bab
        UGA UAG
        AUG AGG
        """.strip().splitlines()
        tests = map(lambda x: x.split(), tests)
        
        truth = [True, True, False, True]
        
        for tid in xrange(len(tests)):
            self.assertEquals(amino.is_single_sub(tests[tid][0], tests[tid][1]),
                              bool(truth[tid]))
    
if __name__ == '__main__':
    unittest.main()