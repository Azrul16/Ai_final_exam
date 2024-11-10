import copy
import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print("\n")

# Function to calculate heuristic (number of attacking pairs)
def get_heuristic(board):
    attacks = 0
    positions = []

    # Get positions of all queens
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                positions.append((i, j))

    # Count the number of attacking pairs
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            # Check if queens are in the same row, column, or diagonal
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                attacks += 1
    return attacks

# Function to generate all possible neighbor boards
def get_neighbors(board):
    neighbors = []
    for col in range(8):
        # Find the current row with a queen in this column
        current_row = None
        for row in range(8):
            if board[row][col] == 1:
                current_row = row
                break

        # Skip this column if there is no queen
        if current_row is None:
            continue

        # Generate neighbors by moving the queen within this column
        for new_row in range(8):
            if new_row != current_row:
                new_board = copy.deepcopy(board)
                new_board[current_row][col] = 0
                new_board[new_row][col] = 1
                neighbors.append(new_board)

    return neighbors

# Hill Climbing algorithm
def hill_climbing(board, goal_state):
    current_board = board
    current_heuristic = get_heuristic(current_board)
    iteration = 0

    while True:
        print(f"Iteration {iteration}: Heuristic = {current_heuristic}")
        print_board(current_board)

        # Check if the current board matches the goal state
        if current_board == goal_state:
            print("Goal state reached!")
            return current_board

        if current_heuristic == 0:
            print("Solution found!")
            return current_board

        neighbors = get_neighbors(current_board)

        # If no neighbors, or no improvement, we break
        if not neighbors:
            print("No neighbors found. Stopping.")
            return current_board

        # Sort neighbors based on the heuristic, we choose the one with the lowest heuristic (minimum attacking pairs)
        neighbors.sort(key=get_heuristic)

        # Select the best neighbor (the one with the least attacking pairs)
        best_neighbor = neighbors[0]
        best_heuristic = get_heuristic(best_neighbor)

        # If no better neighbor is found, break
        if best_heuristic >= current_heuristic:
            print("Reached local maximum or plateau. No better neighbor found.")
            return current_board

        # Move to the best neighbor
        current_board = best_neighbor
        current_heuristic = best_heuristic
        iteration += 1

# Initial board state provided by the user
initial_board = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Goal board state (example solution)
goal_state = [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0]
]

print("Initial State:")
print_board(initial_board)

print("Goal State:")
print_board(goal_state)

# Solve using Hill Climbing
solution_board = hill_climbing(initial_board, goal_state)
print("Final Solution:")
print_board(solution_board)
