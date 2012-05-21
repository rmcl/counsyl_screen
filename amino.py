''''
amino.py - Solution to Problem #1 of Counsyl Screen.

'''
INPUT_FILE='amino.csv'

def load_amino_acids(filename):
    '''
	Generator to load a csv file containing amino acids, one per line in
	the following format:
			name,codon1,codon2,...
			
	:param filename: The filename of the csv file.
	:type filename: str
	:return: Iterator of tuples in format (name, codons)
		where codons in a list of strings.
    '''
    acids = map(lambda x: x.strip().split(','), open(filename))

    for acid in acids:
        name = acid[0].strip()
        codons = map(lambda x:x.strip(), acid[1:])

        yield name, codons
		
def build_codon2name(aa):
	codon2name = {}

	for name, codons in aa:
		for codon in codons:
			codon2name[codon] = name
			
	return codon2name
	
def is_single_sub(s1, s2):
	'''Determine if two strings differ by a single character'''
	d = [i for i in xrange(len(s1)) if s1[i] != s2[i]]
	if len(d) > 1:
		return False
	return True	

def build_single_bp_conversion_dict(codon2name):
	single_bp_convertable = {}
	
	for codon_a in codon2name.keys():
		for codon_b in codon2name.keys():
			if is_single_sub(codon_a, codon_b):
				a_name = codon2name[codon_a]
				b_name = codon2name[codon_b]

				try:
					single_bp_convertable[a_name].add(b_name)
				except KeyError:
					single_bp_convertable[a_name] = set([b_name])
					
				try:
					single_bp_convertable[b_name].add(a_name)
				except KeyError:
					single_bp_convertable[b_name] = set([a_name])
	
	return single_bp_convertable

if __name__ == '__main__':
	global INPUT_FILE
	codon2name = build_codon2name(load_amino_acids(INPUT_FILE))
	
	sbp_conv = build_single_bp_conversion_dict(codon2name)
			
	for src,trgs in sbp_conv.iteritems():
		trg = ','.join(trgs)
		print '%s: %s' % (src, trg)
		