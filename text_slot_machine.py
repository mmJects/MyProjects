"""
Disclaimer : I'm not supporting gambling and betting services. This project is not inferred
to those illegal services. The purpose of this project is to examine my coding skills .
Diffifulty : easy => Simple and easy syntaxes are used for this project.
Outlined by Tech with tim ( https://www.youtube.com/watch?v=th4OBktqK1I&t=8s )
Coded by Yun Yun.
"""
"""
Note : As this is an testing skills projects, I used all kinds of logic as much s I can.
For example : I use different syntaxes for the user's input validation.
"""

import random   # to choose random values

# Machine class including methods like a real machine
class Machine:              # I used machine object to make things together
    ROWS = 3                # rows of a machine
    COLUMNS = 3             # cols of a machine
    MAX_LINES = 3           # betting lines of a machine
    COLUMN = None           # this is just a class variable to store the list of random value
    symbols_count = {       # a dictionary to create random values and theri rare amounts
        "A":2,              # the lesser the value , the more difficult to find 
        "B":4,
        "C":6,
        "D":8
    }
    symbols_value = {       # a rare state dictionay to multiple the betting amount if bingo
        "A":5,              # In opposite, multipling the betting amount will higher for rare elements
        "B":4,
        "C":3,
        "D":2
    }
    def __init__(self,lines=0):     # instantiaion function , setting default value for flexible
        self.lines = lines          # for now, it take user's betting lines

    def ask_lines(self,):           # ask the user how many lines to bet on
        print("Enter the number of lines to bet on ( 1 - " + str(self.MAX_LINES) +" ) ")   # ask user
        while True:             # this is a forever loop while the user put invalid values
            lines = input("? ")
            try:
                lines = int(lines)  # typecast user's input to integers
            except:                 # if the user din't input numbers
                print("You need to add valid lines range of 1 to 3")    
            else:                   # if no error occurs
                if not 1 <= lines <= self.MAX_LINES:    # but if the user's input is not in range(1,3)
                    print(f"You are allowed to bet on minimum 1 line and maximum 3 lines")
                    continue                            # continue the loop first
                self.lines = lines                      # if the user's input is correct
                break                                   # break the loop

    def get_slot_machine_spin(self):    # this is to get random value with three lists in a list
        all_symbols = []                # list for all available symbols
        for symbol,symbol_count in self.symbols_count.items():  # loop the dictionary
            for _ in range(symbol_count):                       # loop again with the realted values of dct
                all_symbols.append(symbol)                      # the more values the key has,it will put more
        columns = []                    # final list that will have three lists
        for _ in range(self.COLUMNS):   # loop through with the column as the class variable
            column = []                 # a list in a final list
            current = all_symbols[:]    # copying all items to a new list
            for _ in range(self.ROWS):
                value =random.choice(all_symbols)   # take random value from all symbols list
                current.remove(value)               # remove that value form new list
                column.append(value)                # append the random value to the column list   
            # after looping and puting the symbol a list and append that list into the final list             
            columns.append(column)                  
        self.COLUMN = columns                     # make the final list as class variable to be callable from everywhere

    def print_slot_machine(self):                       # printing the random values 
        for row in range(len(self.COLUMN[0])):          # loop through about the rows
            for i,column in enumerate(self.COLUMN):     # loop through the final list
                if i == len(self.COLUMN) - 1:       
                    print(column[row])                  # print items in a final list by indexes
                else:
                    print(column[row],"|",end=" ")

    def check_winning(self,lines,bet):                  # check winner ( user's bet lines , user's bet amount)
        win = 0                                         # to get the winning betting amount
        win_lines = []                                  # to tack the winning lines
        for i in range(lines):                          # loop through the user's betting lines
            symb = self.COLUMN[0][i]                    # set the symbol of first nested list as a symb
            for col in self.COLUMN:                     # loop through with the final list
                symb_check = col[i]                     # assign the index of a final list as symbol check
                if symb != symb_check:                  # if the symb is not equal with the another symbol of a row
                    break                               # break the loop
            else:                                       # if the symbols of a list are same
            # multiply the user's bet and key of a rare state dictionary related to the symbol 
                win += self.symbols_value[symb] * bet   # add the total amount to the winning betting amount
                win_lines.append(i+1)                   # append the index of a wining line + 1 to the winning lines
        return win,win_lines                            # return the winning betting amount and winning lines


