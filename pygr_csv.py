'''
Counsyl Technical Screen
Problem #3
A program that maps coordinates to the human reference genome via pygr.

Author: Russell McLoughlin (russ.mcl@gmail.com)
'''
import logging
from pygr import worldbase

INPUT_FILE = 'pygr_in.csv'

def read_input(filename):
    '''
    Generator to read in a csv file of the following format:
        "name, chromosome, start, end\n"
    Convert start and end to integers.

    :param filename: The filename of the input file.
    :type filename: str.
    :return: An iterator of tuples in the format (name, chrom, start, end).
    
    '''
    i = 0
    for line in open(filename):
        i += 1
        if i == 1:
            continue

        try:
            name, chromosome, start, end = line.strip().split(',')
            start, end = int(start), int(end)
            yield name, chromosome, start, end
        except ValueError:
            logging.warning('invalid input on line %d.' % (i-1))

def map2genome(chromosome, start, end):
    '''Query worldbase to map coordinates to the human genome version hg19.

    :param chromosome: The name of the chromosome to query.
    :type chromosome: str
    :param start: The start of the sequence of interest.
    :type start: int
    :param end: The end of the sequence of interest.
    :type end: int

    :returns: Return the sequence, first 20pb of five and three flank.
    '''
    hg19 = worldbase.Bio.Seq.Genome.HUMAN.hg19()        

    try:
        chrome = hg19[chromosome]
    except KeyError:
        raise Exception, "Invalid Chromosome %s." % (chromosome)

    sequence = str(chrome[start:end])
    five_flank = str(chrome[start-20:start])
    three_flank = str(chrome[end:end+20])

    return sequence, five_flank, three_flank

def main():
    '''Read input from file and print results to stdout.'''
    global INPUT_FILE

    print 'name,sequence,5p_flank,3p_flank'
    
    for name, chromosome, start, end in read_input(INPUT_FILE):
        result = map2genome(chromosome, start, end)
        print name+','+','.join(result)

if __name__ == '__main__':
    main()
