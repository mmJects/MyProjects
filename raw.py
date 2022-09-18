# from random import randint      # import random
# # for easy mode , we make random choice for AI

# """
# We use random values for easy ai mode , 
# minimax algorithm for unbeatable ai mode ,
# Minimax algorithm will be explained in algoithms.txt file
# """

# # user's choose function
# def choose(mark,lst):   # ( user's mark , list )
#     chocies_lst = ["1","2","3","4","5","6","7","8","9"]     # These are almost indentical with choose 
#     print(f"\n\t\t ******Player's Turn ({mark})****** ")    # function from other file
#     while True:                                                   
#         choice = input("\n\tPlease enter the location on board(1-9) => ")
#         if choice in chocies_lst:
#             choice = int(choice)
#             if lst[choice-1] == ' ':
#                 lst[choice-1] = mark
#                 return lst
#             elif lst[choice-1] != ' ':
#                 print("\nYour input is occupied..")


# # easy mode for ai
# def ai_ez(lst,mark):              # ( list , mark for ai )
    
#     while True:                   # always looping 
#         a= randint(0,8)           # find random range 1 to 9
#         if lst[a] != " ":         # if random value position is not empty
#             pass                  # do nothing
#         else:                     # if it is not empty
#             lst[a]=mark           # assign that position with ai's mark
#             return lst            # return  modifying list 

# # test function for all available places
# def ai_hd(lst):
#     best = -1000                    # set the initial value to minimize 
#     best_mv = None                  # declare best move
#     for i in range(9):              # for all available places
#         if lst[i] == " ":           # if the place is available
#             lst[i] = player         # assign  that position with player's mark
#             val = find_best(lst,False,0)    # call the minimax algorithm with False boolean which meamsn to maximize
#             lst[i] = " "                    # remove player's mark
#             if val > best:                  # if the value from recursion is greater than the initial value
#                 best_mv =  i                # assign that position as best move for AI
#                 best = val                  # reassing the initial value with the value from recursion
#     return best_mv

# # unbeatable mode for ai
# # find best position for ai to beat player using minmax algorithm
# def find_best(lst,isMax,depth):     # (list,boolean,depth)

#     val = check_winner(lst)         # check winner to check who got terminal state
#     if val == 10:                   # if player wins
#         return val - depth          # return 10 - depth
#     if val == -10:                  # if ai wins
#         return val + depth          # return 10 + depth
#     if " " not in lst:              # if the board is full
#         return 0                    # return 0
#     if isMax:                       # if True boolean condition
#         # set the negative compared value so that nearly every conditions is greater 
#         best = -1000                
#         best_mv = None              # set the best move as none
#         for i in range(9):          # loop through the all states  to find best move     
#             if lst[i] == " ":       # if the position is empty   
#                 lst[i] = player     # set that position with player mark      
#                 # if we've inserted that postion , find the other possibilities 
#                 # by assigning AI mark and return the value => turn minimizing
#                 eval = find_best(lst,not isMax,depth + 1)   # recursion ( lst , False boolean , depth + 1)
#                 lst[i] = " "                                # after recursive , remove player mark in that position 

#                 if eval > best:     # if the value is greater than the compared value ;
#                     best = eval     # assign that value into that compared value
#                     best_mv = i     # set that postion as best_position
#         return best_mv              #  return the best_position
#     else:                           # if False boolean condition
#         # set the postitive compared value so that nearly every conditions is greater 
#         best = 1000                 
#         best_mv = None              # set the best move as none
#         for i in range(9):          # loop through the all states  to find best move  
#             if lst[i] == " ":       # if the position is empty
#                 lst[i] = ai         # set that position with ai mark
#                 # if we've inserted that postion , find the other possibilities 
#                 # by assigning AI mark and return the value => turn maximizing
#                 eval = find_best(lst,isMax,depth+1)      # recursion ( lst , True boolean , depth + 1) 
#                 lst[i] = " "                             # after recursive , remove player mark in that position 
#                 if eval < best:                          # if the value is greater than the compared value ;              
#                         best = eval                      # assign that value into that compared value
#                         best_mv = i                      # set that postion as best_position
#         return best_mv                                   # if False boolean condition
# """
# You can't understand above function without understanding minmax algorithm.
# So, first learn the logic of the minimax and I will also explain as much as I can
# """


# #updating the board with input
# def update_display(lst):
#     print(f"\t\t\t   {lst[0]}  |  {lst[1]}  |  {lst[2]}  ")
#     print( "\t\t\t -----|-----|----- ")
#     print(f"\t\t\t   {lst[3]}  |  {lst[4]}  |  {lst[5]}  ")
#     print( "\t\t\t -----|-----|----- ")
#     print(f"\t\t\t   {lst[6]}  |  {lst[7]}  |  {lst[8]}  ")

