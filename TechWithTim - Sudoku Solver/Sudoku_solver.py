"""
We have a matrix to represent the entire sudoku grid

example:
[[9, 4, 0, 0, 3, 1, 0, 0, 7],
 [6, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 2, 0, 0, 9],
 [0, 7, 0, 0, 6, 0, 2, 0, 0],
 [0, 9, 0, 0, 4, 0, 8, 0, 0],
 [0, 3, 0, 0, 0, 0, 5, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 8, 0, 0, 8, 1],
 [0, 0, 0, 0, 0, 0, 0, 4, 0]]

We can solve it the naive way by trying every possible combination
 this would equate to 9^81 = 1.96e77 possibilities

Or we can use BACKTRACKING
1.) pick an empty square
2.) try all numbers 1-9
3.) as soon as we find a number that fits in the square (checking row, column and square sudoku rule)
    we use that number and don't look for the other possibilities
4.) repeat (we go to the next empty square)

let's imagine that we tried to fill the first row with 9, 4, 2, 5, 3, 1, 6, 8, 9
 we filled in the 2, 5, 6 and 8
 we find that the 8 is in the same column as another 8 so it doesn't work
 so that's not a valid solution

5.) backtrack

we erase the 8 and go back a step to the 6 and remove it from the possibilities
 thus we try 7, 8 and 9 and none of those work and none of the other either
 so we backtrack again
 no we go back to the 5 and we try a different number, for example 8

 Now we repeat that until eventually we recursively get the solution that will work
 thus eliminating all the naive solutions that would have never worked and
 cutting down the number of 'naively' checked solutions by a drastic amount
"""

board = [
 [7, 8, 0, 4, 0, 0, 1, 2, 0],
 [6, 0, 0, 0, 7, 5, 0, 0, 9],
 [0, 0, 0, 6, 0, 1, 0, 7, 8],
 [0, 0, 7, 0, 4, 0, 2, 6, 0],
 [0, 0, 1, 0, 5, 0, 9, 3, 0],
 [9, 0, 4, 0, 6, 0, 0, 0, 5],
 [0, 7, 0, 3, 0, 0, 0, 1, 2],
 [1, 2, 0, 0, 0, 7, 4, 0, 0],
 [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


"""
- first we need to make a function that will pick an empty square
- next is trying all the numbers
- we need a function that will check whether the number is valid in the square
- then we need to repeat
- and finally a function that will handle the backtracking, not valid go back and reset to 0
"""

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

#print_board(board)


def find_empty(bo):
    # looking for an empty square (denoted by 0)
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    
    # if there is no blank squares
    return None # or False


def valid(bo, num, pos):
    # function to check whether the chose number is a possible valid solution to a given position

    # bo - board
    # num - chosen number
    # position - tuple (i, j)

    # we need to check row, column and square

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            # iterates over the row (column) and excludes the position for which we're checking
            #  because in the testing function we're first puttin in the number and then validating 
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != 0:
            # same thing as before but for columns
            return False
        
    # Check box
    """
    to determine in which box we are we use integer division //

    [[(0, 0), (0, 1), (0, 2)],
     [(1, 0), (1, 1), (1, 2)],
     [(2, 0), (2, 1), (2, 2)]]

    then we just loop through that box
    """
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            # we're multiplying by 3 because box (0, 2) has indexes ((0-2), (6-8))
            if bo[i][j] == num and (i, j) != pos:
                return False

# All of this code can be written so much faster with numpy, do tomorrow

"""
Now for the function that will solve the board and backtrack, we do this recursively
"""

def solve(bo):
    # our base case for the algorithm is that it stops when the whole board is full
    #  - i.e. there's no 0's in the board anymore
    # the way the backtracking algorithm works is that when we get to the bottom of the board
    #  we've actually found the solution
    
    # this is our base case of the algorithm, once we reach this case we're done
    find = find_empty(bo)
    if not find:
        # We've found the solution end the function
        return True
    else:
        row, col = find
        # if the base case isn't satisfied, the find_empty function finds an empty square

    for i in range(1, 10):

        # for seeing how the backtracking works
        #print(bo)

        # we try if it's a valid solution
        if valid(bo, i, (row, col)):
            bo[row][col] = i # we set that value in the board if valid

            # our recursive/backtracking loop
            # if after one last call the function triggers the base case, it means
            #  that we've solved it, so it returns True
            # else it backtracks by setting the value to 0 at that position
            
            # it tries until it find a possible value from 1-9
            #  if it doesn't find it it return False, thus the solve(bo) isn't True
            #  for the layer above, and it returns up until the point it find the right path
            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

#print_board(board)
#solve(board)
#print("\n" + "-"*20 + "\n")
#print_board(board)