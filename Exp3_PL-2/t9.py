import sys
Veg_Order = []
NonVeg_Order = []
Veg_Bill = []
NonVeg_Bill = []
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
      print("1-Veg Burger:110")
      print("2-Veg Pizza:120")
      print("3-Dosa:100")
      VegChoice = int(input("Enter your choice:"))
      if VegChoice == 1:
               Veg_Order.append('Veg-Burger : 110')
               Veg_Bill.append(110)
               ch = input("Do you wish to continue?[Y/N]:")
               if ch == 'Y' or ch == 'y':
                  continue
               else:
                  break
      elif VegChoice == 2:
               Veg_Order.append('Veg-Pizza : 120')
               Veg_Bill.append(120)
               ch = input("Do you wish to continue?[Y/N]:")
               if ch == 'Y' or ch == 'y':
                  continue
               else:
                  break

      elif VegChoice == 3:
               Veg_Order.append('Dosa : 100')
               Veg_Bill.append(100)
               ch = input("Do you wish to continue?[Y/N]:")
               if ch == 'Y' or ch == 'y':
                  continue
               else:
                  break
vegbill = sum(Veg_Bill)

print("Your order is {} ".format(Veg_Order))
print("Your Total Bill is {}".format(vegbill))
if choice == 1:
    sys.exit()

for i in range(1, n+1):

    if choice == 2:
      print("You have selected option 2-Non-Veg")
      print("Select from the following options for Veg")
      print("1-Chicken Burger:110")
      print("2-Chicken Pizza:120")
      print("3-Chicken Nuggets:100")
      NonVegChoice = int(input("Enter your choice: "))
      if NonVegChoice == 1:
                NonVeg_Order.append('Chicken Burger: 110')
                NonVeg_Bill.append(110)
                ch = input("Do you wish to continue?[Y/N]:")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    break
      elif NonVegChoice == 2:
                NonVeg_Order.append('Chicken Pizza : 120')
                NonVeg_Bill.append(120)
                ch = input("Do you wish to continue?[Y/N]:")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    break

      elif NonVegChoice == 3:
                NonVeg_Order.append('Chicken Nuggets : 100')
                NonVeg_Bill.append(100)
                ch = input("Do you wish to continue?[Y/N]:")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    break

nonvegbill = sum(NonVeg_Bill)

print("Your order is {} ".format(NonVeg_Order))
print("Your Total Bill is {}".format(nonvegbill))
if choice == 2:
    sys.exit()
