first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
roll_no = int(input("enter your roll no. : "))

s1 = int(input("enter marks for subject 1: "))
s2 = int(input("enter marks for subject 2: "))
s3 = int(input("enter marks for subject 3: "))
s4 = int(input("enter marks for subject 4: "))
s5 = int(input("enter marks for subject 5: "))

sum = int(s1+s2+s3+s4+s5)
percentage = (sum / 5)
print("Your percentage is: ", percentage)
if percentage <= 100 and percentage >= 75:
   print("you get A grade !")
elif percentage <= 74 and percentage >= 60:
   print("you get B grade !")
elif percentage <= 59 and percentage >= 40:
   print("you get C grade !")
else:
   print("you are failed !")







   



