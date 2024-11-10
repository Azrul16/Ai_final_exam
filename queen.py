import numpy as np

# Define the initial board state
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

# Goal state (not used directly in optimization)
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

def count_conflicts(board):
    """Count the number of pairs of queens attacking each other."""
    conflicts = 0
    size = len(board)
    # Check for column and diagonal conflicts
    for col in range(size):
        queens_in_col = []
        for row in range(size):
            if board[row][col] == 1:
                queens_in_col.append(row)

        # Count conflicts within the same column
        conflicts += len(queens_in_col) * (len(queens_in_col) - 1) // 2

        # Check diagonal conflicts
        for i in range(len(queens_in_col)):
            for j in range(i + 1, len(queens_in_col)):
                if abs(queens_in_col[i] - queens_in_col[j]) == abs(i - j):
                    conflicts += 1

    return conflicts

def hill_climbing(board):
    """Perform the hill climbing algorithm to solve the 8-queens problem."""
    current_board = [row[:] for row in board]
    current_conflicts = count_conflicts(current_board)
    print(f"Initial board:\n{np.array(current_board)}\nConflicts: {current_conflicts}\n")

    iterations = 0

    while current_conflicts > 0:
        next_board = None
        next_conflicts = current_conflicts

        # Try moving each queen in each column to each row
        for col in range(len(current_board)):
            for row in range(len(current_board)):
                if current_board[row][col] == 1:
                    # Create a copy of the current board
                    new_board = [r[:] for r in current_board]
                    
                    # Move queen to a new row (found in the same column)
                    new_board[row][col] = 0  # Remove current queen
                    
                    for new_row in range(len(current_board)):
                        if new_row != row:
                            # Place the queen in the new row
                            new_board[new_row][col] = 1  # Place queen in new row

                            # Count the conflicts for the new board
                            conflicts = count_conflicts(new_board)

                            # If this new board has less conflicts, update it
                            if conflicts < next_conflicts:
                                next_board = new_board
                                next_conflicts = conflicts

        # If no better board was found, we are stuck
        if next_board is None:
            print("Stuck in a local minimum!")
            break

        # Update to the next state
        current_board = next_board
        current_conflicts = next_conflicts
        iterations += 1
        
        print(f"Iteration {iterations}:\n{np.array(current_board)}\nConflicts: {current_conflicts}")

    if current_conflicts == 0:
        print("Solution found!")
        print(np.array(current_board))
    else:
        print("No solution found.")

# Run the hill climbing algorithm with the initial board
hill_climbing(initial_board)
