import random as rd


WIN =   {448, 56, 7, 292, 146, 73, 84, 273} # winning combinations 
NUMBERS = ("0️⃣","1️⃣","2️⃣","3️⃣","4️⃣", "5️⃣","6️⃣", "7️⃣","8️⃣", "9️⃣") # possible moves 
TILE = "🔹"; X  = "❌"; O = "🟢" # tile, X, O for drawing 


def move(score, index):
    """ Set the index: th bit of v to 1 and return the new value. """
    return score | (1 << index)


def is_placed(score, index): 
    """ checks if bit is placed in score """ 
    return not (score & (1 << index)) == 0 


def is_placed_both(scoreX, scoreO, i):
    """ checks if bit is placed in both scores """
    return (is_placed(scoreX, i) or is_placed(scoreO, i))
        

def possible_moves(scoreX, scoreO):
    """ returns array of possible moves 0-9 """
    return [i for i in range(9) if not is_placed_both(scoreX, scoreO, i)]


def is_win(score):
    """ check if any winning bit combination in score """
    return True in map(lambda win: (score & win) == win, WIN)


def find_winner(scoreX, scoreO):
    """ first score - X, second score - O"""
    if is_win(scoreX): return (True, "X")
    if is_win(scoreO): return (True, "O")
    return (False, None)


def draw_field(scoreX, scoreO, counter):
    print(TILE*7)
    for j in range(9):                  
        if (j) % 3 == 0: print('', end=TILE)              # tile before any row 
        if is_placed(scoreX, j): print(X, end=TILE)       # X
        elif is_placed(scoreO, j): print(O, end=TILE)     # O
        else: print(f"{NUMBERS[j+1]} ", end=TILE)         # possible move number 
        if (j+1) % 3 == 0: print("\n" + TILE*7)           # line between rows 
    print(f'     ➡️{" " + X if counter % 2 != 0 else " "+ O}') # next player moving 


scoreX  = 0 # player 1 moves 
scoreO  = 0 # player 2 moves
counter = 0 # move counter 
winner = (False, None) # winner 
ai = 'y' in input(" > Play with AI? yes/no: ") 

draw_field(scoreX, scoreO, counter)
while False in winner and counter < 9:
    # if player move 
    if not (counter % 2 != 0 and ai): 
        choice = input(" > Your move: ")
        # if something is False: choice is number; in range 0 - 10; not placed
        if False == choice.isnumeric() and 0 > int(choice) > 10 and is_placed_both(scoreX, scoreO, int(choice)-1):
            print ("\033[A \033[A") # erase line 
            continue    
        else: choice = int(choice)
    else: choice = rd.choice(possible_moves(scoreX, scoreO)) + 1  # if is ai move pick random cell
        
    if counter % 2 == 0: scoreX = move(scoreX, choice-1) 
    else:                scoreO = move(scoreO, choice-1) 
    
    draw_field(scoreX, scoreO, counter)
    winner = find_winner(scoreX, scoreO)
    counter += 1    
    
if True in winner: # print winner
    print( f"{'❌ Won!' if 'X' in winner else '🟢 Won!'}")
else: print("⬜️ Tie! ") # print tie 
