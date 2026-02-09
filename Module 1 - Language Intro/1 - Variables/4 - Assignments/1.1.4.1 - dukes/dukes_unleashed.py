"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
# Check that I have virtual environment and stuff working
print("program woke up")

# define variables
full_time_undergrad_cost_instate = float(30792)
full_time_undergrad_cost_outstate = float(47882)
return_percent = 0.05

# assuming we mean that the return percentage is the quantity of currency that cannot be used because it is gaining interest
# we will say that one needs 1/return percent in order for it to "grow" the neccesary bonus to finance our interests
in_state_gift = (full_time_undergrad_cost_instate * ( 1.0 / return_percent ))
out_state_gift = (full_time_undergrad_cost_outstate * ( 1.0 / return_percent ))


#state the required gift values:
print("for annual University costs, the typical costs are as follows:")
print("Instate: " + str(f"{in_state_gift:,}") + " USD")
print("Outstate: " + str(f"{out_state_gift:,}") + " USD")
