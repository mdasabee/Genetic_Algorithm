from genetic_mod_func import *
def Sim_mod(numTrials):
    '''
    numTrials - (int) - integer representing the number of trials to do
    '''
    solutions = []
    for trial in range(numTrials):
        solution = genetic_mod()
        solutions.append(solution)
    
    return max_occurs(solutions)