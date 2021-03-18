from All_Necessary_Funcs import *
import pylab
#Encoding
Population = encode([1,8,9,11,13,16,19],4)
#Evaluation
Fitnesses = evaluate2(Population)

random.seed(10)  #Check to ensure reproducibility. ##Comment out afterwards
              
#Initialization
initial_pop = initialize(Population,10)

index = 0
while index < 100:       #stopping criteria 100 for now    
    #Selection
    mate_pool = Roulette(initial_pop, Fitnesses, 2)  # 2 offspring in the pool
    
    #Crossover      
    parents,offspring = NewCrossover(mate_pool, 0.8)   #Pc = 0.8

    #Mutate
    mutant = mutate(offspring,0.2)    #Pm = 0.2
    
    #Elitism       
    initial_pop = WeakParent(initial_pop,Fitnesses,parents,mutant)
   
    index += 1

    winner = max_fit(initial_pop,Fitnesses)
    pylab.figure()
    pylab.plot(index,winner,'ob')

print index,len(initial_pop)
print max_occurs(initial_pop)