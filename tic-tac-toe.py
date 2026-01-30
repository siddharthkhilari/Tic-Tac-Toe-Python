
import random


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def player_move(board, player):
    while True:
        try:
            position = int(input(f"Player {player}, choose position (1-9): "))

            if position < 1 or position > 9:
                print("❌ Please choose a number between 1 and 9.")
                continue

            if board[position - 1] != " ":
                print("❌ Position already filled. Try another.")
                continue

            board[position - 1] = player
            break

        except ValueError:
            print("❌ Please enter a valid number.")



def computer_move(board):
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    position = random.choice(empty_positions)
    board[position] = "O"
    print("Computer chose position:", position + 1)



def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False



board = [" "] * 9
current_player = "X"

print("🎮 TIC TAC TOE — You (X) vs Computer (O)")

for turn in range(9):
    print_board(board)

    if current_player == "X":
        player_move(board, "X")
    else:
        computer_move(board)

    if check_winner(board, current_player):
        print_board(board)
        print(f"🏆 {current_player} wins!")
        break

    current_player = "O" if current_player == "X" else "X"
else:
    print_board(board)
    print("🤝 It's a draw!")
