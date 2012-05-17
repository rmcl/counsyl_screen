'''
Counsyl Technical Screen
Problem #3
A program that maps coordinates to the human reference genome via pygr.

Author: Russell McLoughlin (russ.mcl@gmail.com)
'''
from pygr import worldbase

INPUT_FILE='pygr_in.csv'


def read_input(filename):
    i = 0
    for line in open(filename):
        i += 1
        if i == 1:
            continue

        name, chromosome, start, end = line.strip().split(',')
        yield name, chromosome, start, end


def main(): 
    global INPUT_FILE

    hg19 = worldbase.Bio.Seq.Genome.HUMAN.hg19()        

    print 'name,sequence,5p_flank,3p_flank'
    
    for name, chromosome, start, end in read_input(INPUT_FILE):

        start = int(start)
        end = int(end)

        try:
            chrome = hg19[chromosome]

            sequence = str(chrome[start:end])
            five_flank = str(chrome[start-20:start])
            three_flank = str(chrome[end:end+20])

            print ','.join((name, sequence, five_flank, three_flank))

        except KeyError:
            raise 'invalid chromosome'

if __name__ == '__main__':
    main()
