#!/usr/bin/env python
# encoding: utf-8
''''
davyncy_test.py - Unit tests for problem #2 of Counsyl Screen.

Author: Russell Mcloughlin (russ.mcl@gmail.com)
'''

import unittest
import davyncy


class DavyncyTest(unittest.TestCase):

    def test_shred_text(self):
        inp = 'THE DOG JUMPED OVER THE\nHILL. IT WAS GREAT!'
        for sample in davyncy.shred_text(inp, 3, 7):
            self.assertGreaterEqual(len(sample), 3)
            self.assertLessEqual(len(sample), 7)

    
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
            self.assertEquals(davyncy.calc_overlap(t[0],t[1]),(int(t[2]),t[3]))
            
    def test_calc_overlap2(self):
        t1 = "ity, she ran across the field\n\nafter it, and fortunately was just in ti"
        t2 =" iosity, she ran across the field\n\nafter it, and fortunately was just in tim"
        
        self.assertEquals(davyncy.calc_overlap(t1,t2)[0], 71)

    def test_build_fragment_str(self):
        t = ['EATHOTDOGSAREGOOD','SNOOPDOGY','HOTDOG','SWEETSNOOP']
        f = dict(enumerate(t))
        
        s = davyncy.build_fragment_str(f)
        predict = "EATHOTDOGSAREGOOD$$$0!!!SNOOPDOGY$$$1!!!HOTDOG$$$2!!!SWEETSNOOP$$$3!!!"
        self.assertEquals(s, predict)
        
    def test_get_pair_longest_overlap(self):
        t = ['EATHOTDOGSAREGOOD','SNOOPDOGY','HOTDOG','SWEETSNOOP']
        f = dict(enumerate(t))
        overlaps = list(davyncy.get_pair_longest_overlap(f,1))

        #EATHOTDOGSARGEGOOD and HOTDOG  -> HOTDOG
        self.assertEquals(overlaps[0], (2,0))
        
        ##EATHOTDOGSARGEGOOD and HOTDOG  -> DOG
        self.assertEquals(overlaps[1], (2,0))
        
        ##SWEETSNOOP and SNOOPDOGY  -> SNOOP
        self.assertEquals(overlaps[2], (3,1))
        
if __name__ == '__main__':
    unittest.main()