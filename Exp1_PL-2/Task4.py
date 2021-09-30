days = int(input("enter the number days took to return the book: "))
if days <= 5:
    print("your fine is 50 paisa")
elif days in range(6,11):
    print("your fine is 1 rupees")
elif days in range(10,29):
    print("your fine is 5 rupees")
else:
    print("your membership is cancelled")