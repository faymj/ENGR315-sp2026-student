import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path_to_datafile = "././data/drop-jump/all_participant_data_rsi.csv"

#Use examples from the last assignment to check that we are loading the file right
try:
    rawdataset = open(path_to_datafile)
except FileNotFoundError:
    print(path_to_datafile + " not found. please amend file path as neccessary (line 9)")

#setting up variables
entry = []
dataset = []
done = 0
trial = 0
force_plate_rsi = 0
accelerometer_rsi = 0
percent_error = 0


#Proccess the file information to something more useful (inspired by the mechanisms behind `Assignment 1`)
while not done:
    #turn out it is essential this comes first, or else the thing gets an unpack error.
    line = rawdataset.readline()
    if line == '':
        done = True
        continue
    
    #unpacking action (I find it weird that this doesn't need int conversion, but maybe that cause its already ints?)
    (trial, force_plate_rsi, accelerometer_rsi, percent_error) = line.rstrip().split(",")
    entry = (trial, force_plate_rsi, accelerometer_rsi, percent_error)
    
    #add to our dataset for the computer to read
    dataset.append(entry)
done = 1

print(dataset)

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph to each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')
 
#creating a plot by mapping each set of letters onto a specific temp variable, and rendering that

#UNFINISHED
# create x-axis for chi2 plot
plt.plot(force_plate_rsi, accelerometer_rsi, label='test label')
plt.title('Data mapped')
plt.xlabel('Force plate (N)')
plt.ylabel('Acceleration')
plt.legend()
plt.show()

"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE


"""
Force Plate
"""
### YOUR CODE HERE

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE

"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE