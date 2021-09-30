num = int(input("enter the no. of coins: "))
row = 1
coin_total = 1
while (coin_total + row) < num:
   row += 1
   coin_total += row
print(f"The max height that can be obtained with {num} is {row} ")