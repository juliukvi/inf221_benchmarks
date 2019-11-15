import numpy as np
import timeit
import copy
import pandas as pd
# importing python script with defined algorithm if not using builtin or numpy
# sorting algorithm
import quicksort

#  name = name() #  if using imported algorithm

name = "quicksort"  # Name of sorting algorithm, if using builtin or numpy
                        # sorting algorithm

sorting_algorithm = quicksort.algorithm  # Choose sorting_algorith to test
number_of_elements = []  # Create list with the number of elements for each benchmark
limit = 22
for i in range(7, limit, 3):
    number_of_elements.append(2**i)
n_ar = 15  # Number of executions, found by using
#              number_of_executions_finder.py

number_of_elements = number_of_elements[4]
name_element_ordering = "Reverse"  # BestCase-WorstCase-MiddleCase
np.random.seed(1337) #
#test_data = np.arange(1, number_of_elements+1) # SORTED data
#test_data = np.random.random((number_of_elements,))  # RANDOM data
test_data =  np.arange(1, number_of_elements+1)[::-1] # REVERSE sorted data
clock = timeit.Timer(stmt='sort_func(copy(data))',
                     globals={'sort_func': sorting_algorithm,
                              'data': test_data,
                              'copy': copy.copy})
t = clock.repeat(repeat=7, number=n_ar)
t = pd.DataFrame(t)
t.to_pickle("./benchmarks/"+name+"-"+name_element_ordering+"-"+
            str(number_of_elements)+"-"+str(n_ar)+".pkl")
print(t)