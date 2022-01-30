'''Memory Game
Done by: Neha Gopinathan'''

import cards
import time

try:
    r = int(input("Row: "))
    cs = int(input("Column: "))
    if r*cs % 2 !=0:
        print("Try again with different values!")
        exit()
    elif r == 1 and cs == 1:
        print("Try again with different values!")
        exit()
except ValueError:
    print("Not a value, try again")
    exit()

def make_flippable(card):
    '''This function is made to make the cards flippable. It is faced down when it is set to "False", it then appends the card to the list'''
    list = [False]
    list.append(card)
    return list
    
def is_match(carda, cardb, score):
    '''This function is to find the cards that match. It uses the if condition on the cards that are flipped up; which are "True"
and compares them. If they are both true, it then uses another if condition to determine if they match. If the cards match then
the score will add up, if they don't match then it will flip both cards down.'''
    if carda[0] == True and cardb[0] == True:
        if carda[1][0] == cardb[1][0] and carda[1][2] == cardb[1][2]:
            print("It's a match!\n")
            remove_cards(board, carda)
            score += 1
            return score
        else:
            print("It's not a match!\n")
            flip_carddown(board)
    else:
        print("One or both cards are not face up!\n")
    return score


def select_cards(no_of_cards, deck):
    '''This function is used to select enough cards from the number of cards chosen to fill the board. It spilts the cards in half, then
duplicates the cards from one half of the deck.'''
    cards_formemory = []
    half = int(no_of_cards/2)
    listtwo = cards.deal(half, deck)
    return listtwo*2

def make_board(rows, columns, deckk):
    '''This function is used to make the board. it calls the select_cards function which determines the amount of cards needed
then shuffles them. using the '''
    deck = select_cards(rows*columns, deckk)
    shuffleddeck = cards.shuffle(deck)
    final_deck = []
    test = shuffleddeck
    c=0
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(test[j+c])
        c+=columns
        final_deck.append(row)
    board = [[make_flippable(final_deck[i][j]) for j in range(columns)] for i in range(rows)]
    return board
    
def print_board(board):
    '''This function is used to display the board. If the card is facing down then it displays the default flipped side.
If the card is chosen then it displays the number of the card that was facing down. '''
    for i in range(r):
        for j in range(cs):
            if board[i][j][0] == False:
                print('[-]', '\t', end = '')
            elif board[i][j][0] == True:
                print(board[i][j][1][3], '\t', end = '')
            else:
                print('', '\t', end = '')
        print('\n')

def make_move(board):
    '''This function is to make the move of picking the card that you want by picking the row and column number. it then splits the
values into 2, one for the rwo and one for the column. '''
    choice = []
    try:
        choice = input("Enter row and column: ")
    except ValueError:
        print("Not a value")
    try:
        values = choice.split()
        rows = values[0]
        columns = values[1]
    except ValueError:
        print("Enter proper value!")
    finally:
        return int(rows), int(columns)

def flip_carddown(board):
    '''This function flips the cards facing down. It sets them to False for them to be faced down.'''
    for i in range(r):
        for j in range(cs):
            board[i][j][0] = False
    
def flip_cardup(board, choice):
    '''This function is used to flip the cards faced up. If the card is picked then it sets it to "True" which then reveals the card.'''
    try:
        for i in range(r):
            for j in range(cs):
                if i == int(choice[0]) and j == int(choice[1]):
                    board[i][j][0] = True
    except TypeError:
        print("Card has been removed or is already face-up!")

def remove_cards(board, choice):
    '''This function removes the cards that match from the board. if they match then it sets the place in the board as blank'''
    for i in range(r):
        for j in range(cs):
            if choice == board[i][j]:
                board[i][j] = "   "
    
def main():
    '''This function calls the print_board to display the board and starts the time. It then sets the score to 0
and uses the while function to start the process of the game. It flips the chosen cards and compares them using the is_match function.
If they aren't the same then the score remains the same and continues the loop. if the cards are the same then the score increases the score.
After all the cards are gone it displays the final score.'''
    deck = cards.make_deck()
    newdeck = cards.shuffle(deck)    
    board = make_board(r, cs, newdeck)
    print_board(board)
    start = time.time()
    end = time.time()
    print("Time:", round(end - start, 1), "seconds")
    score = 0
    loopcont = int((r*cs)/2)
    print("Score:", score)
    while score < loopcont:
        r1, c1 = (make_move(board))
        flip_cardup(board, (r1, c1))
        print_board(board)
        r2, c2 = (make_move(board))
        flip_cardup(board, (r2, c2))
        end = time.time()
        print_board(board)
        print("Time:", round(end - start, 1), "seconds")
        score = is_match(board[r1][c1], board[r2][c2], score)
        print_board(board)
        print("Score:", score)
    print("Thank you for playing!")
    exit()



if __name__ == "__main__":
    main()
    input()
