def mortgage_payment(principal, annual_i_rate, years):
    r = annual_i_rate/1200
    n = years * 12

    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)


def total_interest(principal, monthly_payment, years):
    return (monthly_payment * years * 12) - principal

principal = float(input("Enter the loan amount: "))
annual_i_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the loan term (years): "))

monthly_payment = mortgage_payment(principal, annual_i_rate, years)
interest = total_interest(principal, monthly_payment, years)

print(f"Monthly payment: ${monthly_payment:,.2f}")
print(f"Total interest paid: ${interest:,.2f}")

# Question 3
# In question 2, the return keyword sends each function's result back to where it was called, so the value
# can be stored and reused. mortgage_payment(principal, annual_i_rate, years) returns the monthly payment,
# which is a vlaue that can be passed to total_interest(principal, monthly_payment, years) as am argument.
# Without return, the result would not leave the function, and the second funtion wouldn't have a value to 
# compute with.