import math

# Board with empty spaces
board = [" " for _ in range(9)]

# Show Position Guide for Player
def show_positions():
    print("\nChoose positions like this:")
    print("[{1,2,3},")
    print(" {4,5,6},")
    print(" {7,8,9}]\n")


# Print Current Board
def print_board():
    print("\nCurrent Board:")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print("\n")


# Check Winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)


# Check Draw
def is_draw():
    return " " not in board


# Available Moves
def available_moves():
    return [i for i in range(9) if board[i] == " "]


# -------------------------------
# Minimax with Alpha Beta Pruning
# -------------------------------

def minimax(is_maximizing, alpha, beta):

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    # AI Turn (Maximizing)
    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False, alpha, beta)
            board[move] = " "

            best_score = max(best_score, score)
            alpha = max(alpha, score)

            if beta <= alpha:
                break

        return best_score

    # Human Turn (Minimizing)
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True, alpha, beta)
            board[move] = " "

            best_score = min(best_score, score)
            beta = min(beta, score)

            if beta <= alpha:
                break

        return best_score


# AI Best Move Search
def best_ai_move():
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = "O"
        score = minimax(False, -math.inf, math.inf)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# -------------------------------
# Main Game Loop
# -------------------------------

def play_game():
    print("🎮 Tic Tac Toe AI Project")
    print("You are X | AI is O")

    show_positions()

    while True:
        print_board()

        # Human Move (1–9)
        try:
            human_move = int(input("Enter position (1-9): ")) - 1
        except:
            print("Invalid input! Enter number 1-9.")
            continue

        if human_move < 0 or human_move > 8:
            print("Enter valid position (1-9).")
            continue

        if board[human_move] != " ":
            print("Position already filled! Try again.")
            continue

        board[human_move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 You Win!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        # AI Move
        print("🤖 AI is thinking...")
        ai_move = best_ai_move()
        board[ai_move] = "O"

        if check_winner("O"):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break


# Run Game
play_game()
