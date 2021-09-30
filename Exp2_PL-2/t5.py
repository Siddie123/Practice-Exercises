
ch = input("Enter any character : ")

if ch[0].isalpha():
    print("\n" + ch[0], "is a ALPHABET.")
elif ch[0].isdigit():
    print("\n" + ch[0], "is a DIGIT.")
else:
    print("\n" + ch[0], "is a SPECIAL CHARACTER.")
