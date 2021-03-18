from evaluate import *
import random
def WeakParent(current_pop, fitness, parents, mutant):
    '''
    current_pop - (list) - list containing current population
    fitness - (dict) - chromosome - fitness value pairs)
    parents - (list) - consists of the two parents selected for mating
    mutant- (list) - consists of offspring which may or may not have been mutated
    '''        
    par1_fit = fitness[tuple(parents[0])]
    par2_fit = fitness[tuple(parents[1])]
    mut_fit = fitness[tuple(mutant)]
    if mut_fit > min(par1_fit, par2_fit):
        if min(par1_fit, par2_fit) == par1_fit:
            weak_parent = parents[0]
        else:
            weak_parent = parents[1]
            
        current_pop.remove(tuple(weak_parent))
        current_pop.append(tuple(mutant))
                
    return current_pop
    
########################################################################    
    
def Random(current_pop, mutant):
    '''
    current_pop - (list) - list containing current population
    mutant - (list) - consists of offspring which may or may not have been mutated
    '''
    removee = random.sample(current_pop,1)
    current_pop.remove(removee[0])
    current_pop.append(tuple(mutant))
    return current_pop
    
#############################################################################
def Weakest(current_pop,fitness, mutant):
    '''
    current_pop - (list) - list containing current population
    fitness - (dict) - chromosome - fitness value pairs      ### not so yet
    mutant - (list) - consists of offspring which may or may not have been mutated
    '''
    removee = current_pop[fitness.index(min(fitness))]
    current_pop.remove(removee)
    current_pop.append(tuple(mutant))
    return current_pop
    