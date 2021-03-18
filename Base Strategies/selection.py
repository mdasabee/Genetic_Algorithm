from evaluate import *
import random

def inside(range_dict,val):
    '''
    This is a helper function for selection function
    dic - range dictionary
    val - (float)
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]

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
        rnd = random.uniform(0.0 , so_far) 
        temp = inside(range_dict,rnd)
        mating_pool.append(temp)
    return mating_pool

    
def Tournament(Pop, fitness, Tour_Size , rounds = 2):
    """
    Pop - (list) - A population of chromosomes
    fitness - (dict) - Chromosome - Fitness value pairs for all chromosomes
    Tour_Size - (int) - Number of individuals per tournament
    rounds - (int) - Number of tournament rounds to do 
    """
    ini_sample = random.sample(Pop , Tour_Size)
    #fitness  = []
    pool = []
    max_fit = 0
    max_chrom = 0
    for num in range(rounds):
        for chrom in ini_sample:
            if fitness[chrom] > max_fit:
                max_fit = fitness[chrom]
                max_chrom = chrom
        pool.append(max_chrom)
    return pool
    
        
################################################################################3        
        
#def Rank(Ini_Pop , fitness , n = 2):
#    '''
#    Ini_Pop - list containing chromosomes
#    fitness - list containing fitness values of chromosomes in corresponding index
#    n - int : number of elements desired in mating pool
#    '''
#    sum_fitness = sum(fitness)
#    fit_chrom = zip(fitness,Ini_Pop)
#    range_dict = {}
#    mating_pool = []
#    so_far = 0
#    count = 0
#
#    while count < len(fitness):
#        x,y = so_far,so_far+fitness[count]
#        range_dict[x,y] = chromosome[count]
#        so_far += fitness[count]
#        count += 1
#
#    for i in range(n):
#        rnd = random.uniform(0,sum_fitness) 
#        temp = inside(range_dict,rnd)
#        mating_pool.append(temp)
#    return mating_pool    
