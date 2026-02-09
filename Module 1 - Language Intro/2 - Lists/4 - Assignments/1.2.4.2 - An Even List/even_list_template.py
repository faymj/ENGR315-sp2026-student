import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""

#find out the "left" and the "right" sides of the middle of our list
list_left_middle = ( ( len(even_list) // 2 ) -1)  
list_right_middle = ( ( len(even_list) // 2 ) )  

#placeholders to check the numbers are what I expect them to be
#print(list_left_middle)
#print(list_right_middle)

#performing the average of the two middle values
middle_average = (( even_list[list_left_middle] + even_list[list_right_middle] ) / 2 )

#placeholders to check the numbers are what I expect them to be
#print(even_list[list_left_middle])
#print(even_list[list_right_middle])

# reading that value of the middle two values
print("The average of the middle values is: ", middle_average)
