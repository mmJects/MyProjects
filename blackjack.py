# user/bin/env Python3
# BlackJack Game by Yun Yun
# Outlined by PERIAN Data
import random                   # import random module for random choices
import sys                      # import sys module to count argumnets in terminal
# Shapes
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')   
# Prefixes
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# Values of Prefixes
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}

class Card:     # Card class to show the name of the card
    def __init__(self,suit,rank):       # attributes ( shape , Prefixes)
        self.suit = suit                # assign class atrribute - shape of a card
        self.rank = rank                # assign calss attribute - prefix of a card
        self.value = values[rank]       # get the value with the prefix attribute
        
    def __str__(self):                  # string method 
        return self.rank + ' of ' + self.suit   # to return the name of a card

class Deck:     # Deck class to store all the 51 cards
    def __init__(self):     # intiate the deck class
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []     # list to store all cards
        for suit in suits:      # loop through the shapes lists
            for rank in ranks:  # loop through the prefixes list
                # This assumes the Card class has already been defined!
                # use Card class to get the name of a card with that prefix and shpae 
                self.all_cards.append(Card(suit,rank))  # store the card name into a list
                
    def shuffle(self):                  # shffle method to shuffle 
        # Note this doesn't return anything and  shffle all the cards of a list
        random.shuffle(self.all_cards)  
        
    def deal_one(self):                # deal one method to remove card
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()    


class Player:                   # Player class to store player's cards
    def __init__(self,name):    # initialize the class with the name attribute
        self.name = name        # assign name attribute
        # A new player has no cards
        self.own_cards = []     # a list to store player's cards
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.own_cards.pop(0)
    
    def cards(self):            # cards method to display player's cards     
        print(f"\t\t\t{self.name} have - ")
        for i in range(len(self.own_cards)):            # loop through as the amount of player's cards 
            print(f"\t\t\t\t    {self.own_cards[i]}")   # display each card through the looping 

    def cards_val(self):        # cards_val method to calculate the points of computer 
        value = 0
        for i in range(len(self.own_cards)):    # loop through as the amount of player's cards
            value += self.own_cards[i].value    # add the value of each card 
        return value                            # return totol value 

    def cards_cmp(self):        # cards_cmp method to calculate the points of computer
        value = 0    
        for i in range(len(self.own_cards)):    # loop through as the amount of computer's cards          
            value += self.own_cards[i].value    # add the value of each card 
        return value                            # return totol value 
    
    def add_cards(self,new_card):               # add_cards method to add
        self.own_cards.append(new_card)         # append the card to the list
    
    
    def __str__(self):
        return f' {self.name} has {len(self.own_cards)} cards => {list(self.own_cards)}'

# check bust function
# ( value of plyaer cards , value of computer cards , name of player , computer , betting amount )
def check_busts(val1,val2,name1,name2,amt):    
    if val1 > 21:       # if the player's points exceed 21
        print(f"\n\t\t\t\t{name1} busts the game with {val1} and loses...")
        print(f"\t\t\t\tYou lose your {amt}$ , sorry..")
        return False
    elif val2 > 21 :    # if the computer's points exceed 21
        print(f"\n\t\t\t\t{name2} busts the game with {val2} and loses...")
        print(f"\t\t\t\tYou win doubled  your betting {amt}$ ,Recieve {amt*2}$ ...")
        return False
    elif val1 > 21 and val2 > 21:   # if both player's points exceed 
        print(f"\n\t\t\t\tDraw match......Both of you bust the game ...")
        return False
    else:                           # if no one busts
        return True

# check winner function
# ( value of plyaer cards , value of computer cards , name of player , computer , betting amount )
def check_winner(val1,val2,name1,name2,amt):
    if val2 > val1:     # if someone loses
        print(f"\n\t\t\t\t{name2} beat {name1} with {val2} > {val1}")
        print(f"\t\t\t\tYou lose your {amt}$ , sorry..")
        return False
    elif val1 > val2:   # if someone wins
        print(f"\n\t\t\t\t{name1} beat {name2} with {val1} > {val2}")
        print(f"\t\t\t\tYou win doubled  your betting {amt}$ ,Recieve {amt*2}$ ...")
        return False
    else:               # if no one wins or lose 
        return True

