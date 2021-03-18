from evaluate import *
import random

#helper function for crossover and mutation functions
def get_good_candidates(chrom,candidates= [1,8,9,11,13,16,19]):
    """
    A Helper function for mutation
    chrom - (list) - a chromosome
    candidates - (list) - list containing candidate nodes
    """
    for gene in chrom:
        candidates.remove(gene)
    return candidates

def NewCrossover(mating_pool, Pc):
    '''
    mating_pool - list from the selection function
    Pc - float (0<Pc<1) - Probability of crossover
    '''
    parents = random.sample(mating_pool,2)
    offspring = []
    for gene in parents[0]:
        if gene in parents[1]:
            offspring.append(gene)
    left = len(parents[0])-len(offspring)
    good_can = get_good_candidates(offspring)
    new_genes = random.sample(good_can,left)
    for ng in new_genes:
        offspring.append(ng)
    return parents,sorted(offspring)
        

def Uniform(mating_pool, Pc):
    '''
    mating_pool - list from the selection function
    Pc - float (0<Pc<1) - Probability of crossover
    '''
    [parent1,parent2] = random.sample(mating_pool,2)
    
    offspring1 = parent1[:]
    offspring2 = parent2[:]
    mask = [round(random.uniform(0,1)) for i in range(4)]
    ind = 0
    for j in range(4):
        if mask[j] == 1 and random.uniform(0,1) < Pc:
            offspring1[ind] = parent2[ind]
            offspring2[ind] = parent1[ind]
        ind += 1
    return [parent1,parent2],[offspring1,offspring2]
    
    
def OnePoint(mate_pool,Pc):
    [parent1,parent2] = random.sample(mate_pool,2)
    offspring1 = parent1
    offspring2 = parent2
    
    mask = random.randint(1,4)
    if random.uniform(0,1) < Pc:
        for j in range(mask-1):
    
            offspring1[j] = parent2[j]
            offspring2[j] = parent1[j]
    return offspring1,offspring2