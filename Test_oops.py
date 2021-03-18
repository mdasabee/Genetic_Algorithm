from All_Necessary_Classes import *
from itertools import combinations
#Encoding
chromosomes = list(combinations([1,8,9,11,13,16,19],4))

Pop = Population(chromosomes)
Test1 = Genetic(Pop)
    
random.seed(10)  #Check to ensure reproducibility. ##Comment out afterwards

#Evaluation
Test1.Evaluate()
#Initialization
Test1.Initialize(10)

index = 0
while index < 100:       #stopping criteria 100 for now
    Test1.NewGeneration()   #A new generation
    
    #Selection
    Test1.Selection(5)  # 5 offspring in the pool
    
    #Crossover
    parents,offspring = Test1.Crossover(0.8)   #Pc = 0.8
    
    #Mutate
    mutant = Test1.Mutate(offspring , 0.2)    #Pm = 0.2
    
    #Elitism
    Test1.Elitism(parents,mutant)
    
    index += 1

print len(Test1.initial_pop.GetPop())
print max_occurs(Test1.initial_pop.GetPop())