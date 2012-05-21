''''
amino.py - Solution to Problem #1 of Counsyl Screen.

'''
INPUT_FILE = 'amino.csv'

def load_amino_acids(filename):
    '''
    Load a csv file containing amino acids, one per line in the following
    format:
            name,codon1,codon2,...
    
    :param filename: The filename of the csv file.
    :type filename: str
    :return: dictionary of codon to name.
    '''
    codon2name = {}
    acids = map(lambda x: x.strip().split(','), open(filename))

    for acid in acids:
        name = acid[0].strip()
        codons = map(lambda x:x.strip(), acid[1:])

        for c in codons:
            codon2name[c] = name
            
    return codon2name

def is_single_sub(s1, s2):
    '''Determine if two strings differ by a single character
    
    :param s1: The first string.
    :type s1: str
    :param s2: The second string.
    :type s1: str
    :returns: bool
    '''
    d = [i for i in xrange(len(s1)) if s1[i] != s2[i]]
    if len(d) != 1:
        return False
    return True 

def build_single_bp_conversion_dict(codon2name):
    '''
    Build dictionary of amino acids to a set of amino acids that can be
    converted to with a single base pair change
    
    :param codon2name: Dictionary of codon sequence to amino acid name.
    :type codon2name: dict
    :returns: dictionary of codon names -> set of codon names.
    '''
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

def main():
    '''
    Read in amino acid file and then write out which amino acids can
    be converted in by a single bp change
    '''
    global INPUT_FILE
    codon2name = load_amino_acids(INPUT_FILE)
    
    sbp_conv = build_single_bp_conversion_dict(codon2name)
            
    for src,trgs in sbp_conv.iteritems():
        trg = ','.join(trgs)
        print '%s: %s' % (src, trg)

if __name__ == '__main__':
    main()