"""
Author:Robert Elliott
TicTacToe game solution
"""

def create_board():
    board = []
    for i in range(9):
        board.append(i+1)
    return board
        
def draw_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-+-+-+-+-")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-+-+-+-+-")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_move(player, board):
    move_choice = int(input(f"{player}'s turn to move: "))
    board[move_choice-1] = player

def is_winner(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True

def get_player(current):
    if current == "x":
        return "o"
    elif current == "o":
        return "x"

def is_draw(board):
    for i in range(9):
        if isinstance(board[i], int):
            return False
    return True

def main():    
    board = create_board()
    winner = False
    draw = False
    player = "x"
    while not (winner or draw):
        draw_board(board)
        player_move(player, board)
        player = get_player(player)
        winner = is_winner(board)
        draw = is_draw(board)
    draw_board(board)
    print("Good game. Thanks for playing!") 
if __name__ == "__main__":
    main()