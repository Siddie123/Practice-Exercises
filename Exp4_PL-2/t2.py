import itertools

values = input(f"enter the values for the set: ")

per = itertools.permutations(values, 2)

print(f"These are the following permutations of the given set [{values}]: ")

for val in per:
    print(val)
    

