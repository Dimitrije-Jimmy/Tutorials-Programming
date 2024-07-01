import numpy as np

# By using NumPy's array operations, your solver should be more efficient and take advantage
#  of vectorized computations, which will significantly speed up the solving process.

# Convert the board to a NumPy array
board = np.array([
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
])


# 1.) 'print_board' function can remain the same since it's focused on printing.
def print_board(bo):
    # just for nice formatting in the terminal

    for i in range(len(bo)):
        # just for printing the lines between rows to make it more readable
        if (i % 3 == 0) and (i != 0):
            print("---------------------")

        for j in range(len(bo[0])):
            # same thing for the vertical lines
            if (j % 3 == 0) and (j != 0):
                print("| ", end="")
                # the end="" means that it doesn't add the \n at the end to go to now row
                #  basically "stay on the same line"
            
            if j == 8:
                # if it's the final column no need for space at the end
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")  


# 2.) 'find_empty' function can be rewritten using NumPy's np.where function:
def find_empty(bo):
    empty_positions = np.where(bo == 0)
    if len(empty_positions[0]) > 0:
        return empty_positions[0][0], empty_positions[1][0]
    return None


# 3.) 'valid' function can be optimized using NumPy's indexing capabilities:
def valid(bo, num, pos):
    # Check row
    if num in bo[pos[0], :]:
        return False

    # Check column
    if num in bo[:, pos[1]]:
        return False

    # Check box
    box_x = (pos[1] // 3) * 3
    box_y = (pos[0] // 3) * 3
    if num in bo[box_y:box_y+3, box_x:box_x+3]:
        return False

    return True

# 4.) 'solve' function can remain relatively unchanged, but you can leverage the NumPy array for assignment:
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row, col] = i
            if solve(bo):
                return True
            bo[row, col] = 0

    return False

# print_board(board)
# solve(board)
# print("\n" + "-"*20 + "\n")
# print_board(board)