investments = [9800, 15250, 23400, 31000, 46750, 59300, 72500, 88000, 132000]

initial_rate=0.03
subsequent_rate=0.05
years=10
final_amount=[]

for principal in investments:
    amount = principal
    for year in range(1, years+1):
        if year <= 5:
            annual_rate = initial_rate
        else:
            annual_rate = subsequent_rate
        amount = amount * (1 + annual_rate)
    final_amount.append(amount)

for amount in final_amount:
    print(f'${amount:,.2f}')

# Question 3(a) Output: 
# $14,499.69
# $22,563.29
# $34,621.71
# $45,866.36
# $69,169.44
# $87,737.92
# $107,268.11
# $130,201.29
# $195,301.94

# Question 3b Calculation:
# First client's amount: $9800
# Year 1 Balance = 9,800 * 1.03
#                = $10,094 

# Year 2 Balance = 10,094 * 1.03
#                = $10,396.82

# Question 3c Output:
# $14,781.24
# $23,001.41
# $35,293.97
# $46,756.97
# $70,512.53
# $89,441.56
# $109,350.99
# $132,729.47
# $199,094.21

# Question 3c Explanation:
# Each year gets a new result that is more than the original because year 5 and beyond is being calculated
# with subsequent_rate (0.05). The original code uses subsequent_rate(0.05) for years 6-10 instead of 5-10.
# The affected year that changes the output is year 5 changing it's rate.

# Question  3d:
# In line 15, amount = amount * (1 + annual_rate) is the line that allows for the result to be carried from
# one iteration to the next. It works by mulplying the current result by the 1 + the rate and storing it in 
# back into result to be used in the next year. As the result is always included in the calculation every year's
# total is passed to the next year.