# #check winner
# def check_winner(lst):                      # check winner function ( list )
#     # horizontal check
#     for i in range(0,7,3):
#         if (lst[i]==lst[i+1]==lst[i+2]):
#             if lst[i] == player:            # retrun 10 if player wins
#                 return 10
#             elif lst[i] == ai:              # return -10 if computer wins
#                 return -10
#     # vertical check
#     for i in range(3):
#         if (lst[i]==lst[i+3]==lst[i+6]):
#             if lst[i] == player:
#                 return 10
#             elif lst[i] == ai:
#                 return -10
#     # first diagonal check
#     if (lst[0]==lst[4]==lst[8]) :
#         if lst[0] == player:
#             return 10
#         elif lst[0] == ai:
#             return -10
#     # second diagonal check
#     elif (lst[2] == lst[4] == lst[6]):
#         if lst[4] == player:
#             return 10
#         elif lst[4] == ai:
#             return -10
#     return 0

# # driver function or main function
# def main(mark_p,mark_c,choice):                 # main function ( player mark , ai mark , mode choices 1 or 2)
#     global player                               # make global variable player
#     player = mark_p                             # assign player with player's mark
#     global ai
#     ai = mark_c
#     lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']   # fist list will be empty
#     if choice == 1:                             # if user choose 1 (easy ai mode)
#         while ' '  in lst :                     # always loop if board is empty
#             lst=choose(mark_p,lst)              # choose function for user's choices 
#             update_display(lst)                 # update and displaying the list
#             w = check_winner(lst)               # check winner 
#             if w == 10:                         # if user wins 
#                 print(f"\n\t\tYayy...Player({player}) win the game\n\n")
#                 break                           # break loop
            
#             print("\n")
#             if ' ' in lst:                      # if the board is not empty
#                 lst=ai_ez(lst,mark_c)           # let ai choose random value
#                 update_display(lst)             # update and displaying the list
#                 w = check_winner(lst)           # check winner 
#                 if w == -10 :                   # if ai wins 
#                     print(f"\n\t\tOugh!!!Sorry Ai({ai}) win the game\n\n")
#                     break                       # break the loop 
#             else:                               # if the board is empty
#                 print(f"\n\t\t ********Match Draw.... ********")
#     else:                                       # if user choose unbeatable ai mode
#         while " " in lst:                       # always loop if board is empty
#             lst = choose(mark_p,lst)            # choose function for user's choices       
#             update_display(lst)                 # update and displaying the list
#             w = check_winner(lst)               # check winner 
#             if w == 10:                         # if user wins
#                 print(f"\n\t\tYayy...Player({player}) win the game\n\n")
#                 break

#             print("\n")
#             if ' ' in lst:                      # if the board is not empty
#                 pos = ai_hd(lst)                # use find_best function to get the best position
#                 lst[pos] = ai                   # assign the the best position with AI's mark
#                 update_display(lst)             # update and displaying the list
#                 w = check_winner(lst)           # check winner 
#                 if w == -10:                    # if ai wins
#                     print(f"\n\t\tOugh!!!Sorry Ai({ai}) won the game\n\n")
#                     break   
#             # else:                               # if the board is empty
#             #     print(f"\n\t\t ********Match Draw.... ********")   
        

# if __name__ == '__main__':
#     main()                  # driver code for main function
       
# from random import randint      # import random
# # for easy mode , we make random choice for AI

# """
# We use random values for easy ai mode , 
# minimax algorithm for unbeatable ai mode ,
# Minimax algorithm will be explained in algoithms.txt file
# """

# # user's choose function
# def choose(mark,lst):   # ( user's mark , list )
#     chocies_lst = ["1","2","3","4","5","6","7","8","9"]     # These are almost indentical with choose 
#     print(f"\n\t\t ******Player's Turn ({mark})****** ")    # function from other file
#     while True:                                                   
#         choice = input("\n\tPlease enter the location on board(1-9) => ")
#         if choice in chocies_lst:
#             choice = int(choice)
#             if lst[choice-1] == ' ':
#                 lst[choice-1] = mark
#                 return lst
#             elif lst[choice-1] != ' ':
#                 print("\nYour input is occupied..")


# # easy mode for ai
# def ai_ez(lst,mark):              # ( list , mark for ai )
    
#     while True:                   # always looping 
#         a= randint(0,8)           # find random range 1 to 9
#         if lst[a] != " ":         # if random value position is not empty
#             pass                  # do nothing
#         else:                     # if it is not empty
#             lst[a]=mark           # assign that position with ai's mark
#             return lst            # return  modifying list 

# # unbeatable mode for ai
# # find best position for ai to beat player using minmax algorithm
# def find_best(lst,isMax,depth):

