#!usr/bin/env Python3
from random import randint

rdm = randint(0,101) # for collectiong random random
print("\t\t This is Guessing Number ( 1 - 100 ) Game Challenge")
print("\t\t **************************************************")
print("\t If your guess is within 10 of the number , it will show *Warm* ")
print("\t **************************************************************")
print("\t If your guess is further 10 of the number , it will show *Cold* ")
print("\t ***************************************************************")
guess = 0
gus_lst = []
result = 0
z = 0
while result != 1:
    num = int(input("What's your guess number ? : "))
    gus_lst.append(num)
    if num < 1 or num > 100:
        print("Out of bounds")
    elif num == rdm:
        result = 1
    elif num < rdm and num > (rdm - 11) and num > z and z != 0:
        print("Warmer")
    elif num > rdm and num < (rdm + 11) and num < z and z != 0:
        print("Colder")   
    elif num < rdm and num > (rdm - 11):
        print("Warm")
    elif num > rdm and num < (rdm + 11):
        print("Cold")
    else:
        print("Your guess is wrong!")
    guess += 1
    z = num
print()
print("\t *****  To win the game , you guessed %d times  *****"%(guess))
print(f"\t *****  Your guesses are {gus_lst}  *****")