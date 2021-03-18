from genetic_oop_func import *
def RunSim_iterations(max_iterations, numTrials = 100):
    '''
    numTrials - (int) - integer representing the number of trials to do
    mat_iterations - (list) - range of maximum number of iterations to do
    '''
    answer = {}
    for val in max_iterations:
        solutions = []
        for trial in range(numTrials):
            solution = genetic_oop(max_iter = val)
            solutions.append(solution)
        string = "max iter value "+str(val)
        answer[string] = max_occurs(solutions)
    return answer
        
def RunSim_ini_pop_size(ini_pop_size, numTrials = 100):
    '''
    numTrials - (int) - integer representing the number of trials to do
    ini_pop_size - (list) - range of inital population sizes to try
    '''
    answer = {}
    for size in ini_pop_size:
        solutions = []
        for trial in range(numTrials):
            solution = genetic_oop(Pop_Size = size)
            solutions.append(solution)
        string = "Ini Pop Size "+str(size)
        answer[string] = max_occurs(solutions)
    return answer
    
def RunSim_pc(pc_list, numTrials = 100):
    '''
    numTrials - (int) - integer representing the number of trials to do
    pc_list - (list) - range of probability of crossover values to try
    '''
    answer = {}
    for pc in pc_list:
        solutions = []
        for trial in range(numTrials):
            solution = genetic_oop(Pc = pc)
            solutions.append(solution)
        string = "Pc =  "+str(pc)
        answer[string] = max_occurs(solutions)
    return answer
    

def RunSim_pm(pm_list, numTrials = 100):
    '''
    numTrials - (int) - integer representing the number of trials to do
    pm_list - (list) - range of probability of mutation values to try
    '''
    answer = {}
    for pm in pm_list:
        solutions = []
        for trial in range(numTrials):
            solution = genetic_oop(Pm = pm)
            solutions.append(solution)
        string = "Pm = "+str(pm)
        answer[string] = max_occurs(solutions)
    return answer
    
#RunSim_iterations([100,200,300,400,500])
#RunSim_ini_pop_size([10,15,20,25,30])
#RunSim_pc([0.5,0.6,0.7,0.8,0.9])
#RunSim_pm([0.1,0.2,0.3,0.4,0.5])