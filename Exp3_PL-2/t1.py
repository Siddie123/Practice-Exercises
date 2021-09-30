username_password = []
while True:
   username = input("enter the username: ")
   username_password.append(username)
   password = input("enter the password: ")
   username_password.append(password)
   ch = input("do you want to continue ? [yes/no]: ")
   if ch == 'y' or ch == 'Y':
      continue
   else:
      break

print(username_password)
