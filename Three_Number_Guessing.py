#usr/bin/env python3
import random

def main():
    print("\t\t ******** Welcome to the Game ******** ")
    print("\t I'm thinking of three digits. Can you guess them?")
    print("\t I'll give some clues for you")
    print("\t Pico   \t One digit is correct but wrong position")
    print("\t Fermi  \t One digit is correct and right position")
    print("\t Bagels \t No digit is correct")
    print("\t Hey!I've thought a number")
    print("\t You have 10 chances to guess....")
    chk_guess()





def chk_guess():
    a=random.randint(100,999)
    rdm=f"{a}"
    # print(a)
    # print(rdm[0])
    max_guess=10
    num_guess=1
    while  True:
        while num_guess<=max_guess:
            for chance in range(1,11):
                print(f"\tGuess #{chance}:")
                c=input("\t> ")
                
                try :
                    if c[0] == rdm[0] and c[1] == rdm[1] and c[2] == rdm[2]:
                        print(f"\tYayy!.You made a correct guess with {chance} chances")
                        return True
                    elif (c[0] == rdm[0] and c[1] == rdm[1]) or (c[0] == rdm[0] and c[2] == rdm[2]) or (c[1] == rdm[1] and c[2] == rdm[2]):
                        print("\tFermi Fermi") 
                    elif (c[0] == rdm[0]) or (c[1] == rdm[1]) or (c[2] == rdm[2]):
                        print("\tFermi") 
                    elif ( c[0] == rdm[1] ) or ( c[0] == rdm[2] ) or ( c[1] == rdm[2] ) :
                        print("\tPico")
                    else:
                        print("\tBagels....Nothing matches and try again")
                except IndexError:
                    print("\tYou didn't follow the rules of the game.\n\tPunishment => You wasted your chance!")
                num_guess += 1
            if max_guess == 10:
                print("You coundn't guess within 10 chances!Try again!")
                print(f"The result is {rdm}")
                break
        break
              

main()



    