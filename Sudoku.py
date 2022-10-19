from pprint import pprint


def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c

    return None, None  

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
   
    row, col = find_next_empty(puzzle)

   
    if row is None: 
        return True 
    

    for guess in range(1, 10): 

        if is_valid(puzzle, guess, row, col):

            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True
        

        puzzle[row][col] = -1


    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
