import random
import matplotlib.pyplot as plt

# Implementation of Tic Tac Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for draw
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Draw'

    return None

def make_random_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def is_game_over(board):
    return check_winner(board) is not None

def play_game():
    board = initialize_board()
    current_player = 'X'

    while not is_game_over(board):
        row, col = make_random_move(board)
        board[row][col] = current_player
        current_player = 'O' if current_player == 'X' else 'X'

    return check_winner(board)

def main(num_games):
    results = {'X': 0, 'O': 0, 'Draw': 0}
    for _ in range(num_games):
        winner = play_game()
        if winner == 'Draw':
            results['Draw'] += 1
        else:
            results[winner] += 1
    
    print("Results after", num_games, "games:")
    print("X Wins:", results['X'])
    print("O Wins:", results['O'])
    print("Draws:", results['Draw'])

    # Plotting results
    labels = ['X Wins', 'O Wins', 'Draws']
    values = [results['X'], results['O'], results['Draw']]
    plt.bar(labels, values, color=['blue', 'green', 'red'])
    plt.xlabel('Results')
    plt.ylabel('Frequency')
    plt.title('Tic Tac Toe Results')
    plt.show()

if __name__ == "__main__":
    num_games = 1000
    main(num_games)
