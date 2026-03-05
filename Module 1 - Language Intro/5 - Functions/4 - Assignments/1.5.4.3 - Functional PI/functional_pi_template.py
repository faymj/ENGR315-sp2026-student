import math

desired_error = 1E-10

def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    #summoning the creature from my earlier assignment about PI.
    calculateit = abs( math.log10( desired_error ) / 2 )
    print(calculateit)
    pi_iterations = int(calculateit)
    print(pi_iterations)

    print("check what the heck this number is" , calculateit)

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
    print("iterations to occur:" , pi_iterations)

    # perform pi_interations iterations of this loop
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

    ### YOUR CODE HERE ###

    # change this so an actual value is returned
    return looped_hell

approximation = my_pi( desired_error )

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
