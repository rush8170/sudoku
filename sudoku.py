
def print_solution(sudoku):
    for i in sudoku:
        for j in i:
            print(j,end=' ')
        print("")
    print("\n")

def unassigned_cell(sudoku,row,col):
    return sudoku[row][col]==True

def find_next_empty_location(sudoku,l):
    for i in range(9):
        for j in range(9):
            if(sudoku[i][j]==0):
                l[0] = i
                l[1] = j
                return True
    return False

def is_feasible_row(sudoku,row,val):
    for i in range(9):
        if sudoku[row][i]==val:
            return False
    return True

def is_feasible_col(sudoku,col,val):
    for i in range(9):
        if sudoku[i][col]==val:
            return False
    return True

def is_feasible_block(sudoku,row,col,val):
    for i in range(row,row+3):
        for j in range(col,col+3):
            if(sudoku[i][j]==val):
                return False
    return True


def is_feasible(sudoku,row,col,val):
    return is_feasible_row(sudoku,row,val) and is_feasible_col(sudoku,col,val) and is_feasible_block(sudoku,row-row%3,col-col%3,val)

def solve_sudoku(sudoku):
    l =[0,0]
    if(find_next_empty_location(sudoku,l)==False):
        return True
    for i in range(1,10):
        if(is_feasible(sudoku,l[0],l[1],i)):
            sudoku[l[0]][l[1]]=i
            if solve_sudoku(sudoku)==True:
                return True
            sudoku[l[0]][l[1]]=0
    return False

if __name__ =='__main__':
    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],  
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],  
            [0, 0, 0, 0, 0, 0, 0, 7, 4],  
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    if(solve_sudoku(sudoku)==True):
        print_solution(sudoku)
    else:
        print('Solution does not exist')