import string

symbs = string.ascii_lowercase

print("Note : We are decrypting the alphabets only , so we can't decrypt for the other characters")
txt = input("Enter the text you want to decrypt : ")
for key in range(26):
    decrypted = ""
    for i in txt:
        char = i.lower()
        try:
            if char in symbs:
                origin_index = symbs.index(char)
                decrypted_char = symbs[origin_index - key]
            else:
                decrypted_char = char
        except:
            idx = key - origin_index
            decrypted_char = symbs[25 - idx]
        decrypted_char = decrypted_char if char == i else decrypted_char.swapcase()
        decrypted += decrypted_char
    print(f"The decrypted text by key {key:<2}  is ",decrypted)