'''
solution for kSum problem
'''
'''
Given an array nums of n integers, an integer k, and target return an array of 
all the unique k numbers that sum to target
'''
import sys
from typing import List

ARRAY = []
K = 0
TARGET = 0

def readFile(file):
    try:
        with open(file, 'r') as infile:
            array  = infile.readline().rstrip('\n')
            k      = infile.readline().rstrip('\n')
            target = infile.readline().rstrip('\n')
        
        validateInput(array, k, target)
        return

    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_directory:
        print(is_directory)
    
    sys.exit(1)

def validateInput(array:str, k:str, target:str) -> None:
    global ARRAY, K, TARGET
    if array != '':
        ARRAY = [int(num) for num in array.split(',')]
    else:
        print("\033[91m\033[4mINVALID TEST CASE\033[0m: List cannot be empty\033[0m")
        sys.exit(1)

    K = int(k)
    TARGET = int(target)

    if K <= 0:
        print("\033[91m\033[4mINVALID TEST CASE\033[0m: k cannot be negative\033[0m")
        sys.exit(1)

def recurse(k, nums, start, end, subsum, result, target):
    if k == 2:
        l, r = start, end
        while l < r:
            sums = nums[l] + nums[r]
            if sums < target:
                l += 1
            elif sums > target:
                r -= 1
            else:
                result.append(subsum + [nums[l], nums[r]])
                while (l < r) and (nums[l] == nums[l + 1]):
                    l += 1
                l += 1
        return

    for i in range(start, end - k + 2):
        if i > start and nums[i] == nums[i - 1]:
            continue
        subsum.append(nums[i])
        recurse(k - 1, nums, i + 1, end, subsum, result, target - nums[i])
        subsum.pop()

def kSum():
    result = []
    recurse(K, sorted(ARRAY), 0, len(ARRAY) - 1, [], result, TARGET)

    print(f"The {K} unique numbers that sum to {TARGET} in {ARRAY} are: ")
    for array in result:
        print(array)

def main(arg):
    readFile(arg)
    kSum()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m\033[0m: python3 kSum.py [filename]")
        sys.exit(1)

    main(sys.argv[1])