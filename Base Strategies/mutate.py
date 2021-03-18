import random
#helper function for mutation function
def get_good_candidates(chrom,candidates):
    """
    A Helper function for mutation
    chrom - (list) - a chromosome
    candidates - (list) - list containing candidate nodes
    """
    for gene in chrom:
        candidates.remove(gene)
    return candidates


def mutate(chromosome, Pm):
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