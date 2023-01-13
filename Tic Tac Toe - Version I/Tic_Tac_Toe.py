#!usr/bin/env Python3
#Tic Tac Toe Project 
#Developed by Yun Yun

"""                        Guidelines
=>First you will have to make two choices ( 1 - With Friend , 2 - With Computer)
=>=>If you choose friend mode , player 1 set its signs ( O / X ) and for the player computer will automatically 
choose. And you have to choose locations on the board and compete with your opponent.
=>=>If you choose computer mode, you will make  two choices again ( 1 - easy AI , 2 - unbeatable AI )
=>=>=> If you choose easy compute mode , you will choose your marks and computer will choose the other mark.
       In  easy mode , you will have 99.9 % chance to beat computer if  you play optimally. if not 95%..
=>=>=> First choose your marks..
       With unbeatable mode , you will only have 0.01% chance by optimal moves.
            ********Winning Conditions will display in readme.txt file.*********
"""

#Since we've made a lot of functioons and complex connetions , we 've to combine two files

import Tic_Tac_Toe_AI as fun       # import the Tic_Tac_Toe_AI python code from other files

# displaying Information
def intro():

    print("\a\t\t\t\tWelcome to the Tic Tac Toe game..")                # Game Intro
    print("\n\tIf you can make three of your marks in a horizontal , vertical , or diagonal row , you are the winner(yayy..!)")
    print("\n\t\tYou can play with => your friend (choice 1) or => AI (choice 2).....")
    print("\n\t\t\tAre you ready to conquer in the universe of Tic Tac Toe???\n")

    print("\t\t\t____|____|____  \t 1 , 2 , 3")                         # Game display
    print("\t\t\t____|____|____  \t 4 , 5 , 6")
    print("\t\t\t    |    |      \t 7 , 8 , 9")

    mark=''
    mode_lst = ["1","2"]

    while True:                                      # Not to choose except 1 or 2
        mode = input("\n\t\tWith Friend(choice 1) or With AI(choice 2) :  ")     # Request user user choice
        if mode in mode_lst:
            mode = int(mode)
            if mode == 1:                                                   # if user choose friend mode

                print("\n\t\t\tWelcome to the Player Versus Player Match....")
                print("\n\t\t**********Player 1 Versus Player 2**********")
                while mark not in ['X','O']:                                # Not to choose marks except X or O
                    mark = input("\n\t\tPlayer 1's mark(O/X) => ")          # ask player 1 to choose mark
                # if user choode player mode , program will return back signs ( X or O )
                return mark                                                 # return user's choice

            elif mode == 2:                                                 # if the user choose computer mode

                print("\n\t\tYou are facing with AI .Go Ahead...")
                print("\n\t********  Human  Player => Versus <= Artifical Intelligence  ********")
                a_mode = 0

                while a_mode != "1" and a_mode  != "2":                         # Not choose modes except 1 and 2
                    a_mode = input("\n\t\tEasy Mode (1) or Impossible Mode (2) =>  ")  # ask computer's mode
                # if user choose computer mode , program will return back integers (1 or 2)
                return int(a_mode)   # reutun user's mode
                
            else:       # if the user choose except 1 or 2 ;
                print("\n\t\tWrong mode..Remake the choice...")
            
#displaying player's mark       
def appch(sth):     # for player mode 
    
    if sth == 'O':
        print("\n\t\t **** Player 1 (O) Vs Player 2 (X) ***")      # if player 1 choose O , 
        return 'X'                                                 # return X for player 2
    elif sth == 'X':
        print("\n\t\t **** Player 1 (X) Vs Player 2 (O) ***")       # if player 2 choose X ,
        return 'O'                                                  #  return O for player 2
    else:
        print("\n\n\t\tWrong input!!!!!!")


