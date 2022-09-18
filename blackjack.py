import random 
import sys
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()    


class Player:
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.own_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.own_cards.pop(0)
    
    def cards(self):       
        print("\t\t\tYou have - ")
        for i in range(len(self.own_cards)):
            print(f"\t\t\t\t    {self.own_cards[i]}")

    def cards_val(self):
        value = 0
        for i in range(len(self.own_cards)):
            value += self.own_cards[i].value
        return value

    def cards_cmp(self):
        value = 0    
        for i in range(len(self.own_cards)):           
            value += self.own_cards[i].value
        return value
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.own_cards.extend(new_cards)
        else:
            self.own_cards.append(new_cards)
    
    
    def __str__(self):
        return f' {self.name} has {len(self.own_cards)} cards => {list(self.own_cards)}'
#function
def check_busts(val1,val2,name1,name2,amt):
    if val1 > 21:
        print(f"\n\t\t\t\t{name1} busts the game with {val1} and loses...")
        print(f"\t\t\t\tYou lose your {amt}$ , sorry..")
        return False
    elif val2 > 21 :
        print(f"\n\t\t\t\t{name2} busts the game with {val2} and loses...")
        print(f"\t\t\t\tYou win doubled  your betting {amt}$ ,Recieve {amt*2}$ ...")
        return False
    elif val1 > 21 and val2 > 21:
        print(f"\n\t\t\t\tDraw match......Both of you bust the game and...")
        return False
    else:
        return True

def check_winner(val1,val2,name1,name2,amt):
    if val2 > val1:
        print(f"\n\t\t\t\t{name2} beat {name1} with {val2} > {val1}")
        print(f"\t\t\t\tYou lose your {amt}$ , sorry..")
        return False
    elif val1 > val2:
        print(f"\n\t\t\t\t{name1} beat {name2} with {val1} > {val2}")
        print(f"\t\t\t\tYou win doubled  your betting {amt}$ ,Recieve {amt*2}$ ...")
        return False
    else:
        return True

def hit_or_stand(player,new_deck): 
    chk = int(input("\n\t\t\t\tPress 1 to hit or press 2 to stand: "))
    print(            "\t\t\t\t************************************")
    if chk == 1:
        print(f"\n\t\t\t\t{player.name} deal one card from the deck...")
        player.add_cards(new_deck.deal_one()) 
    elif chk == 2 :
        print(f"\n\t\t\t\t{player.name} stands.....")
        return chk
    else:
        print("Wrong input")

def show_all(player,comp):
    print("\t\t\tYou have - ")
    for i in range(len(player.own_cards)):
        print(f"\t\t\t\t    {player.own_cards[i]}")
    print("\t\t\tComputer Dealer have - ")
    for i in range(len(comp.own_cards)):
        print(f"\t\t\t\t\t    {comp.own_cards[i]}")

#Main part
def main():
    if len(sys.argv) == 2:
        player = Player(sys.argv[1])
    else:
        player = Player('1')
    comp = Player('Computer dealer')

    new_deck=Deck()
    new_deck.shuffle()
    print("\n\t\t\t\t ******* Welcome to the blackjack Game! ******* ")
    print("\t\t\t\t ******* You have to face with Our AI 1.0 ! ******* ")
    amt = int(input("\t\t\t ==> Put your betting amount: "))
    input("\n\t\t\tPress enter to start the game.....") 
    game_on = True   
    player.add_cards(new_deck.deal_one())
    comp.add_cards(new_deck.deal_one())
    player.add_cards(new_deck.deal_one())
    comp.add_cards(new_deck.deal_one())  
    count = 0
    chk = 0
    while game_on:   
            player.cards()
            result1 = player.cards_val()
            result2 = comp.cards_cmp()
            # game_on=check_busts(result1,result2,player.name,comp.name,amt)
            # if game_on == False:
            #     show_all(player,comp)
            #     break
            print(f"\n\t\t\t\tComputer has {comp.own_cards[count]}")
            print( "  \t\t\t\t********************************")
            
            if result1 < 16:
                input("\n\t\t\t\t You are cards are under 16 so press enter to deal a card: ")
                player.add_cards(new_deck.deal_one()) 
                player.cards()
            else:
                chk = hit_or_stand(player,new_deck)
                

            if result1 <= 21 :
                if result2 < result1:
                    comp.add_cards(new_deck.deal_one())
                    result2 = comp.cards_cmp()
            
            
            game_on=check_busts(result1,result2,player.name,comp.name,amt)     
            if game_on == False:
                show_all(player,comp)
                break 
            if chk == 2:
                    game_on=check_winner(result1,result2,player.name,comp.name,amt)           
                    if game_on == False:
                        show_all(player,comp)
                        break
    count += 1

        

if __name__ == '__main__':
    main()

    



