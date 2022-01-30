'''
Blackjack
Done by: Neha Gopinathan'''

import cards

def hand_score(hand):
    '''This function is used to determine the score in each hand. Using the for loop, it creates a string that will be used
to add the cards. The if functions are used to add the values of the face cards; the elif function is for the Ace card to detemine
which number will be used.'''
    score = 0
    for card in hand:
        y=str(card[0])
        if y == 11 or y == 12 or y == 13:
            score=score+10
        elif y == 14:
            if (score+11) >= 11:
                score=score+1
            else:
                score=score+11
        else:
            score=score+int(y)
    return score


def print_hand_and_score(name, hand):
    '''This function is used to display the name and hand of the players in the game. Using the for loop, it is used to sort the cards
in each hand. The if condition is used to find the smaller card in the hand and sort it. It then prints the hand.'''
    print(name)
    small=hand[0][0]
    c=len(hand)
    for i in range(c-1):
        small=i
        for x in range (small+1, c):
            if hand[x][0]<hand[small][0]:
                small=x
        hand[i], hand[small]=hand[small], hand[i]
    for a in hand:
        print(a[3], end="")
    print("\tScore: ", str(hand_score(hand)))


def win_lose_or_draw(player_score, dealer_score):
    '''This function is used to determine who won the round. Using the if function, it determines the conditions and prints the appropriate phrase.'''
    if player_score == 21:
        print("Congratulations! You won.\n")
    elif dealer_score == 21:
        print("Sorry, The Dealer won!\n")
    elif player_score > 21:
        print("Sorry, you busted. You lost the game!\n")
    elif dealer_score > 21:
        print("The Dealer busted. You won the game!\n")
    elif player_score > 21 and dealer_score > 21:
        print("The game is draw!\n")
    elif player_score > dealer_score:
        print("Congratulations, your score is higher, so you won!\n")
    elif player_score < dealer_score:
        print("Sorry, the Dealer score is higher, you lost the game!\n")
    elif player_score == dealer_score:
        print("The game is draw!")


def dealer_hit_or_stand(player_hand, dealer_hand):
     '''This function is used to determine if the dealer will hit or stand his hand. Using the while function, it calls the "hand_score" function to
know whether to hit or stand. The if conditions is used to decide to hit. If the function is True then the dealer hits, otherwise it stands.'''
     while hand_score(player_hand) < 21:
        if hand_score(dealer_hand) < 17 or hand_score(dealer_hand) < hand_score(player_hand):
            return True
        else:
            return False

def player_hit_or_stand():
    '''This function is used to determine whether the player wants to hit or stand. Using the while function, this is if the player enters a letter
that isn't used to describe "hit" or "stand", it then prints the statement again for the player to try again. The if conditions is used to determine what
the user has chosen.'''
    i=str(input("(H)it or (S)tand?: "))
    while not (i=="S" or i=="s" or i=="H" or i=="h"):
        print("You entered the wrong input!")
        i = input("(H)it or (S)tand?")
    if i.upper()=="H":
        return True
    elif i.upper()=="S":
        return False
        

def main():
    '''This function calls function for the orignal code "cards.py" such as "make_deck", "deal", "shuffle" and "draw" fucntions to help start the game.
It first asks for the player's name, then proceeds to make the deck using the "make_deck" fucntion. It then proceeds to cut the deck in half and gives
the player and dealer 2 cards from the bottom half of the deck. After giving the cards to the players, it calls the "print_hand_and_score_" of the player
and dealer's hands. It then asks the player and dealer if they want to hit or stand by calling the "player_hit_or_stand" fucntion" and "dealer_hit_or_stand".
If they chose to hit then a card will be added to their hand using the "draw" fucntion from "cards.py" After adding the cards of each hand, it then uses the
"win_lose_or_draw" fucntion to determine who won.'''
    playerName=input("Please enter your name: ")
    dealerName="Dealer"
    deck=cards.make_deck()
    shuffleddeck=cards.shuffle(deck)
    top,bottom=cards.cut(shuffleddeck)
    player_hand = cards.deal(2, bottom)
    dealer_hand = cards.deal(2, bottom)
    choice=0
    player_score=hand_score(player_hand)
    dealer_score=hand_score(dealer_hand)
    print_hand_and_score(playerName, player_hand)
    print_hand_and_score(dealerName, dealer_hand)
    hit_choice=player_hit_or_stand()
    hit_choice2=dealer_hit_or_stand(player_hand, dealer_hand)
    if hit_choice==True:
        player_hand.append(cards.draw(bottom,player_hand,2))
    if hit_choice2==True:
        dealer_hand.append(cards.draw(bottom,dealer_hand,2))
    print_hand_and_score(playerName, player_hand)
    print_hand_and_score(dealerName, dealer_hand)
    win_lose_or_draw(player_score,dealer_score)

if __name__=='__main__':
    main()
    input()
   
