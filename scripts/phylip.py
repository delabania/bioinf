from collections import deque

def get_genome_parts(genome):
    genome_parts = deque()
    for i in range(0, len(genome), 10):
        genome_parts.append(genome[i:i+10])

    return genome_parts

def fill_to_ten_characters(name):
    assert len(name) <= 10
    spaces_number = 10 - len(name)
    return name + spaces_number * ' '


def get_genome_splitted(full_genome):
    genome_splitted = {}
    for bacteria, genome in full_genome.iteritems():
        genome_splitted[bacteria] = get_genome_parts(genome)
    return genome_splitted

def print_row(bacteria_splitted_genome):
    parts_num = 0
    for part in bacteria_splitted_genome:
        print part,
        parts_num += 1
        if parts_num == 5:
            break
    for i in range(parts_num):
        bacteria_splitted_genome.popleft()
    if not bacteria_splitted_genome:
        return True

    print ''

def save_to_file(full_genome):
    splitted = get_genome_splitted(full_genome)
    bacteries = set()
    end = False
    while not end:
        for bacteria in full_genome:
            if bacteria not in bacteries:
                bacteria_name = fill_to_ten_characters(bacteria)
                print bacteria_name,
            else:
                print ' ' * 10,
            bacteries.add(bacteria)

            if print_row(splitted[bacteria]):
                end = True
        print ''