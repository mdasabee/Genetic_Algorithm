from genetic_oop_func import *
def Sim_oop(numTrials):
    '''
    numTrials - (int) - integer representing the number of trials to do
    '''
    solutions = []
    for trial in range(numTrials):
        solution = genetic_oop()
        solutions.append(solution)
    return max_occurs(solutions)