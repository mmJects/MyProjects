# users/bin/env python3

import re                               # to limit user's input with regex          
from termcolor import colored           # to add colored texts        

res = "quick"                           # an english word to guess

lst = [                                 # to store user's letter in 2D array
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
                                ]

def game_intro():                       # Game intro
    print("\t\t\t***Welcome to Wordle Game***\n")
    chk = "k"
    while not chk in ["y","n"]:                                   # always looping if ther user's input is not Y or N
        chk = input("\t\tWanna know the rules(y/n): ").lower()    # ask the users for Y / N
    if chk == 'y':                                                # if the user wants to know rules
        with open("C:\\Programming\\Python\\Projects_docs\\wordle_docs.txt",mode="r+") as f:# read file from my docs
            lines = f.readlines()                                 # read the lines and store in a list
            for i in lines:                                       # loop throung the list
                print(f"{i}",end="")                              # and print out line by line
        
 

def draw_table(l):                      # draw table for user inteface
    print( "\t\t===============================")   
    print(f"\t\t|  {l[0][0]}  |  {l[0][1]}  |  {l[0][2]}  |  {l[0][3]}  |  {l[0][4]}  |")
    print( "\t\t===============================")   
    print(f"\t\t|  {l[1][0]}  |  {l[1][1]}  |  {l[1][2]}  |  {l[1][3]}  |  {l[1][4]}  |")
    print( "\t\t===============================")   
    print(f"\t\t|  {l[2][0]}  |  {l[2][1]}  |  {l[2][2]}  |  {l[2][3]}  |  {l[2][4]}  |")
    print( "\t\t===============================")   
    print(f"\t\t|  {l[3][0]}  |  {l[3][1]}  |  {l[3][2]}  |  {l[3][3]}  |  {l[3][4]}  |")
    print( "\t\t===============================")   
    print(f"\t\t|  {l[4][0]}  |  {l[4][1]}  |  {l[4][2]}  |  {l[4][3]}  |  {l[4][4]}  |")
    print( "\t\t===============================")   
    print(f"\t\t|  {l[5][0]}  |  {l[5][1]}  |  {l[5][2]}  |  {l[5][3]}  |  {l[5][4]}  |")
    print( "\t\t===============================\n")

draw_table(lst)                     # firstly show user about the table

def game_logic(res,lst):            # game logic takes ( target word , user's guesses )
    for i in range(6):              # As a 6 rows , we take 6 loops for user's guess
        while True:                 # use while loop to check user's input
            inp = input("Enter 5 letter word :  ")  # user's input
            if re.search("[a-z][a-z][a-z][a-z][a-z]",inp) and len(inp) == 5:    # if user's input has 5 letters
                break                                                           # break the loop
            print("\t******Only input 5 letters ( A to Z )******")                # warning for invalid input
        inp_lst = list(map(str,inp))                           # make a user's guess list to reassign
        for j in range(5):                                     # use five looping to check user's characters
            if inp_lst[j] == res[j]:                           # if user input same letter and position
                inp_lst[j] = colored(inp_lst[j],"green")       # color the word with green
            elif inp[j] in res:                                # if user input has the same letter
                inp_lst[j] = colored(inp_lst[j],"yellow")      # color that letter with yellow
            lst[i][j] = inp_lst[j]                             # insert user's letter into list
        draw_table(lst)                                        # show graph with the user's inputs and informations
        if inp == res:                                      # if user's input is exactly with target :
            print("\tYayy...Your guess is a correct word..")  # show information and 
            break                                           # break the loop
        if i == 5:                                          # if the attempts are failed 
            print("\tSorry you failed the game.")             # print the game losing errors

if __name__ == '__main__':
    game_intro()
    draw_table(lst)
    game_logic(res,lst)