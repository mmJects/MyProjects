import cs50     # importing the cs50 library to ask integer

print("\t\t The Great Caesar Cipher - Encrypted or Decrypted Machine ") # Description message

choice = "invalid"                          # just variable to go in condition
modes = {"e":"Encrypted","d":"Decrypted"}   # dictionary to check user's choice

while True:
    if choice not in ["e","d"]:         # since the initalized choice variable is not "e" or "d"
        choice = input("Would you like to (e) encrypt or (d) decrypt?? ").lower()   # ask user for the input
        if choice not in ["e","d"]:     # if the user's input is not "e" or "d"
            continue                    # restart the loop
        mode = choice                   # assign the choice into mode
    key = cs50.get_int("Pleae enter the shfiting key (0-25) to use : ")     # get the shifting key to crypting
    # We need to limit the key , if not the output will not be alphabets
    if 0 < key < 26:            # if the key is range 0 to 25
        break                   # break

line = input("Enter text : ")   # asking user for the crypted text

result = """"""               # initializing the variable to output the target

for char in line:               # loop through the each character of line
    asci = ord(char.upper())    # get the ascii value of character
    if mode == "e":             # if the mode is encryption
        crypted = asci + key    # shift right the ascii value with user's key
        # if the ascii values are greater than the 90 : which means the output will be other characters ( not alphabets )
        if crypted > 90:        
            extra =crypted - 90     # getting the exceeded value 
            crypted = 64 + extra    # add the exceeded value with the first alphabet ( A )

    elif mode == "d":               # if the mode is decryption
        crypted = asci - key        # shift left the ascii value with user's key
        # if the ascii values are less than the 65 : which means the output will be other characters ( not alphabets )
        if crypted < 65 :           
            extra = 65 -crypted     # getting the exceeded value
            crypted = 91 - extra    # add the exceeded value with the first alphabet ( A )

    if 65 <= crypted <= 90:             # if the output ascii values are alphabets
        if char == char.upper():        # if user's input character is uppercase
            result += chr(crypted)      # change the ascii value to the character and adding the result 
        else:                           # if user's input character is lowercase
            result += chr(crypted).lower()  # change the ascii value to the character with lowercase and adding 
    else:   
        result += " "

print(f"Your {modes[mode]} text is:",result)    # Output for user
