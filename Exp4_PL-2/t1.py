def is_pangram(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False

	return True

string = input("enter a string: ")
if(is_pangram(string) == True):
	print(f"Yes, the given string: [{string}] is a PANGRAM ")
else:
	print(f"No, the given string: [{string}] is NOT a PANGRAM ")


