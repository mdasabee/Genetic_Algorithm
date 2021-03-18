from All_Necessary_Classes import *
from itertools import combinations
def genetic_oop(Pop_Size = 10 , Pc = 0.8, Pm = 0.2, Pool_Size = 5, max_iter = 100):
    
    chromosomes = list(combinations([1,8,9,11,13,16,19],4))
    
    Pop = Population(chromosomes)
    Test1 = Genetic(Pop)
    
    #random.seed(10)  #Check to ensure reproducibility. ##Comment out afterwards
 
    #Evaluation
    Test1.Evaluate()
    #Initialization
    Test1.Initialize(Pop_Size)
    
    index = 0
    while index < max_iter:      
        Test1.NewGeneration()   #A new generation
        
        #Selection
        Test1.Selection(Pool_Size)  # 5 offspring in the pool
        
        #Crossover
        parents,offspring = Test1.Crossover(Pc)
        
        #Mutate
        mutant = Test1.Mutate(offspring , Pm)  
        
        #Elitism
        Test1.Elitism(parents,mutant)
        
        index += 1
    
    #print 'There are ', len(Test1.initial_pop.GetPop()), 'chromosomes in the final generation. The best is:'
    return max_occurs2(Test1.initial_pop.GetPop())