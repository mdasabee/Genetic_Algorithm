from numpy import loadtxt
import math
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
    count = 0
    fitness = []
    while count < no_chromosomes:
        total = 0
        for i in initial_pop[count]:
            for j in range(1,21):
                total += math.exp(-1*c[i-1][j-1])*x[i-1][j-1]*d[i-1]*J_star[i-1][j-1]  
        fitness.append(total)
        count += 1
    return fitness
    
    
def evaluate2(initial_pop, dist_mat= 'Data/c.csv', serv_mat = 'Data/x.csv', potential = 'Data/d.csv' , neighbours = 'Data/J_star.csv'):
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