P = int(input("Enter the Principal"))
R = int(input("Enter the interest rate"))
T = int(input("Enter the time (Number of Years)"))

A = P * (1 + (R/100)*T)
print(f"your interest is {A}")
