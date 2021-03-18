from numpy import loadtxt
import math
import random

class Population(object):
    def __init__(self,pop):
        """
        pop - (list) - a list containing lists of encoded chromosomes
        """
        self.pop = pop
        
    def GetPop(self):
        """
        returns the population object (self.pop)
        """
        return self.pop[:]
        
    def SetPop(self,pop):
        """
        pop - (list) - a list containing encoded chromosomes
        sets self.pop to pop
        """
        self.pop = pop
        
    def AddToPop(self,new_elem):
        """
        new_elem - (list) list containing new chromosomes to be added
        """
        self.pop.append(new_elem)
        
    def RemoveFromPop(self, old_elem):
        """
        old_elem - (list) list representing a chromosome in self.pop
        """
        self.pop.remove(old_elem)
        
    def __str__(self):
        """
        returns self.pop with nice formatting
        """
        string = "There are " + len(self.Getpop()) + "elements in the population. They are: "
        return string, self.Getpop()
        
        
##############################################################################################3        
     
class Genetic(Population):
    def __init__(self,pop):
        """
        pop - A population object
        """
        Population.__init__(self,pop)
        self.initital_pop = []
        self.fitness = {}
        self.mating_pool = []
        
        
    def Initialize(self,size):
        """
        size - (int) - indicates the size of the initial population
        """
        ini_pop = random.sample(self.pop.GetPop(),size) 
        self.initial_pop = Population(ini_pop)
        
    def Evaluate(self, dist_mat= 'Data/c.csv', serv_mat = 'Data/x.csv', potential = 'Data/d.csv', neighbours='Data/J_star.csv'):
        '''
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
            
        Ini_Pop = self.pop.GetPop()
        for chrom in Ini_Pop:
            total = 0
            for i in chrom:
                for j in range(20):
                    total += math.exp(-1*c[i-1][j])*x[i-1][j]*d[j]*J_star[i-1][j]  
            self.fitness[chrom] = total
        #return self.fitness

        
    def Selection(self, Pool_Size = 2):
        '''
        Pool_Size - (int) : number of elements desired in mating pool
        This function does Roulette wheel selection
        '''
        range_dict = {}
        ini_pop = self.initial_pop.GetPop()
        so_far = 0

        #This creates the wheel
        for chrom in ini_pop:
            (x,y) = (so_far , so_far + self.fitness[chrom])
            range_dict[x,y] = chrom
            so_far += self.fitness[chrom]
        #This selects randomly from the wheel
        for i in range(Pool_Size):
            rnum = random.uniform(0 , so_far) 
            temp = inside(range_dict,rnum)
            self.mating_pool.append(temp)
        #return self.mating_pool
        
    def Crossover(self , Pc):
        '''
        Pc - (float) - Probability of crossover, 0 < Pc < 1
        '''
        parents = random.sample(self.mating_pool , 2)
    
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
            
            
    #Mutation function definition
    def Mutate(self,chromosome, Pm):
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
        
    ###Weakest      Remove if not necessary
    #def Elitism(self, mutant):
    #    '''
    #    mutant - (list) - consists of offspring which may or maynot have been mutated
    #    '''
    #    removee = self.initial_pop.GetPop()[self.fitness.index(min(self.fitness))]
    #    self.initial_pop.RemoveFromPop(removee)
    #    self.initial_pop.AddToPop(tuple(mutant))
    
    def Elitism(self, parents, mutant):
        '''
        parents - (list) - consists of the two parents selected for mating
        mutant- (list) - consists of offspring which may or may not have been mutated
        This function does Weak Parent elitism
        '''        
        par1_fit = self.fitness[tuple(parents[0])]
        par2_fit = self.fitness[tuple(parents[1])]
        mut_fit = self.fitness[tuple(mutant)]
        if mut_fit > min(par1_fit, par2_fit):
            if min(par1_fit, par2_fit) == par1_fit:
                weak_parent = parents[0]
            else:
                weak_parent = parents[1]
                
            self.initial_pop.RemoveFromPop(tuple(weak_parent))
            self.initial_pop.AddToPop(tuple(mutant))
                    
        return self.initial_pop.GetPop()    
       
    def NewGeneration(self):
        '''
        This is just for clearing the mating pool and fitnesses for a new generation
        '''
        self.mating_pool = []    
    
#####################################################################
#The following are helper functions used in the Genetic object
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

def inside(range_dict, val):
    '''
    This is a helper function for the selection function
    range_dict - (dict) range dictionary with mapping of fitness values and corresponding chromosome
    val - (float) a value which will 
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]
            
def max_occurs(initial_pop):
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
    return max_num,winner

def max_occurs2(initial_pop):    #This is for the simulation
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
#########################################################################
    