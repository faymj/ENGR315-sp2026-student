import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values

#Set this to prepare the arrays and the number of iterations-1 to be conducted
pi_iterations = 11

#prep arrays 1
a = [1]
b = [1]
p = [1]
t = [1]

#expand arrays
for i in range(0, pi_iterations):
    a.append(1)
    b.append(1)
    p.append(1)
    t.append(1)

a[0] = 1
b[0] = 1 / ( 2 ** 0.5 )
p[0] = 1
t[0] = 1 / 4

print(a)
print(b)
print(p)
print(t)

# perform 10 iterations of this loop
for i in range(1, pi_iterations):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###
    print("RUNNING ITERATION", i)
    a[i] = ( a[i-1] +b[i-1] ) / 2
    print(a)
    b[i] = ( a[i-1] * b[i-1] ) ** 0.5
    print(b)
    p[i] = 2 * p[i-1]
    print(p)
    t[i] = t[i-1] - p[i-1] * ( ( a[i] - a[i-1] ) ** 2 )
    print(t)
 # the key detail here is that this doesn't iterate properly if you do [i+1] and [i],
 # because it doesn't properly refer to earlier numbers.
 # theres probably a way around that by pushing the iteration system down by one, but whatever.

    # print out the current loop iteration. This is present to have something in the loop.
    print("FINSIHED ITERATION ", i)
    looped_hell = ( ( ( a[i] + b[i] ) ** 2) / ( 4 * t[i] ) )
    print("result: " + str(looped_hell) )

"""
Step 3: After iterating pi iteration times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = looped_hell

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
