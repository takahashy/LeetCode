'''
Given an array nums of n integers, an integer k, and target return an array of 
all the unique k numbers that sum to target
'''
import sys
from typing import List

class Solution:
    def __init__(self, file):
        self.array = []
        self.target, self.k = -1, -1
        self.__readFile(file)

    def __readFile(self, file):
        try:
            with open(file, 'r') as infile:
                array  = infile.readline().rstrip('\n')
                k      = infile.readline().rstrip('\n')
                target = infile.readline().rstrip('\n')
            
            self.__validateInput(array, k, target)
            return

        except FileNotFoundError as file_not_found:
            print(file_not_found)
        except IsADirectoryError as is_directory:
            print(is_directory)
        
        sys.exit(1)

    def __validateInput(self, array:str, k:str, target:str) -> None:
        if array != '':
            self.array = [int(num) for num in array.split(',')]
        else:
            print("\033[91m\033[4mINVALID TEST CASE\033[0m: List cannot be empty\033[0m")
            sys.exit(1)

        self.k = int(k)
        self.target = int(target)

        if self.k <= 0:
            print("\033[91m\033[4mINVALID TEST CASE\033[0m: k cannot be negative\033[0m")
            sys.exit(1)

    def __recurse(self, result, array, k, target, subarray, start, end):
        if k == 2:
            while start < end:
                num1, num2 = array[start], array[end]
                if num1 + num2 == target:
                    result.append(subarray + [num1, num2])
                    while (start < end) and (num1 == array[start]):
                        start += 1
                elif num1 + num2 < target:
                    start += 1
                else:
                    end -= 1

        for i in range(start, end - k + 2):
            if (i > start) and (array[i] == array[start]):
                continue
            self.__recurse(result, array, k - 1, target - array[i], subarray + [array[i]], i + 1, end)

    def kSum(self):
        result = []
        self.__recurse(result, sorted(self.array), self.k, self.target, [], 0, len(self.array) - 1)

        print(f"The {self.k} unique numbers that sum to {self.target} in {self.array} are: ")
        for array in result:
            print(array)

def main(arg):
    solve = Solution(arg)
    solve.kSum()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m\033[0m: python3 kSum.py [filename]")
        sys.exit(1)

    main(sys.argv[1])