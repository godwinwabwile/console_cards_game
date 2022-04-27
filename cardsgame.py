# select random cards
# allocate cards to each player
import random


'''card class has a deck list as an attribute. The setDeck method generates 12 random integers
between 1 and 20 and seeds them into self.deck list'''
class Cards:
    '''initialize the class'''
    def __init__(self, deck=[]):
        self.deck =deck

    '''get random numbers between 1 and 30 and populate the variable deck'''
    def setDeck(self):
        mylist=[]
        for num in range(12):
            ran =random.randint(1,20)
            mylist.append(ran)
        self.deck=mylist

    def __str__(self):
        print("My cards are {}".format(self.deck))
'''player inherits from the Cards class, has a status attribute(not so important for this console game) '''
class Player(Cards):
    def __init__(self, status):
        self.status=status

    '''method to view my cards'''
    def mycards(self):
        if len(self.deck)>0:
            print("here are your cards")
            print(self.deck)
        else:
            print("Your deck does not have any cards")
    '''logic of flashing one card'''
    def compPlay(self):
        if len(self.deck)>0:
            upperbound= len(self.deck)-1
            select= random.randint(0,upperbound) #selects a random index within the limits of the decks indeces
            values =[select, self.deck[select]]
            return values #returns a list card value and the selected index
        
        else:
            print("You do not have any cards in your deck")

    '''Game logic for human player'''
    def humanPlayer(self):
        if len(self.deck)>0:
            select = int(input("enter the index of the card you want to flip:")) #asks the user to input the index of a number 
            if type(select) == type(1) and select<len(self.deck): #checks if the input number is an integer and whether it is within the list of indices in the deck list
                values =[select, self.deck[select]]
                return values #returns a list card value and the selected index
            else:
                print("the value should be a number between 0 and {}".format(len(self.deck)-1)) #raises an error of a wrong type or a number beyond the bounds

        else:
            print("You do not have enough cards in your deck") #raises an error what there are no cards in the players deck



status =True #a variable that determines whether the game is on or off
comp =Player(1) #initialize an object of the player class
comp.setDeck() #run code to generate random cards for player 1
    
human_player= Player(2) #initialize an object of the player class
human_player.setDeck() #run code to generate random cards for player 1

#game loop
while status:
    
    '''logic to determine who starts the game'''
    #code blocks asks the user if they want to start the game or have the computer start the game
    starter = int(input("Type 1 if you want to start the game or 2 if you want the computer to start: ")) 
# the human player starts the game 
    if starter==1:
        mycards =human_player.mycards()
        mycard = human_player.humanPlayer()
        compscard = comp.compPlay()
        if mycard[1] > compscard[1]: #an incident where the human wins
            comp.deck.pop(compscard[0])
            human_player.deck.append(compscard[1])
            print("You selected {} while the computer selected {}. You win !!".format(mycard[1], compscard[1]))

        elif compscard >mycard: #in the event computer wins
            human_player.deck.pop(mycard[0])
            comp.deck.append(mycard[1])
            print("You selected {} while the computer selected {}. Computer wins !!".format(mycard[1], compscard[1]))

        elif compscard == mycard: # in the event there is a draw
            human_player.deck.pop(mycard[0])
            comp.deck.pop(compscard[0])
            print("You selected {} while the computer selected {}. ITS A DRAW!!".format(mycard[1], compscard[1]))

        else: 
            print("unexpected error occured with player 1")

# the computer starts the game
    elif starter ==2:
        compscard = comp.compPlay()
        if compscard[1]:print("The computer has flipped selected its card, select yours")


        mycards =human_player.mycards()
        mycard = human_player.humanPlayer()

        
        
        if mycard[1] > compscard[1]: #an incident where the human wins
            comp.deck.pop(compscard[0])
            human_player.deck.append(compscard[1])
            print("You selected {} while the computer selected {}. You win !!".format(mycard[1], compscard[1]))

        elif compscard >mycard: #in the event computer wins
            human_player.deck.pop(mycard[0])
            comp.deck.append(mycard[1])
            print("You selected {} while the computer selected {}. Computer wins !!".format(mycard[1], compscard[1]))

        elif compscard == mycard: # in the event there is a draw
            human_player.deck.pop(mycard[0])
            comp.deck.pop(compscard[0])
            print("You selected {} while the computer selected {}. ITS A DRAW!!".format(mycard[1], compscard[1]))

        else: 
            print("unexpected error occured with computer")

    else:
        print("To play, you can only enter 1 or 2")

    # determining the winner
    if len(human_player.deck)-len(comp.deck) >= 5:
        print("You WIN!!")
        status=False
    elif len(comp.deck)- len(human_player.deck) >= 5:
        print("You Loose!!")
        status=False
    





