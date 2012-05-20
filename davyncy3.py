#!/usr/bin/env python
# encoding: utf-8
"""
davyncy2.py

Russell Mcloughlin on 2012-05-18.

"""

import sys
import os
import random
import time
import heapq

def shred_text(source, min_fragment_len = 35, max_fragment_len = 50):
    '''
    Break a string into many fragments of length between a min and max.
    This simulates the illuminati's part in the story.

    :param source: The source text to shred.
    :param min_fragment_len: The minimum length of fragments to return.
    :param max_fragment_len: The maximum length of fragments to return.
    '''
    cur_pos = 0
    src_len = len(source)
    
    fragments = []
    # Iterate through the source string and take pieces between the min
    # and maximum fragment length.
    while cur_pos < src_len:
        frag_len = random.randint(min_fragment_len, max_fragment_len)
        fragments.append(source[cur_pos:cur_pos+frag_len])
        cur_pos += frag_len

    # mix up the fragments
    random.shuffle(fragments)

    return fragments

def calc_overlap(a, b, min_overlap = 1):
    '''
    Calculate the overlap between two strings assuming one of four cases:
        1. a is a prefix of b
        2. b is a prefix of a
        3. a is a substring of b
        4. b is a substring of a
        
    If the overlap is less than the min overlap length then return no overlap.
    
    :param a: The first string
    :type a: str
    :param b: The second string
    :type b: str
    :param min_overlap: The minimum overlap allowed between the two strings.
    :type min_overlap: int
    :return tuple of int containing amount of overlap and string containing the
        overlaping string.
    '''
    maxn = 0
    for n in xrange(1, 1 + min(len(a), len(b))):
        suffix = a[-n:]
        prefix = b[:n]
        if prefix == suffix:
            maxn = n
    if maxn >= min_overlap:
        return maxn, a + b[maxn:]
    else:
        for n in xrange(1, 1 + min(len(b), len(a))):
            suffix = b[-n:]
            prefix = a[:n]
            if prefix == suffix:
                maxn = n

    if maxn >= min_overlap:
        return maxn, b + a[maxn:]

    #check for complete overlap
    if a.find(b) >= 0:
        return len(b), a
    elif b.find(a) >= 0:
        return len(a), b

    return 0, ''

class FragmentOverlap(object):
    def __init__(self, fragments = None):
        self.fragments = {}
        self.distance = []

        tmp_distance = {}
        if fragments is not None:
            for frag_id, frag in fragments.items():
                for xnum, xfrag in self.fragments.iteritems():
                    sid, bid = min(frag_id, xnum), max(frag_id, xnum)
                    if sid == bid or (sid, bid) in tmp_distance:
                        continue

                    overlap_count, combined = calc_overlap(xfrag, frag, 1)
                    tmp_distance[(sid,bid)] = (1e9 - overlap_count, combined)

                self.fragments[frag_id] = frag

        self.distance = map(lambda x: (x[1][0], x[0], x[1][1]), tmp_distance.items())
        heapq.heapify(self.distance)
        print 'done adding frags'
    
    def add_fragment(self, frag, frag_id):   
        for xnum, xfrag in self.fragments.iteritems():
            sid, bid = min(frag_id, xnum), max(frag_id, xnum)
            if sid == bid:
                continue
        
            overlap_count, combined = calc_overlap(xfrag, frag, 1)
            heapq.heappush(self.distance, (1e9 - overlap_count, (sid,bid), combined))
            
        self.fragments[frag_id] = frag

    def rm_fragment(self, frag_id):
        del self.fragments[frag_id]
        

    def get_pair_largest_overlap(self):
        while len(self.distance) > 0:
            overlap_len, (frag1, frag2), combined = heapq.heappop(self.distance)
            overlap_len = (overlap_len - 1e9) * -1

            if frag1 not in self.fragments or frag2 not in self.fragments:
                continue

            self.rm_fragment(frag1)
            self.rm_fragment(frag2)
            #print frag1, frag2, overlap_len, combined
            return frag1, frag2, overlap_len, combined

    def num_fragments(self):
        return len(self.fragments)

def assemble(fragments):
    '''Given a list of fragments, combine them into a single fragment.'''
    
    fo = FragmentOverlap(fragments)
    
    print 'done adding fragments'

    max_id = fo.num_fragments()
    while fo.num_fragments() > 1:
        print 'number of fragments', fo.num_fragments()
        frag1_id, frag2_id, overlap_len, combined = fo.get_pair_largest_overlap()
        
        # If the two fragments don't overlap then don't use their combination
        if overlap_len <= 0:
            raise Exception, 'returned two fragments with no overlap-bad!'

        fo.add_fragment(combined, max_id)
        max_id += 1

    return fo.fragments
    

def main():
    min_overlap = 11

    # Generate fragments from source text.
    fragments = []
    for i in xrange(10):
        fragments.extend(shred_text('\n'.join(open('davyncy_source.txt').readlines())))

    # remove fragments shorter than min length
    fragments = filter(lambda x: len(x) > min_overlap, fragments)
    
    f = open('davyncy_source_frags.txt', 'w+')
    for frag in fragments:
        f.write("'''"+frag+"'''\n")
    f.close()
    
    fragments = dict(enumerate(fragments))

    fragments = assemble(fragments)

    print fragments.items()[0][1]

if __name__ == '__main__':
    main()

