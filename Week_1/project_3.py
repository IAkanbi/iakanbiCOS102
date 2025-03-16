# Code for calculating Annuity Plan
P = int(input("Enter the Principal Amount: "))
R = int(input("Enter the interest rate: "))
n = int(input("Enter how many times interest is applied per time period"))
T = int(input("Enter the Time (Number in Years): "))

A = P * ((1+R/n)**n*T - 1)/(R/n)
print(A)
