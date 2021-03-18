from itertools import combinations

def encode(candidates, k):
    """
    candidates - (list) - a list containing candidate nodes eg.[1,2,3]
    k - (int) - number of required terminals
    """
    combn = list(combinations(candidates,k))
    return combn

#pop = list()
#for i in range(1,21):
#    for j in range(i+1,21):
#        for k in range(j+1,21):
#            for l in range(k+1,21):
#                pop.append([i,j,k,l])


#Assuming candidates are nodes 1,8,9,11,13,16,19 and we want 4 as terminals
#box = list(combinations([1,8,9,11,13,16,19],4))
#print box
#print len(box)

def encode(candidates, k):
    """
    candidates - (list) - a list containing candidate nodes eg.[1,2,3]
    k - (int) - number of required terminals
    """
    combn = list(combinations(candidates,k))
    return combn