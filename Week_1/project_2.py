# Code for calculating Compound Interest
P = int(input("Enter the Principal: "))
R = int(input("Enter the interest rate: "))
T = int(input("Enter the Time (Number of Years): "))
n = int(input("Enter how many times interest is applied per time period"))

A = P * (1 + R/n)**n*T
print("your interest is " + str(A))
