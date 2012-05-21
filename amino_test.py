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
    def test_is_single_sub(self):
        tests = """
        russell rassell
        bob bab
        UGA UAG
        AUG AGG
        """.strip().splitlines()
        tests = map(lambda x: x.split(), tests)
        
        truth = [True, True, False, True]
        
        for t in xrange(len(tests)):
            self.assertEquals(amino.is_single_sub(tests[t][0],tests[t][1]),bool(truth[t]))
    
if __name__ == '__main__':
    unittest.main()