'''
solution to n queens problem
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
    
def solveNQueens(n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        def safe(x,y):
            for i in range(x):
                for j in range(n):
                    if board[i][j] == 'Q':
                        if (y == j) or (y == j + x - i) or (y == j - x + i): 
                            return False
            return True

        def backtrack(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if safe(i,j):
                    board[i][j] = 'Q'
                    backtrack(i + 1)
                    board[i][j] = '.'

        backtrack(0)
        return res
    
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
    boards = solveNQueens(n)
    printBoards(boards, n)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m:\033[0m python3 n_queens.py [filename]")
        sys.exit(1)
    
    main(sys.argv[1])