#All necessary functions
from itertools import combinations
from numpy import loadtxt
import random
import math
#################################################################################
#Encoding function definition
def encode(candidates, k):
    """
    candidates - (list) - a list containing candidate nodes eg.[1,2,3]
    k - (int) - number of required terminals
    """
    combn = list(combinations(candidates,k))
    return combn
    
################################################################################
#Initialization function definition
def initialize(pop,size):
    '''
    pop - (list) A list containing all chromosomes
    size - (int) Representing the size of the initial population
    '''
    #import random
    initial_pop = random.sample(pop,size)
    return initial_pop
    
###################################################################################################################################    
#Evaluation function definition
    
def evaluate(initial_pop, dist_mat= 'Data/c.csv', serv_mat = 'Data/x.csv', potential = 'Data/d.csv' , neighbours = 'Data/J_star.csv'):
    '''
    initial_pop - list containing all chromosomes
    dist_mat - csv file containing distance matrix
    serv_mat - csv file containing service matrix 
    potential - csv file containing potentials for the nodes
    neighbours - csv file containing neighbours for candidate nodes
    '''
    #Reading in csv files
    c = loadtxt(dist_mat, delimiter = ',')
    x = loadtxt(serv_mat, delimiter = ',')
    d = loadtxt(potential,delimiter = ',')
    J_star = loadtxt(neighbours,delimiter = ',')
    no_chromosomes = len(initial_pop)

    fitness = {}
    count = 0
    while count < no_chromosomes:
        total = 0
        for i in initial_pop[count]:
            for j in range(20):
                total += math.exp(-1*c[i-1][j])*x[i-1][j]*d[j]*J_star[i-1][j]  
        fitness[initial_pop[count]] = total
        count += 1
    return fitness

############################################################################################################        
#helper function for selection process
def inside(range_dict, val):
    '''
    This is a helper function for the selection function
    range_dict - (dict) range dictionary with mapping of fitness values and the
                    corresponding chromosome
    val - (float) a value whose range we are searching for.
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]


#Selection Function definitions
def Roulette(chromosomes,fitness,n=2):
    '''
    chromosomes - list containing chromosomes
    fitness - dict containing chromosome - fitness pair values for all chromosomes
    n - int : number of elements desired in mating pool
    '''
    range_dict = {}
    mating_pool = []
    so_far = 0

    #This creates the wheel
    for chrom in chromosomes:
        new_fitness = fitness[chrom]
        x,y = so_far , so_far+new_fitness  
        range_dict[x,y] = chrom  #try changing this around too
        so_far += new_fitness

    #This selects randomly from the wheel
    for i in range(n):
        rnum = random.uniform(0.0 , so_far) 
        temp = inside(range_dict,rnum)
        mating_pool.append(temp)
    return mating_pool

    


#########################################################################################
#helper function for crossover and mutation functions
def get_good_candidates(chrom,candidates= [1,8,9,11,13,16,19]):
    """
    A Helper function for mutation
    chrom - (list) - a chromosome
    candidates - (list) - list containing candidate nodes
    """
    can_copy = candidates[:]
    for gene in chrom:
        can_copy.remove(gene)
    return can_copy
    
    
#Crossover function definitions
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
    
################################################################################ 
#Mutation function definition
def mutate(chromosome, Pm):
    """
    chromosome - a single chromosome string
    Pm - probability of mutation
    """
    rnd = random.uniform(0,1)
    if rnd < Pm:
        ind = random.randint(0,3)
        good_candidates = get_good_candidates(chromosome)
        new_gene = random.sample(good_candidates,1)
        chromosome[ind] = new_gene[0]
    return sorted(chromosome)


#######################################################################################
    #elitism    
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
      

def Random(current_pop, mutant):
    '''
    current_pop - (list) - list containing current population of fixed size
    mutant - (list) - consists of offspring which may or maynot have been mutated
    '''
    removee = random.sample(current_pop,1)
    current_pop.remove(removee[0])
    current_pop.append(tuple(mutant))
    return current_pop
    
########################################################################################
# Helper function for determining best offspring.

def max_occurs(initial_pop):    #This is for the simulation
    max_num = 0
    winner = 0
    so_far = []
    for chrom in initial_pop:
        if chrom in so_far:
            continue
        else:
            current = initial_pop.count(chrom)
            so_far.append(chrom)
            if current > max_num:
                max_num = current
                winner = chrom
    return winner
    
def max_fit(initial_pop,fitness):
    small_fit = []
    for chrom in initial_pop:
        small_fit.append(fitness[chrom])
        
    return max(small_fit)
    