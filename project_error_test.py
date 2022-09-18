
# unbeatable mode for ai
def find_best(lst,isMax,depth):

    val = check_winner(lst)
    if val == 10:
        return val - depth
    if val == -10:
        return val + depth
    if (check_space(lst) == False):
        return 0
    if isMax:
        best = -1000
        move = None
        for i in range(9):
            if lst[i] == " ":
                lst[i] = player
                best_val = find_best(lst,not isMax,depth + 1)
                lst[i] = " "
                if best_val > best:
                    best = best_val
                    move = i
        return move 
    else:
        best = 1000
        move = None
        for i in range(9):
            if lst[i] == " ":
                lst[i] = ai
                best_val = find_best(lst,isMax,depth+1)
                lst[i] = " "
                if best_val < best:
                    best = best_val
                    move = i
        return move 

# find best moves for opponent
# def ai_hd(lst):
#     best = -1000
#     best_mv = -1
#     for i in range(9):
#         if lst[i] == " ":
#             lst[i] = player
#             val = find_best(lst,False,0)
#             lst[i] = " "
#             if val > best:
#                 best_mv =  i
#                 best = val
#     return best_mv

#Check empty space
def check_space(lst):
    for i in lst:
        if i == " ":
            return True
    return False

#updating the board with input
def update_display(lst):
    print(f"\t\t\t   {lst[0]}  |  {lst[1]}  |  {lst[2]}  ")
    print( "\t\t\t -----|-----|----- ")
    print(f"\t\t\t   {lst[3]}  |  {lst[4]}  |  {lst[5]}  ")
    print( "\t\t\t -----|-----|----- ")
    print(f"\t\t\t   {lst[6]}  |  {lst[7]}  |  {lst[8]}  ")

#check winner
def check_winner(lst):
    for i in range(0,7,3):
        if (lst[i]==lst[i+1]==lst[i+2]):
            if lst[i] == player:
                return 10
            elif lst[i] == ai:
                return -10
    for i in range(3):
        if (lst[i]==lst[i+3]==lst[i+6]):
            if lst[i] == player:
                return 10
            elif lst[i] == ai:
                return -10
    
    if (lst[0]==lst[4]==lst[8]) :
        if lst[0] == player:
            return 10
        elif lst[0] == ai:
            return -10

    elif (lst[2] == lst[4] == lst[6]):
        if lst[4] == player:
            return 10
        elif lst[4] == ai:
            return -10
    return 0 

def main():
    global player
    player = 'X'
    global ai
    ai = 'O'
    lst = ['X',' ',' ',' ','O',' ','O',' ',' ']
    val = find_best(lst,False,0)
    print(val)
    lst[val] = ai
    print(lst)
main()