# hit or stand function to ask users
def hit_or_stand(player,new_deck):      # ( player class , deck class )
    chk = "a"                           # first initalize the input value to go in while loop
    while chk not in ["1","2"]:         # to validate user's input with while loop
        chk = input("\n\t\t\t\tPress 1 to hit or press 2 to stand: ")   # ask user's input
        print(            "\t\t\t\t====================================")
    chk = int(chk)                      # type cast the user's input to interger
    if chk == 1:                        # if the player hits
        print(f"\n\t\t\t\t{player.name} deal one card from the deck...")
        player.add_cards(new_deck.deal_one())   # remove one card from the deck
    elif chk == 2 :                     # if the player stand
        print(f"\n\t\t\t\t{player.name} stands.....")
        return chk

# bet_amt function to ask your betting amount
def bet_amt():
    while True:
        print(f"\t\t\t Put your betting amount: ") 
        amt = input("\t\t\t ==> ")                  # ask the betting amont 
        try:                                        # try 
            amt = int(amt)                          # to typecast to integers 
        except:                                     # if there is an error
            print("\t\t Please enter only digits ")   # show error message
            continue                                    # start the loop
        if amt < 1:                                 # if the input is less than 1:
            print("\t\t You can only bet above 1$..")
            continue                                # start the loop
        return amt                                  # return the amount if there is no error

# show all the cards of participants
def show_all(player,comp):      # ( player class , computer class )
    print("\t\t\tYou have - ")
    for i in range(len(player.own_cards)):
        print(f"\t\t\t\t    {player.own_cards[i]}")
    print("\t\t\tComputer Dealer have - ")
    for i in range(len(comp.own_cards)):
        print(f"\t\t\t\t\t    {comp.own_cards[i]}")

# driver function
def main():
    if len(sys.argv) == 2:      # if the player input his name in terminal
        player = Player(sys.argv[1])    # assign that name to player
    else:                       # if no name
        player = Player('1')    # assign "1" to player
    comp = Player('Computer dealer')    # make an instance of Computer 
    new_deck=Deck()                     # make an instance of deck
    new_deck.shuffle()                  # shuffle the cards 
    print("\n\t\t\t\t ******* Welcome to the blackjack Game! ******* ")
    print("\t\t\t\t ******* You have to face with Our AI 1.0 ! ******* ")
    amt = bet_amt()
    input("\n\t\t\tPress enter to start the game.....") 
    game_on = True                      # game on True
    player.add_cards(new_deck.deal_one())   # remove one card for player
    comp.add_cards(new_deck.deal_one())     # remove one card for computer
    player.add_cards(new_deck.deal_one())   # remove one card for player
    comp.add_cards(new_deck.deal_one())     # remove one card for computer
    count = 0       
    chk = 0
    while game_on:   
            player.cards()                  # show the player's cards
            result1 = player.cards_val()    # get the value of player
            result2 = comp.cards_cmp()      # get the value of computer
            print(f"\n\t\t\t\tComputer has {comp.own_cards[count]}")    # show one card of computer
            print( "  \t\t\t\t********************************")
            
            if result1 < 16:                            # if player's cards are under 16
                input("\n\t\t\t\t You are cards are under 16 so press enter to deal a card: ")
                player.add_cards(new_deck.deal_one())   # remove one card from deck
                player.cards()                          # show the player's cards
            else:                                       # if the player's cards are above or equal 16
                chk = hit_or_stand(player,new_deck)     # ask player to stand or hit
                

            if result1 <= 21 :              # if the player's points is less than 21
                if result2 < result1:       # and player's point is greater than computer's points
                    comp.add_cards(new_deck.deal_one()) # remove one card for computer
                    result2 = comp.cards_cmp()
            
            
            game_on=check_busts(result1,result2,player.name,comp.name,amt)  # check bust function
            if game_on == False:        # if someone loses
                show_all(player,comp)   # show all cards of particiapants
                break 
            if chk == 2:                # if player stands
                    game_on=check_winner(result1,result2,player.name,comp.name,amt)    # check winner           
                    if game_on == False:         # if someone wins
                        show_all(player,comp)   # show all cards of particiapnats
                        break                   # break the loop
    count += 1

        

if __name__ == '__main__':
    main()

    



