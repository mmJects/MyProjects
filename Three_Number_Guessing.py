# usr/bin/env python3
# THree Number Guessing by Yun Yun
import random

def main():                         # driver function
    print("\t\t ******** Welcome to the Game ******** ")
    print("\t I'm thinking of three digits. Can you guess them?")
    print("\t I'll give some clues for you")
    print("\t Pico   \t One digit is correct but wrong position")
    print("\t Fermi  \t One digit is correct and right position")
    print("\t Bagels \t No digit is correct")
    print("\t Hey!I've thought a number")
    print("\t You have 10 chances to guess....")
    chk_guess()                     # invoke check_user's guess function

def chk_guess():                    # to check user'g guess function
    a=random.randint(100,999)       # make a random value of 100 to 999 - three digit numbers
    rdm=str(a)                      # change the random value to string so that we can make slices
    # print(a)
    # print(rdm[0])              
    vld = list(map(str,range(10)))  # a list containing 0 to 9 to validate user's input
    for chance in range(1,11):      # As there are 10 chances , loop 10 times
        print(f"\tGuess #{chance}:")    # Display guess times
        while True:                     # always looping for validating user's input
            c = input("\t> ")           # ask user's input
            if len(c) == 3:             # if the user input 3 digits or letters
                if c[0] in vld and c[1] in vld and c[2] in vld : # if user input exactly digits
                    break                   # break the always looping 
            print("\tOnly input 3 digits")  # to display if the user didn't input 3 digits
        # check the stages 
        if c[0] == rdm[0] and c[1] == rdm[1] and c[2] == rdm[2]:    # if 3 digits are correct
            print(f"\tYayy!.You made a correct guess with {chance} chances")
            break                                                   # break the loop
        elif (c[0] == rdm[0] and c[1] == rdm[1]) or (c[0] == rdm[0] and c[2] == rdm[2]) or (c[1] == rdm[1] and c[2] == rdm[2]):
        # if 2 digits are in right places   
            print("\tFermi Fermi") 
        elif (c[0] == rdm[0]) or (c[1] == rdm[1]) or (c[2] == rdm[2]):
        # if 1 digits is in right place
            print("\tFermi") 
        elif ( c[0] == rdm[1] ) or ( c[0] == rdm[2] ) or ( c[1] == rdm[2] ):
        # if 1 digit is in right but not the correct position
            print("\tPico")
        else:       # if not completely same
            print("\tBagels....Nothing matches and try again")
            print(f"\tYou only left {10-chance} chances to guess..")
    else:           # if the user spent 10 chances
        print("\tYou coundn't guess within 10 chances!Try again!")
        print(f"\tThe result is {rdm}")   
# driver code
if __name__ == "__main__":
    main()      # invoke main function