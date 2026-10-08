balance = 70000
rate = 3.0
increase = 0.5
year = 1
target = 80000

while balance < target:
    balance = balance * (1 + rate / 100)

    print(f"Mia has ${balance:,.2f} in year {year} at {rate:.2f} percent")

    rate = rate + increase
    year = year + 1

print(f"\nMia has reached her savings target in {year-1} year/s.")