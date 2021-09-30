example = "apple", "orange", "banana", "berry", "mango"
print(example[1:3])
print(example[0:2:3])
print(example[-2])
print(example[1])
print(example[2:])

example2 = "apple", "orange", "banana", ["berry", "mango"]
example2[3][0] = "Pear"
print(example2)

Months = {"Jan", "Feb", "Mar"}
print(Months)

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

for d in Days:
    print(d)

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])

Days.add("Sun")
print(Days)

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])

Days.discard("Sun")
print(Days)
