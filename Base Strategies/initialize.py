import random
def initialize(pop,size):
    '''
    pop - (list) A list containing all chromosomes
    size - (int) Representing the size of the initial population
    '''
    initial_pop = random.sample(pop,size)
    return initial_pop