# user class including methods like a real user can do
class User:

    amount = 0                              # amount variable that will be in the machine
    # lines = 0                               # lines variable to store user's betting lines
    # instantiation method
    def __init__(self,name="You",bet=0):    # name parmeter to set user's name and bet parameter to take user's betting
        self.name = name                    # assign the parameters as a class variable
        self.bet = bet

    def deposit(self):                      # deposit function to get the user's deposited amount for machine
        print("Depositing amount")
        while True:                         # use while for checking the valid user's amount
            amt = input("> ")               # take the user's input      
            if amt.isdigit():               # if the user's input is digit
                amt = int(amt)              # typecast that digit string to integer
                if amt < 10:                # if the user's betting amount is less than 10
                    print("You need to deposit the minimum amount of 10$")   
                    continue                # restart the loop even if the input is digit    
                self.amount += amt          # add the amount to the class variable
                break                       # break the loop
            else:                           # if the user's input is not digit
                print("Please enter the valid amount only with the digits..")   # printing and do nothing
        # describe user that how much money had deposited to the machine
        return f"{self.name} added {amt}$ to the machine and total is {self.amount}$..." 

    def betting(self,lines):                # ask user for betting amount ( parameter : user's betting on lines)
        self.lines = lines                  # set user's betting on lines as class variable
        print(f"{self.name}'s Betting amount for each line")
        while True:                         # while loop for filtering user's invalid input
            bet_each = input("> ")          # ask user for betting amount on each line ( not total amount )
            if bet_each.isdigit():          # if user's input is digit
                bet_each = int(bet_each)        # type case user's input to integer
                bet_amt = bet_each * self.lines     #  multipy user's input and user's betting on lines
            # if user's total amount is greater than user's money in machine or total amount is less than 9$
                if bet_amt > self.amount or bet_amt < 9:  
                    print("You can't bet over your depositing amount or total betting not to be less than 9$")
                    print(f"{self.name} has only  deposited {self.amount}$") 
                    print(f"You bet a total of {self.lines} lines")  
                    continue                    # restart the while loop for insufficient amount
                self.bet = bet_amt         # make user's total amount as class variable
                break                      # and break the loop
            else:                          # if the user's input is not digit
                print("Please enter the valid amount only with the digits..")   # show error message
        self.amount -= self.bet            # subtract total betting amount from user's money in the machine
        return f"{self.name} bet {bet_each}$ for {self.lines} line(s) \nTotal betting : {self.bet}$"

    def game_on_off(self):             # game_on_off function to ask user play again or not
        for _ in range(1000*1000):     # used for loop but a very wide range like while loop
            game_on = input("Wanna play again?(y/n) ").upper()  # ask user and change user's input to uppercase
            if game_on in ["Y","N"]:                            # if user's input is "Y" or "N"
                # if a user who has less than 10$ want to play again
                if self.amount < 10 and game_on == 'Y':
                    print(f"{self.name} don't have enough money in machine\nSo {self.name} need to deposit..")
                    # tell the user to deposit money and return "Y1"
                    return "Y1"
                # if a user who has more than 10$ want to play again
                elif self.amount >= 10 and game_on == 'Y':
                    print(f"{self.name}  have enough money in machine...")
                    # ask again the user want to deposit or not
                    dp = input(f"Wanna deposit?(y/n) ").upper()
                    while dp not in ["Y","N"]:              # if the user's input is not "Y" or "N"
                        print("Please enter 'y' or 'n'")    # show error message and 
                        dp = input(f"Wanna deposit?(y/n) ").upper() # ask again
                    if dp == "N":           # if the user don't want to deposit again
                        return "Y2"         # return "Y2"
                    return "Y1"         # return "Y1" if the user's want to deposit again
                return game_on          # return "N"
            else:                                   # if the user's input is not in ["Y","N"]
                print("Please enter 'y' or 'n'")    # show error message

# driver code
if __name__ == '__main__':
    name = input("What's your name: ")
    my = User(name)           # create an instance of user's object including name
    slot = Machine()          # create an instance of slot machine's object 
    game_on = "Y"             # set game on as Y so that we can enter in while loop
    while not game_on == "N": # always looping till the user's don't want to play ( game_on == "N")
        print(my.deposit())             # ask the deposit amount
        for _ in range(1000*1000):      # for loop to check condition a user's play without depositing or not
            slot.ask_lines()            # ask user's betting on line
            print(my.betting(slot.lines))   # ask user's betting amount including betting on lines
            slot.get_slot_machine_spin()    # spin the slot machine
            slot.print_slot_machine()       # print the slot machine
            win,win_lines = slot.check_winning(slot.lines,my.bet)   # check winning and take tow return values
            if win == 0:                    # if user loses
                print("Sorry No win on your betting lines....")             # show message abd
                print(f"Your total amount in our machine: {my.amount}$")    # show remaining money
            else:                           # if user wins
                print(f"Yayy..You won {win}$ on your betting line number", *win_lines,"")   # show winning amount 
                my.amount += win            # add winning amount to the money's in the machine
                print(f"Your total amount in our machine: {my.amount}$")    # show total amount of money in machine
            game_on = my.game_on_off()      # ask user to play again or not
            if game_on == "N":              # if a user's don't want to play
                print(f"Have a nice day!See ya...")
                break                       # break the for loop
            elif game_on == 'Y1':           # if a user's want to play and deposit again
                print("Genius choice...")
                break                       # break the for loop and restart while loop
        else:                               # if a user want to play without depositing 
            print("You wanted to play the game without depositing..")
            continue                        # continue the for loop