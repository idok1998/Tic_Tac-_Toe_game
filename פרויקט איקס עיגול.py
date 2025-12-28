# משחק איקס עיגול 

# הלוח יהיה מורכב ממספרים מ-1 עד 9
# 1 | 2 | 3 
#---+---+---
# 4 | 5 | 6 
#---+---+---
# 7 | 8 | 9
    
# כאשר אחד מהמשתמשים מצליח להגיע ל3 צורות בקו ישר 
# (1 2 3), (4 5 6), (7 8 9), (1 5 9), (3 5 7), (1 4 7), (2 5 8), (3 6 9) 
# הוא ניצח במשחק.


def is_winner(board): 
    if board[1] == board[2] == board[3] and board[3]:
        return board[1]
    if board[4] == board[5] == board[6] and board[4]:
        return board[4]
    if board[7] == board[8] == board[9] and board[7]:
        return board[7]
    if board[1] == board[5] == board[9] and board[1]:
        return board[1]
    if board[3] == board[5] == board[7] and board[3]:
        return board[3]
    if board[1] == board[4] == board[7] and board[1]:
        return board[1]
    if board[2] == board[5] == board[8] and board[2]:
        return board[2]
    if board[3] == board[6] == board[9] and board[3]:
        return board[3]
    return None
    
def print_board(board):
    def val(x):
        return x if x is not None else " "
    print()
    print(f" {val(board[1])} | {val(board[2])} | {val(board[3])} ")
    print("---+---+---")
    print(f" {val(board[4])} | {val(board[5])} | {val(board[6])} ")
    print("---+---+---")
    print(f" {val(board[7])} | {val(board[8])} | {val(board[9])} ")
    print()

def game ():  
    print("Welcome to tic tac toe game!")
    print("Each turn, you choose which square to place your symbol in.")
    print("You need to get three in a row to win")
    print("User1 get the X symbol and user2 get the O symbol")
    def print_numbers_board():
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")
    print_numbers_board()

    board =[None] * 10 
    no_winner = True
    counter = 0
    while no_winner: 
        
        user1 = (int)(input("user 1 enter x locations: ")) 
        while user1 > 9 or user1 < 1 or board[user1] is not None: 
            user1 = (int)(input("the sell not in range or full, enter a new sell: "))
        board[user1] = "x"
        print_board(board) 
        if is_winner(board) == "x":
            print("user 1 is the winner of the game!")
            no_winner = False
            break
        counter += 1 
        if counter == 9:
            print("draw")
            return

        user2 = (int)(input("user 2 enter o locations: "))
        while  user2 > 9 or user2 < 1 or board[user2] is not None:
            user2 = (int)(input("the sell not inrange or full, enter a new sell: "))
        board[user2] = "o"
        print_board(board) 
        if is_winner(board) == "o":
            print("user 2 is the winner of the game!")
            no_winner = False
            break
        counter += 1
    return

def new_game():
    while True:
        while True:  
            start = input("Do you want to start a new game? (y/n): ").lower()
            if start in ('y', 'n'):
                break
            print("Please enter 'y' or 'n'.")
        if start == 'n':
            print("Goodbye!")
            break
        game()
new_game()