#     val = check_winner(lst)
#     if val == 10:
#         return val - depth
#     if val == -10:
#         return val + depth
#     if " " not in lst:
#         return 0
#     if isMax:
#         best = -1000
#         best_mv = None
#         for i in range(9):
#             if lst[i] == " ":
#                 lst[i] = player
#                 eval = find_best(lst,not isMax,depth + 1)
#                 lst[i] = " "
#                 if eval > best:
#                     best = eval
#                     best_mv = i 
#         return best_mv
#     else:
#         best = 1000
#         best_mv = None
#         for i in range(9):
#             if lst[i] == " ":
#                 lst[i] = ai
#                 eval = find_best(lst,isMax,depth+1)
#                 lst[i] = " "
#                 if eval < best:
#                     best = eval
#                     best_mv = i 
#         return best_mv

# # find best moves for opponent
# def ai_hd(lst):
#     best = -1000
#     best_mv = None
#     for i in range(9):
#         if lst[i] == " ":
#             lst[i] = player
#             val = find_best(lst,False,0)
#             lst[i] = " "
#             if val > best:
#                 best_mv =  i
#                 best = val
#     return best_mv


# #updating the board with input
# def update_display(lst):
#     print(f"\t\t\t   {lst[0]}  |  {lst[1]}  |  {lst[2]}  ")
#     print( "\t\t\t -----|-----|----- ")
#     print(f"\t\t\t   {lst[3]}  |  {lst[4]}  |  {lst[5]}  ")
#     print( "\t\t\t -----|-----|----- ")
#     print(f"\t\t\t   {lst[6]}  |  {lst[7]}  |  {lst[8]}  ")

# #check winner
# def check_winner(lst):                      # check winner function ( list )
#     # horizontal check
#     for i in range(0,7,3):
#         if (lst[i]==lst[i+1]==lst[i+2]):
#             if lst[i] == player:            # retrun 10 if player wins
#                 return 10
#             elif lst[i] == ai:              # return -10 if computer wins
#                 return -10
#     # vertical check
#     for i in range(3):
#         if (lst[i]==lst[i+3]==lst[i+6]):
#             if lst[i] == player:
#                 return 10
#             elif lst[i] == ai:
#                 return -10
#     # first diagonal check
#     if (lst[0]==lst[4]==lst[8]) :
#         if lst[0] == player:
#             return 10
#         elif lst[0] == ai:
#             return -10
#     # second diagonal check
#     if (lst[2] == lst[4] == lst[6]):
#         if lst[4] == player:
#             return 10
#         elif lst[4] == ai:
#             return -10

#     return 0

# # driver function or main function
# def main(mark_p,mark_c,choice):                 # main function ( player mark , ai mark , mode choices 1 or 2)
#     global player                               # make global variable player
#     player = mark_p                             # assign player with player's mark
#     global ai
#     ai = mark_c
#     lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']   # fist list will be empty
#     if choice == 1:                             # if user choose 1 (easy ai mode)
#         while ' '  in lst :                     # always loop if board is empty
#             lst=choose(mark_p,lst)              # choose function for user's choices 
#             update_display(lst)                 # update and displaying the list
#             w = check_winner(lst)               # check winner 
#             if w == 10:                         # if user wins 
#                 print(f"\n\t\tYayy...Player({player}) win the game\n\n")
#                 break                           # break loop
            
#             print("\n")
#             if ' ' in lst:                      # if the board is not empty
#                 lst=ai_ez(lst,mark_c)           # let ai choose random value
#                 update_display(lst)             # update and displaying the list
#                 w = check_winner(lst)           # check winner 
#                 if w == -10 :                   # if ai wins 
#                     print(f"\n\t\tOugh!!!Sorry Ai({ai}) win the game\n\n")
#                     break                       # break the loop 
#             else:                               # if the board is empty
#                 print(f"\t\t ********Match Draw.... ********")
#     else:                                       # if user choose unbeatable ai mode
#         while " " in lst:                       # always loop if board is empty
#             lst = choose(mark_p,lst)            # choose function for user's choices       
          
#             w = check_winner(lst)               # check winner 
#             update_display(lst)                 # update and displaying the list
#             if w == 10:                         # if user wins
#                 print(f"\n\t\tYayy...Player({player}) win the game\n\n")
#                 break

#             print("\n")
#             if ' ' in lst:                      # if the board is not empty
#                 pos = ai_hd(lst)    # use find_best function to get the best position
#                 lst[pos] = ai                   # assign the the best position with AI's mark
           
#                 w = check_winner(lst)           # check winner 
#                 update_display(lst)             # update and displaying the list
#                 if w == -10:                    # if ai wins
#                     print(f"\n\t\tOugh!!!Sorry Ai({ai}) won the game\n\n")
#                     break      
        

# if __name__ == '__main__':
#     main()                  # driver code for main function     


