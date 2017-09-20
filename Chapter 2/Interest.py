p = 10000
n = 12
r = 0.08
t = int(input("years? "))

A = p * (1 + r/n) ** (n*t)

print("Your final amount is: ",A)