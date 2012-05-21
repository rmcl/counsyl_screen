#!/usr/bin/env python
# encoding: utf-8
"""
davyncy.py - Solution to problem 2 of Counsyl Technical screen.

Russell Mcloughlin on 2012-05-18.
"""
import sys
import os
import random
import time
import heapq
import numpy as np

sys.path.append('./lib/pysuffix/')
import tools_karkkainen_sanders as tks

def shred_text(source, min_fragment_len, max_fragment_len):
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

def build_fragment_str(fragments):
    '''Build a string with all of the fragments concatenated together
    
    This will be used by suffix array to find the maximal overlap match
    quickly.
    
    :param fragments: A dictionary of fragments.
    :param type: dict
    :return: string of all fragments with labels appended
    '''
    concat = ''
    cur_pos = 0
    for frag_id, frag in fragments.iteritems():
        label = '%s$$$%d!!!' % (frag,frag_id)
        concat += label
        cur_pos += len(frag) + len(label)

    return concat
    
def get_pair_longest_overlap(fragments, min_overlap):
    '''
    Generator returning maximum overlap matches betwen pairs of fragments.
    
    Algorithm:
        Concatenate fragments + labels into a single string
        Build a suffix array from string
        Compute the longest common prefix (LCP) for each element in the array
        Sort LCP array by size of LCP
        for each element in sorted LCP:
            where the LCP is greater than the minimum overlap
            Extract the LCP element label and the label of the following element. 
            These two elements have the largest overlap in the suffix array so yield them.
    '''
    
    # Build the concatenated fragment + label string.
    concat_frags = build_fragment_str(fragments)

    # Build a suffix array via the karkkainen sanders algorithm
    # Then compute the longest common prefixes
    sa = tks.simple_kark_sort(concat_frags)
    lcp = tks.LCP(concat_frags,sa)
    
    # Sort the LCP by size largest to smallest.
    sorted_lcp = sorted(enumerate(lcp),key=lambda x:x[1], reverse=True)
   
    # Iterate through sorted LCP list.
    for cur_lcp_pos, max_lcp_val in sorted_lcp:
        # If the overlap of this LCP entry is smaller than the minimum overlap
        # then stop yielding label pairs
        if max_lcp_val < min_overlap:
            break

        # Step through contiguous elements in the suffix array and extract
        # labels.
        labels = []
        while len(labels) < 2:
            # Labels are integers prefixed with "$$$" and followed by "!!!"
            label_start = concat_frags.find('$$$', sa[cur_lcp_pos]) + 3
            label_end = concat_frags.find('!!!', label_start)

            # Extract the label and convert from string to int
            label = int(concat_frags[label_start: label_end])
    
            labels.append(label)
            cur_lcp_pos += 1
        
        # If the two entries in the suffix array come from the same fragment
        # then go to the next highest LCP entry.
        if labels[0] == labels[1]:
            continue

        yield labels[0], labels[1]

def calc_overlap(a, b, min_overlap = 1):
    '''
    Calculate the overlap between two strings assuming one of four cases:
        1. a is a substring of b
        2. b is a substring of a
        3. a is a prefix of b
        4. b is a prefix of a


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
    #check for complete overlap (cases 1 & 2)
    if a.find(b) >= 0:
        return len(a), a
    elif b.find(a) >= 0:
        return len(b), b
    elif a == b:
        return len(a), a

    # Check if b is a prefix of a
    maxn = 0
    for n in xrange(1, 1 + min(len(a), len(b))):
        suffix = a[-n:]
        prefix = b[:n]
        if prefix == suffix:
            maxn = n
    if maxn >= min_overlap:
        return maxn, a + b[maxn:]
    else:
        # Check if b is a prefix of a
        for n in xrange(1, 1 + min(len(b), len(a))):
            suffix = b[-n:]
            prefix = a[:n]
            if prefix == suffix:
                maxn = n

    if maxn >= min_overlap:
        return maxn, b + a[maxn:]

    return 0, ''
      
def assemble(fragments, min_overlap = 10):
    '''Given a list of fragments, combine them into a single fragment.
    
    :param fragments: A list of text fragments
    :type fragments: dictionary of int -> str
    :param min_overlap: The minimum overlap to accept between two strings
    :type min_overap: int
    :return: A string containing the assembled fragments.
    '''

    max_id = len(fragments)
    
    # Loop until only a single fragment remains
    while len(fragments) > 1:
        for frag_id in fragments.keys():
            if len(fragments[frag_id]) < min_overlap:
                del fragments[frag_id]

        for frag1_id, frag2_id in get_pair_longest_overlap(fragments, min_overlap):
            if frag1_id not in fragments or frag2_id not in fragments:
                continue

            overlap_len, combined = calc_overlap(fragments[frag1_id], fragments[frag2_id])
                        
            # If the two fragments don't overlap then don't use their combination
            if overlap_len < min_overlap:
                continue

            # Remove the two source fragments
            del fragments[frag1_id]
            del fragments[frag2_id]
            
            # Add the combined fragment with the next largest id number
            fragments[max_id] = combined
            max_id += 1

    # There should be only a single fragment left.
    return fragments.items()[0][1]
    


def main():
    '''
    Read in a file of fragments, assemble them and write out the assembled
    result.
    
    
    '''
    
    # Generate fragments from source text.
    fragments = []
    for i in xrange(10):
        fragments.extend(shred_text('\n'.join(open('davyncy.txt').readlines()),
                         min_fragment_len = 31, max_fragment_len = 75))
    # Convert fragments into dictionary with unique ids
    fragments = dict(enumerate(fragments))

    # Assemble the fragments
    fragment = assemble(fragments)

    print fragment

if __name__ == '__main__':
    main()

