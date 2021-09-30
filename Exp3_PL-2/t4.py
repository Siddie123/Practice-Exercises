def countCharacterType(str):
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0

    for i in range(0, len(str)):

        ch = str[i]

        if ((ch >= 'a' and ch <= 'z') or
                (ch >= 'A' and ch <= 'Z')):

            ch = ch.lower()

            if (ch == 'a' or ch == 'e' or ch == 'i'
                    or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

        elif (ch >= '0' and ch <= '9'):
            digit += 1
        else:
            specialChar += 1

    print(f"Vowels: {vowels}")
    print(f"Consonant: {consonant}")
    print(f"Digit: {digit}")
    print(f"Special Character: {specialChar}")


str = "Hello I @m S1d"
countCharacterType(str)




