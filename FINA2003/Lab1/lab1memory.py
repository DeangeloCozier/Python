P = 5000
r_a = 0.04
r_b = 0.0425
n = 5
bank_a_total = P * (1 + r_a) ** n
bank_b_total = P * (1 + r_b * n)
earned_a = bank_a_total
earned_b = bank_b_total
print(f'After 5 years, I will earn ${earned_a} in Bank A.')
print(f'After 5 years, I will earn ${earned_b} in Bank B.')
if earned_a > earned_b:
    print(f'Bank A pays ${earned_a:.2f - earned_b:.2f} more than Bank B.')
else:
    print(f'Bank B pays ${earned_b:.2f - earned_a:.2f} more than Bank A.')