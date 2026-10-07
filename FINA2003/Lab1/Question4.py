# P = 5000
# r_a = 4 # (Logic) The rate should be 0.04 as the rate is 4%, using 4 means 400% interest
# r_b = 4.25 # (Logic) The rate should be 0.0425 as the rate is 4.25%
# n = 5
# bank_a_total = P * (1 + r_a) ** n
# bank_b_total = P * (1 + r_b * n)
# earned_a = bank_a_total # (Logic) Assigns the total, which is principal + interest but it should be bank_a_total - P 
# earned_b = bank_b_total # (Logic) Assigns the total, which is principal + interest but it should be bank_b_total - P 
# print(f'After 5 years, I will earn ${earned_a} in Bank A.')
# print(f'After 5 years, I will earn ${earned_b} in Bank B.')
# if earned_a > earned_b # (Syntax) Missing the : at the end of the line
#  print(f'Bank A pays ${earned_a - earned_b:.2f} more than Bank B.')
# else # (Syntax) Missing the : at the end of the line
#  print(f'Bank B pays ${earned_b - earned_a:.2f} more than Bank A.')

P = float(input('Please enter the principal amount: '))
r_a = float(input('Please enter the interest rates as percentages (for example, enter 4 for 4%) for Bank A: ')) / 100
r_b = float(input('Please enter the iterest rates for Bank B: ' )) / 100
n = int(input('Please enter the number of years: '))
bank_a_total = P * (1 + r_a) ** n
bank_b_total = P * (1 + r_b * n)
earned_a = bank_a_total - P
earned_b = bank_b_total - P 
print(f'After 5 years, I will earn ${earned_a:.2f} in Bank A.')
print(f'After 5 years, I will earn ${earned_b:.2f} in Bank B.')
if earned_a > earned_b:
 print(f'Bank A pays ${earned_a - earned_b:.2f} more than Bank B.')
else:
 print(f'Bank B pays ${earned_b - earned_a:.2f} more than Bank A.')

# Please enter the principal amount: 8000
# Please enter the interest rates as percentages (for example, enter 4 for 4%) for Bank A: 8
# Please enter the iterest rates for Bank B: 5
# Please enter the number of years: 3
# After 5 years, I will earn $2077.70 in Bank A.
# After 5 years, I will earn $1200.00 in Bank B.
# Bank A pays $877.70 more than Bank B.

# Please enter the principal amount: 10000
# Please enter the interest rates as percentages (for example, enter 4 for 4%) for Bank A: 4.25
# Please enter the iterest rates for Bank B: 4.23
# Please enter the number of years: 4
# After 5 years, I will earn $1811.48 in Bank A.
# After 5 years, I will earn $1692.00 in Bank B.
# Bank A pays $119.48 more than Bank B.

# Please enter the principal amount: 900
# Please enter the interest rates as percentages (for example, enter 4 for 4%) for Bank A: 10
# Please enter the iterest rates for Bank B: 5
# Please enter the number of years: 10
# After 5 years, I will earn $1434.37 in Bank A.
# After 5 years, I will earn $450.00 in Bank B.
# Bank A pays $984.37 more than Bank B.