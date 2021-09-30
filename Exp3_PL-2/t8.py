Veg_Order = []
NonVeg_Order = []
print("Please Select an option")
print("1-Veg Menu")
print("2-Non-Veg Menu")
print("0-Exit")
choice = int(input("Enter your choice:"))
if choice == 0:
   print("Thank you For coming")
   exit()

n = int(input("Enter number of items you will eat:"))
for i in range(1, n + 1):
    if choice == 1:
        print("You have selected option 1-Veg")
        print("Select from the following options for Veg")
        print("1-Veg Burger")
        print("2-Veg Pizza")
        print("3-Dosa")
        VegChoice = int(input("Enter your choice:"))
        if VegChoice == 1:
               Veg_Order.append('Veg-Burger')
               ch = input("Do you wish to continue?[Y/N]:")
               if ch == 'Y' or ch == 'y':
                  continue
               else:
                  break
        elif VegChoice == 2:
               Veg_Order.append('Veg-Pizza')
               ch = input("Do you wish to continue?[Y/N]:")
               if ch == 'Y' or ch == 'y':
                  continue
               else:
                  break

        elif VegChoice == 3:
               Veg_Order.append('Dosa')
               ch = input("Do you wish to continue?[Y/N]:")
               if ch == 'Y' or ch == 'y':
                  continue
               else:
                  break
        print(f"Your order is {Veg_Order} ")


for i in range(1, n+1):
    if choice == 2:
         print("You have selected Option 2 Non-Veg")
         print("Select from the following options for Non-Veg")
         print("1-Chicken Burger")
         print("2-Chicken Pizza")
         print("3-Chicken Nuggets")
         NonVegChoice = int(input("Enter your choice: "))
         if NonVegChoice == 1:
                NonVeg_Order.append('Chicken Burger')
                ch = input("Do you wish to continue?[Y/N]:")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    break
         elif NonVegChoice == 2:
                NonVeg_Order.append('Chicken Pizza')
                ch = input("Do you wish to continue?[Y/N]:")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    break

         elif NonVegChoice == 3:
                NonVeg_Order.append('Chicken Nuggets')
                ch = input("Do you wish to continue?[Y/N]:")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    break
print(f"Your order is {NonVeg_Order} ")
