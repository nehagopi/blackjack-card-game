'''Done by: Neha Gopinathan'''

import random

from colorama import init
init()

def make_card(rank, suit):
    '''This function is used to make the card, the shorthand is created
by the rank and the first letter of the suit. For the face cards, each face has been assigned a number, which using the if
function will help name the card by it's appropriate name. To add the color of each card, if functions are added to determine
which color should be used for which suit. A touple is created which contains the card's information such as the rank, suit, name and the shorthand.'''
    rank=str(rank)
    shorthand="   "
    if rank=='10':
        name="10 of " + suit
        shorthand="10"+suit[0].upper()
    elif rank=='11':
        name="Jack of " + suit
        shorthand=" J"+suit[0].upper()
    elif rank=='12':
        name="Queen of " + suit
        shorthand=" Q"+suit[0].upper()
    elif rank=='13':
        name="King of " + suit
        shorthand=" K"+suit[0].upper()
    elif rank=='14':
        name="Ace of " + suit
        shorthand=" A"+suit[0].upper()
    else:
        name= rank + " of " + suit
        shorthand=" "+rank+suit[0].upper()
    if suit[0].upper()=="H" or suit[0].upper()=="D":
        shorthand = "\u001b[31m" + shorthand + "\033[37m"
    else:
        shorthand = "\u001b[34m" + shorthand + "\033[37m"
    cardtuple=(rank, suit, name, shorthand)
    return cardtuple
    
def make_deck():
    '''This function is made is create the deck. Using the for loop, it takes each suit and
adds every card rank to it, then appends it the the list "mydeck", which then creates a list of 52 different cards.'''
    mydeck=[]
    c=["Hearts","Diamonds","Clubs","Spades"]
    for x in c:
        for i in range(2,15):
            mydeck.append(make_card(i,x))
    return(mydeck)

def shuffle(a):
    '''This function is used to shuffle the cards and will enter a different card for every time it runs.'''
    length = len(a)
    for i in range(length):
        j=random.randint(0,length-1)
        if i!=j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    return a

def draw(a,hand, noofcard):
    '''This function is used to select a random card. It checks the number of cards '''
    if len(a) > 0:
        j=random.randint(0,noofcard)
        hand=a[j]
        a.remove(a[j])
    return hand

def deal(noofcard,a):
    '''This function is used to add cards to each hand. Using the for loop, it calls the 'draw' function to add cards to each hand'''
    onehand=[]
    for i in range(noofcard):
        onehand.append(draw(a,onehand, noofcard))
    return onehand

def cut(a):
    c=len(a)//2
    return a[:c],a[c:]
     
def main():
    '''This functions calls the 'make_deck' and 'shuffle' function to put different cards for each hand that was created.
Using the for loop, it prints three random cards to each hand'''
    a = make_deck()
    a = shuffle (a)
    b,c=cut(a)
    onehand = deal(2,a)
    print ("cards in hand one: ")
    for i in range(2):
        print ("%s "%onehand[i][3])

if __name__=='__main__':
    main()
        
    
    
        
        

        
