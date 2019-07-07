#!/usr/bin/env python
from collections import namedtuple, defaultdict

BacteriaPartDNA = namedtuple('BacteriaPartDNA', 'gene_name dna_part_sequence length')

FILES = [
    'atpD trimAI.out',  'dnaK trimAL.out',
    'rpoB trimAI.out',
    'dnaA trimAI.out',  'gyrB trimAL.out',  'recA trimAI.out',  'thrC TrimAI.out',
]


BACTERIA_GENOME = defaultdict(list)

def should_skip_line(line):
    return line == '\n' or len(line.split()) != 2

def get_gene_data(bacteria_gene_name):
    bacteria, gene = bacteria_gene_name.rsplit('_', 1)
    return bacteria, gene

def process_input_file(filename):
    with open(filename) as f:
        next(f)
        for line in f:
            if should_skip_line(line):
                continue
            bacteria_gene_name, dna_sequence = line.split()
            if not bacteria_gene_name and not dna_sequence:
                continue
            bacteria, gene = get_gene_data(bacteria_gene_name)
            info = BacteriaPartDNA(gene, dna_sequence, len(dna_sequence))
            BACTERIA_GENOME[bacteria].append(info)

def main():
    for file in FILES:
        process_input_file(file)
    print BACTERIA_GENOME.keys()

if __name__ == '__main__':
    main()


