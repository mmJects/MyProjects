#usr/bin/env Python3
from secrets import choice
import colorama
import random 
import time
from termcolor import colored
colorama.init(autoreset=True)


def table(i):
    lst = [' up  ',' down','right',' left','     ','     ']
    rdm = random.choice(lst)
    print( "\t\t\t====================")
    print(f"\t\t\t။။။     {rdm}    ။။။")
    print("\t\t\t။။။              ။။။")
    print(f"\t\t\t။။။              ။။။")
    print("\t\t\t။။။              ။။။")
    print(f"\t\t\t။။။              ။။။")
    print( "\t\t\t===================")
    return 'rdm'
    
def intro():
    print("\t\t\t ******** Welcome to Truth or Lie Game ********")
    print("\t\t Note: Don't trust the texts!!!!!!!!!!")
    gm = int(input("\t\tGuesses made : "))
    for i in range(gm):
        x = random.randint(1,4)
        result = table(x)
        guess = input("\t\tReal location:  ")
        if result == guess:
            print("\t\t\tCorrect...")
        else:
            print("\t\t\ttry again!")

intro()

