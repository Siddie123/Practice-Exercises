elements = []
num_of_elements = int(input("Enter number of elements: "))
for i in range(1, num_of_elements+1):
    n = int(input("Enter element: "))
    elements.append(n)
even = []
odd = []
for j in elements:
    if(j % 2 == 0):
        even.append(j)
    else:
        odd.append(j)
print("The even list", even)
print("The odd list", odd)

