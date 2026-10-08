# Part B - AI Generated Code
# 1. Year would have 1 in the first iteration because range(1, 5) starts at 1.
# 2. This loop will iterate four times because range(1, 5) produces the numbers 1, 2, 3, 4 with 5 not included.
# 3. No, it will not change the value stored in rate, as there is no value being assigned to rate only a calculation.
# 4. Python interprets 3.0 as a number and not 3%, for a percentage it needs to be divided by 100 to be calculated as 3%

# Part C - Repare the AI Generated Code

# First Problem - Incorrect number of years
# In line 5 ( for year in range(1, 5): ), this only gives 4 years instead of 5.

# Second Problem - Incorrect balance calculation
# In line 6 ( balance = balance * (1 + rate) ), this treats rate as 3 instead of 3%, giving 4.0 instead of 1.03.

# Third Problem - Interest rate not being assigned properly 
# In line 8 ( rate + increase ), the sum is calculated but it is not stored or assigned to it does nothing.

balance = 70000
rate = 3.0
increase = 0.5

for year in range(1, 6): # Allows for the loop to iterate for 5 times instead of 4
    balance = balance * (1 + rate/100) # Calculates the interest rate correctly
    print(f"Mia has ${balance:,.2f} in year {year} at {rate:.2f} percent")
    rate = rate + increase # Assigns the calculation to a variable so changes are saved and applied.