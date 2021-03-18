from All_Necessary_Funcs import *
import pylab
def genetic_mod(Pop_Size = 10 , Pc = 0.8, Pm = 0.2, max_iter = 100, Pool_Size = 2, selection = Roulette, crossover = NewCrossover,elitism = WeakParent):
    #Encoding
    Population = encode([1,8,9,11,13,16,19],4)
    #Evaluation
    Fitnesses = evaluate(Population)
                        
    #Initialization
    initial_pop = initialize(Population,Pop_Size)
    
    y = []
    index = 0
    while index < max_iter: 
        
        #Selection
        mate_pool = selection(initial_pop, Fitnesses, Pool_Size)  # 5 offspring in the pool
        
        #Crossover
        parents,offspring = crossover(mate_pool, Pc)   
        
        #Mutate
        mutant = mutate(offspring,Pm)    
        
        #Elitism
        initial_pop = elitism(initial_pop,Fitnesses,parents,mutant)  

        
        index += 1
        
        winner = max_fit(initial_pop,Fitnesses)
        y.append(winner)
    pylab.plot(range(index),y,'-r')
    
    return max_occurs(initial_pop)