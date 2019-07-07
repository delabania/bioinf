from collections import namedtuple, defaultdict

LINE_LENGTH = 50

def write_header(file):
    print '13 4076'

def fill_to_ten_characters(name):
    assert len(name) <= 10
    spaces_number = 10 - len(name)
    return name + spaces_number * ' '

def write_row(genome, current_length, **kwargs):
    name = kwargs.pop(name)
    if name:
        print fill_to_ten_characters(name)

def is_last_genome_line(genome, current_length):
    return len(genome) - current_length <= 50

def format_line(genome, current_length):
    i = 0
    columns = []
    for i in range(5):
        column = genome[current_length:current_length + 10]
        current_length += 10
        columns.append(column)

    print '{}'.join(columns)

    return current_length

def write_genome(genome):
    for i in genome:
    if not is_last_genome_line(genome, current_length):
        current_length = format_line(genome, current_length)
    return current_length

def write_to_phylip(full_genome):
    bacteria_current_processed_genome_length = defaultdict(int)
    # with open('file.phy', 'w') as f:
    for bacteria, bacteria_full_genome in full_genome.iteritems():
        write_header(f)
        write_genome()
        for 
        bacteria_current_processed_genome_length[bacteria] 
        write_genome(bacteria_full_genome, 0)
        return
