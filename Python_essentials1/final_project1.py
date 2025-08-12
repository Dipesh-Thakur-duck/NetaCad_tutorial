from random import randrange

board = [
    [1,2,3],
    [4,'X',6],
    [7,8,9]
]

def display_board(board):
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   X   |   {board[1][2]}   |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   | 
+-------+-------+-------+      
""")

def is_board_full(board):
    list1 = list(range(1,10))
    result = True
    for row in board:
        for column in row:
            if column in list1:
                result = False
                return result
    return result

def enter_move(board):
    tie_or_not = is_board_full(board)
    if tie_or_not:
        return 'Tie'
    user_move = int(input("Enter your move: "))
    found = False
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            if user_move == board[rows][columns]:
                board[rows][columns] = 'O'
                display_board(board)
                result = victory_for(board,'O')
                if result:
                    print(f"{result} won!")
                    return False
                tie_or_not = is_board_full(board)
                if tie_or_not:
                    return 'Tie'
                found = True
                break
        if found:
            break
    else:
        print("Already occupied!")
        return enter_move(board)
    return True #-> game should continue

def draw_move(board):

    tie_or_not = is_board_full(board)
    if tie_or_not:
        return 'Tie'
    
    computer_move = randrange(1,10)
    found = False
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            if computer_move == board[rows][columns]:
                board[rows][columns] = 'X'
                display_board(board)
                result = victory_for(board,'X') # can be True, False or None (falsy)
                if result:
                    print(f'{result} won!')
                    return False
                tie_or_not = is_board_full(board)
                if tie_or_not:
                    return 'Tie'
                found = True
                break
        if found:
            break
    else:
        print("Already occupied!")
        return draw_move(board)
    return True # -> game should continue

def victory_for(board,sgn):
    if sgn == 'X':
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: # vertical strike check
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # horizontal strike check
            return who
        if board[rc][rc] != sgn: # top-left to bottom-right diagonal check
            cross1 = False
        if board[rc][2-rc] != sgn: # bottom-left to top-right diagonal check
            cross2 = False
    if cross1 or cross2:
        return who
    return None

print("\n**Welcome to the tic-tac-toe game**")
display_board(board)

while True:
    if not enter_move(board):
        break
    if not draw_move(board):
        break
    if enter_move == 'Tie' or draw_move == 'Tie':
        print("It's a tie!")
        game_on = False


    


