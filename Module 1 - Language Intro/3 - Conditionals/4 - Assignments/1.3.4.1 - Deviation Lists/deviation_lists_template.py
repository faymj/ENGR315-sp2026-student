"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

### YOUR CODE HERE

# set this variable equal to the list with the largest standard deviation
# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList
longest_list_is = None

### YOUR CODE HERE

#I actually have enough randomness but ok.

#Use funny placeholder variables to hold the std of random_lists
potato1 = np.std(random_list_A)
potato2 = np.std(random_list_B)

#Using if else to assess higher std
if potato1 > potato2:
    longest_list_is = random_list_A
else:
    longest_list_is = random_list_B

#Diagonistic tools to assess manually that it is occuring correctly
#print(potato1)
#print(potato2)

#Printing the value so one can see it.
print("largest stdev list is: "+ str(longest_list_is))