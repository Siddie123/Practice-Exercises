p = float((input("enter the principle amount: ")))
t = float((input("enter the time period: ")))
r = float((input("enter the rate of interest: ")))

compound_interest = p * (pow((1 + r / 100), t))
print("")
print("principle = ", p)
print("rate of interest = ", r)
print("time = ", t)
print("Compound Interest = ", compound_interest)  


