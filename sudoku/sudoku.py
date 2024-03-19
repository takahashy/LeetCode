'''
solving a sudoku board. Given a 9 x 9 board in a file solve the sudoku if it
can be solved and return that board
'''
import sys
from collections import deque

class Sudoku:
    def __init__(self):
        self.board = []
        
    # read the input file and store into board
    def readFile(self, file):
        try:
            with open(file, 'r') as infile:
                for line in infile:
                    if line != '\n':
                        self.board.append(line.split())
        except FileNotFoundError as file_not_found:
            print(file_not_found)
            sys.exit(1)
        except IsADirectoryError as directory:
            print(directory)
            sys.exit(1) 
                    
    # check that the value is not in the row of the board
    def __checkRow(self, row, val):
        return True if val not in self.board[row] else False
            
    # check that the value is not in the column of the board
    def __checkCol(self, col, val):
        for i in range(9):
            if val == self.board[i][col]:
                return False
        return True
    
    # check that the value is not in the 3x3 subgrid of the board
    def __checkSub(self, row, col, val):
        st_row = row // 3 * 3
        st_col = col // 3 * 3
        for i in range(st_row, st_row + 3):
            for j in range(st_col, st_col + 3):
                if val == self.board[i][j]:
                    return False
        return True
    
    def __validVal(self, row, col, val):
        return self.__checkRow(row, val) and self.__checkCol(col, val) and self.__checkSub(row, col, val)
    
    # check if there are any 0s in the board
    def __solved(self, q):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '0':
                    q.append((i,j))
                    return False
        return True
        
    # if the board is not solved try values from 1-9 and backtrack        
    def solveSudoku(self):
        q = deque()
        if (self.__solved(q)):
            return True
        
        i, j = q.popleft()
        for val in range(1,10):
            if self.__validVal(i, j, str(val)):
                self.board[i][j] = str(val)
                if self.solveSudoku():
                    return True
                self.board[i][j] = '0'
        return False
                    
    def printBoard(self):
        for rows in self.board:
            for num in rows:
                print(num, end=' ')
            print()

def main(arg):
    sudoku = Sudoku()
    sudoku.readFile(arg)
    
    if sudoku.solveSudoku():
        print("\033[92mSOLVED:\033[0m")
    else:
        print('\033[91mCANNOT BE SOLVED:\033[0m')
    sudoku.printBoard()
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
            print("\033[91mARGUMENT COUNT ERROR\n\033[0mUsage: python3 sudoku.py [filename]")
            sys.exit(1)
            
    main(sys.argv[1])            

