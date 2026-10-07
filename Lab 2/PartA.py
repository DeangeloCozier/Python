balance = float(70000)
year = 1

rate_year1 = 3.0
print(f"Mia has ${(balance * (1 + rate_year1/100)):,.2f} in year {year} at {rate_year1} percent")


rate_year2 = 3.5
print(f"Mia has ${(balance * (1 + rate_year2/100)):,.2f} in year {year+1} at {rate_year2} percent")

# If we continued for years 3, 4, and 5 we would have to keep repeating calculating the new balance, printing the balance, year and interest rate
# continuously and setting the interest rate for each year.