#intro for AI          
def appch_ai(sth,sth1):     # for computer mode (user's condtion , user's choce )
    mark = 'X' if sth1=='O' else 'O'
    if sth == 1:
        print(f"\n\t\t **** Human Player ({sth1}  Vs Easy AI ({mark})  ***")    # display mark & condition level
        return mark
    elif sth == 2:
        print(f"\n\t\t **** Human Player ({sth1})  Vs Unbeatable AI ({mark}) ***")
        return mark
        
    

#requesting player's input
def choose(mark,lst,ply):
    chocies_lst = ["1","2","3","4","5","6","7","8","9"]     # to check user's inputs
    print(f"\n\t\t ******Player{ply}'s Turn : ({mark}) ******  ")
    while True :                                            # always loop until break
        choice = input("\n\tPlease enter the location on board(1-9) => ")

        if choice in chocies_lst:                       # if user only choose 1 to 9
            choice = int(choice)                        
            if lst[choice-1] == ' ':   # if user's input is empth     # subtract one from user choice
                lst[choice-1] = mark   # assign mark in user's choice # beacuse board range is 0 to 8
            elif lst[choice-1] != ' ': # if user's mark is not empty 
                print("\nYour input is occupied..") # warn user
                choice = 0
            break       # break the always looping beaucse of correct choice

    return lst          # return modified list 


#updating the board with input
def update_display(lst):        # update display with the modified list
    print(f"\t\t\t   {lst[0]}  |  {lst[1]}  |  {lst[2]}  ")
    print( "\t\t\t -----|-----|----- ")
    print(f"\t\t\t   {lst[3]}  |  {lst[4]}  |  {lst[5]}  ")
    print( "\t\t\t -----|-----|----- ")
    print(f"\t\t\t   {lst[6]}  |  {lst[7]}  |  {lst[8]}  ")
 

#check winner
def check_winner(lst,ply,mark):             # chceck winner ( list , player , player's mark)
    # horizontal check
    if (lst[0]==lst[1]==lst[2]==mark) or (lst[3]==lst[4]==lst[5]==mark) or (lst[6]==lst[7]==lst[8]==mark):
        print(f"\n\t\tYayy...Player {ply} win the game...\n\n")
        return 1                # return 1 if someone wins
    # diagonals check
    elif (lst[0]==lst[4]==lst[8]==mark) or (lst[2]==lst[4]==lst[6]==mark):
        print(f"\n\t\tYayy...Player {ply} win the game...\n\n")
        return 1
    # verical check
    elif (lst[0]==lst[3]==lst[6]==mark) or (lst[2]==lst[5]==lst[8]==mark) or (lst[1]==lst[4]==lst[7]==mark):
        print(f"\n\t\tYayy...Player {ply} win the game...\n\n")
        return 1
    elif ' ' not in lst:    # if the board is full
        print("\n\t\t\t ******* Match Tie... *******")

# Driver function 
#main function
def main():     
    x=intro()   # use information ful will get usr's choice ( X or O or 1 or 2 )
    mark_p=""
    if x == 1 or x == 2 :   # if user's choose computer modes
        while mark_p not in ['X','O']:      # to choose only X or O
                mark_p = input("\n\t\tPlayer 1's mark(O/X) => ")
        mark_c=appch_ai(x,mark_p)       # Ai and Player condition function 
        fun.main(mark_p , mark_c,x)     # Go Tic Tac Toe Ai python file
        
    else:               # if user choose marks 
        
        y=appch(x)      # information function of two player mode
        lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']   # list will be empty at first
        i=0                                         # i is to count how much two player make places
        while ' '  in lst and i < 9:
            mark = x if (i%2) == 0 else y           # mark will change each loop
            ply= 1 if (i%2) == 0 else 2             # player type will change each loop
            
            lst=choose(mark,lst,ply)                # choose function to let user choose 
            update_display(lst)                     # update display after each player chose positions
            chk =check_winner(lst,ply,mark)         # check winner after updating the list
            if chk== 1: break                       # if some one wins break the loop
            i += 1                                  # increase i 
    

if __name__ == '__main__' :
    main()                                          # driver code
    
