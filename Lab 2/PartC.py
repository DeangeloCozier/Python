balance = 70000
rate = 3.0
increase = 0.5

for year in range(1, 6):
    balance = balance * (1 + rate / 100)
    print(f"Mia has ${balance:,.2f} in year {year} at {rate:.2f} percent")
    rate = rate + increase

    if balance >= 80000:
        print("Target reached\n")
    else:
        print("Target not yet reached\n")
