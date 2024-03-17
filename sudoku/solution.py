'''
2024 Mar 10
Solution for sudoku
'''
from typing import List
import sys

BOARD = []
    
def checkRow(row, val):
    return True if (val not in BOARD[row]) else False

def checkCol(col, val):
    for i in range(9):
        if val == BOARD[i][col]:
            return False
    return True

def checkSub(row, col, val):
    st_row = row // 3 * 3
    st_col = col // 3 * 3
    for i in range(st_row, st_row + 3):
        for j in range(st_col, st_col + 3):
            if val == BOARD[i][j]:
                return False
    return True

def validVal(row, col, val):
    return checkRow(row, val) and checkCol(col, val) and checkSub(row, col, val)

def solved(pair):
    for i in range(9):
        for j in range(9):
            if BOARD[i][j] == 0:
                pair.clear()
                pair.append(i)
                pair.append(j)
                return False
    return True

def solvedSudoku():
    global BOARD
    empty = []
    if solved(empty): 
        return True
    row, col = empty[0], empty[1]

    for val in range(1,10):
        if validVal(row, col, val):
            BOARD[row][col] = val
            if solvedSudoku(): 
                return True
            BOARD[row][col] = 0 

    return False

def readBoard(file):
    global BOARD
    with open(file, 'r') as infile:
        for line in infile:
            if line != '\n':
                row = [int(num) for num in line.split()]
                BOARD.append(row)            

def printBoard():
    for rows in BOARD:
        for val in rows:
            print(val, end=' ')
        print()

def main():
    try:
        if len(sys.argv) < 2:
            print("\033[91mARGUMENT COUNT ERROR\n\033[0mUsage: python3 solution.py [filename]")
            sys.exit(1)
            
        readBoard(sys.argv[1])
        
        if solvedSudoku():
            print('\033[92mSOLVED:\033[0m')
        else:
            print('\033[91mCANNOT BE SOLVED:\033[0m')
        printBoard()
        
    except FileNotFoundError as file_not_found:
        print(file_not_found)
        sys.exit(1)
    except IsADirectoryError as directory:
        print(directory)
        sys.exit(1)
        

if __name__ == '__main__':
    main()