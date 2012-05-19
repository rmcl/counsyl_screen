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

def shred_text(source, min_fragment_len = 35, max_fragment_len = 50):
	'''
	Break a string into many fragments of length between a min and max.

	:param source: The source text to shred.
	:param min_fragment_len: The minimum length of fragments to return.
	:param max_fragment_len: The maximum length of fragments to return.
	'''
	cur_pos = 0
	src_len = len(source)
	
	fragments = []
	while cur_pos < src_len:
		frag_len = random.randint(min_fragment_len, max_fragment_len)

		fragments.append(source[cur_pos:cur_pos+frag_len])

		cur_pos += frag_len

	random.shuffle(fragments)
	return fragments

def calc_overlap(a, b, min_overlap):
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

def main():
	min_overlap = 11
	fragments = []
	for i in xrange(10):
		fragments.extend(shred_text('\n'.join(open('davyncy_source.txt').readlines())))

	fragments = filter(lambda x: len(x) > min_overlap, fragments)
	
	f = open('davyncy_source_frags.txt', 'w+')
	for frag in fragments:
		f.write("'''"+frag+"'''\n")
	f.close()
	
	fragments = dict(enumerate(fragments))

	

	while len(fragments) > 1:
		
		print 'NUM fragments: ', len(fragments)
		if len(fragments) < 10:
			
			for frag in fragments.items():
				print frag[1]
				print '===================================='
		
		start = time.time()
		
		distance = []
		for xnum, xfrag in fragments.iteritems():
			for ynum, yfrag in fragments.iteritems():
				if xnum == ynum:
					continue
		
				overlap_count, overlap = calc_overlap(xfrag, yfrag, min_overlap)
				
				if overlap_count < min_overlap:
					continue
				distance.append(((xnum,ynum), overlap_count, overlap))

		distance = sorted(distance, key=lambda x:x[1], reverse=True)
			
		print 'TIME: ',time.time() - start

		max_id = len(fragments)	
		for d in distance:
			(frag1, frag2), overlap_count, overlap = d

			# If the two fragments don't overlap then don't use their combination
			if overlap_count <= 0:
				continue
			
			if frag1 not in fragments or frag2 not in fragments:
				continue
			
			del fragments[frag1]
			del fragments[frag2]
			fragments[max_id] = overlap
			max_id += 1


	print fragments.items()[0][1]

if __name__ == '__main__':
	main()

