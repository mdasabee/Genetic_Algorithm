from All_Necessary_Funcs import *

#Encoding
Population = encode([1,8,9,11,13,16,19],4)

#Evaluation
eval_list = evaluate2(Population)

#Print Highest Fitness Chromosome
print max(eval_list, key = lambda ind: eval_list[ind])