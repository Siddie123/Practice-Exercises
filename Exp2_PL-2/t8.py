tc = int(input("Enter the no. of test cases: "))

for i in range(tc):
    a = input()
    b = int(a[0])+int(a[-1])
    print(f"the sum of the first and the last is {b} ")
