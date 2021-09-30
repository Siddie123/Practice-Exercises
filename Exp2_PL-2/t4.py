a1 = int(input("enter the side 1 of the triangle: "))
a2 = int(input("enter the side 2 of the triangle: "))
a3 = int(input("enter the side 3 of the triangle: "))

if a1 == a2 and a2 == a3:
   print("it's a equilateral triangle")
elif a1 == a2 or a2 == a3 or a3 == a1:
   print("it's a isosceles triangle")
else:
   print("it's a scalene triangle")