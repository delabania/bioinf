#!/usr/bin/env python
from collections import namedtuple, defaultdict
from phylip import save_to_file, fill_to_ten_characters

CONFIG = """
alignment = {filename}.phy;
branchlengths = linked;

models = all;
model_selection = aicc;

[data_blocks]
gyrB = 1-711;
recA = 712-1028;
thrC = 1029-1442;
dnaA = 1443-1871;
rpoB = 1872-3083;
dnaK = 3084-3654;
atpD = 3655-4076;
[schemes]
search = greedy;
"""

BACTERIES_NAMES_ABBR = {
    'P_yeei_TT13'            : 'TT13',
    'P_yeei_ATCC_BAA-599'    : 'ATCC_599',
    'P_yeei_CCUG_32052'      : 'CCUG_32052',
    'P_yeei_CCUG_17731'      : 'CCUG_17731',
    'P_yeei_CCUG_32054'      : 'CCUG_32054',
    'P_yeei_CCUG_13493'      : 'CCUG_13493',
    'P_yeei_FDAARGOS_252'    : 'FDA_252',
    'P_yeei_CCUG_54214'      : 'CCUG_54214',
    'P_yeei_LM_20'           : 'LM_20',
    'P_yeei_G1212'           : 'G1212',
    'P_yeei_CCUG_46822'      : 'CCUG_46822',
    'P_yeei_CCUG_32053'      : 'CCUG_32053',
    'P_aminovorans_JCM7685'  : 'JCM7685',
}

def get_gene_pos_info_line(gene, current_end, sequence_info):
    start = current_end
    end = current_end + sequence_info.length - 1
    line = '{gene} = {start}-{end};'.format(gene=gene, start=start, end=end)
    return line

class BacteriaPartDNA:
    def __init__(self):
        self.dna_sequence = ''
        self.length = 0

    def append(self, dna):
        self.dna_sequence += dna
        self.length += len(dna)

    def __str__(self):
        return self.dna_sequence

FILES = [
    'atpD trimAI.out',  'dnaK trimAL.out',
    'rpoB trimAI.out',
    'dnaA trimAI.out',  'gyrB trimAL.out',  'recA trimAI.out',  'thrC TrimAI.out',
]


BACTERIA_GENOME = defaultdict(lambda: defaultdict(BacteriaPartDNA))

def should_skip_line(line):
    return line == '\n' or len(line.split()) != 2

def get_gene_data(bacteria_gene_name):
    bacteria, gene = bacteria_gene_name.rsplit('_', 1)
    return bacteria, gene

def append_to_dict(bacteria, gene, dna_sequence):
    bacteria_gene_info = BACTERIA_GENOME[bacteria][gene]
    bacteria_gene_info.append(dna_sequence)


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
            append_to_dict(bacteria, gene, dna_sequence)


def get_full_bacteria_genome():
    full_genome = {}
    for bacteria, bacteria_genome in BACTERIA_GENOME.iteritems():
        dna = merge_genes(bacteria_genome)
        full_genome[bacteria] = dna
    return full_genome

def merge_genes(bacteria_genome):
    dna_all = ''
    for gene, dna in bacteria_genome.iteritems():
        dna_all += dna.dna_sequence

    return dna_all

def translate(full_genome):
    new_names_dict = {}
    for bacteria, genome in full_genome.iteritems():
        new_name = BACTERIES_NAMES_ABBR[bacteria]
        new_names_dict[new_name] = genome
    return new_names_dict

def main():
    for file in FILES:
        process_input_file(file)
    full_genome = get_full_bacteria_genome()
    genome = translate(full_genome)
    # print(full_genome['P_yeei_TT13'])
    #save_to_file(genome)
    save_to_file_normal(genome)

def save_to_file_normal(genome):
    for bacteria, bacteria_genome in genome.iteritems():
        name = fill_to_ten_characters(bacteria)
        print name + bacteria_genome





if __name__ == '__main__':
    main()


