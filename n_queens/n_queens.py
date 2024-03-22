'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other. Queens can move horizontally, 
vertically, and diagonally any number of spaces

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.
'''
import sys
from typing import List


def readFile(path_file:str):
    try:
        with open(path_file, 'r') as infile:
            n = infile.readline()
        
        if (not n.isdigit()) and (int(n) <= 0):
            raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: Must be a number greater than 0\033[0m")
        return int(n)
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_dir:
        print(is_dir)
    except Exception as error:
        print(error)
    sys.exit(1)
        
def nQueens(n:int) -> List[List[str]]:
    result = []
    board  = [['.'] * n for _ in range(n)]
    
    col_set, diag_set, anti_diag_set = set(), set(), set()
    def backtrack(row):
        if row == n:
            result.append(["".join(row) for row in board])
        
        for col in range(n):
            diag = row - col
            anti = row + col
            if (not col in col_set) and (not diag in diag_set) and (not anti in anti_diag_set):
                col_set.add(col)
                diag_set.add(diag)
                anti_diag_set.add(anti)
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
                col_set.remove(col)
                diag_set.remove(diag)
                anti_diag_set.remove(anti)
    
    backtrack(0)
    return result

def printBoards(boards, n):
    print(f"There are {len(boards)} possible solutions to {n}-Queens")
    i = 1
    for board in boards:
        print(f"\033[1m\033[4m{i}\033[0m\033[0m")
        for row in board:
            for val in row:
                print(val, end=' ')
            print()
        print()
        i += 1

def main(arg):
    n = readFile(arg)
    boards = nQueens(n)
    printBoards(boards, n)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m:\033[0m python3 n_queens.py [filename]")
        sys.exit(1)
    
    main(sys.argv[1])