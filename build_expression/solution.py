'''
solution for build expression
'''
import sys
from typing import Tuple

TOLERANCE = 1e-6


def builtExpression(nums, target, mem, ways) -> Tuple[bool, str]:
    n = len(nums)
    if n == 1:
        if abs(nums[0][0] - target) < TOLERANCE:
            ways.append(nums[0][1])
            return True
        return False
    
    values = tuple(sorted([num[0] for num in nums]))
    if values in mem:
        return mem[values]

    res = False
    for i in range(n):
        for j in range(i + 1, n):
            remainder = nums[:i] + nums[i + 1:j] + nums[j + 1:]

            for val, exp in allOperations(nums[i], nums[j]):
                built = builtExpression([(val, exp)] + remainder, target, mem, ways)
                res = res or built

    mem[values] = res
    return res


def allOperations(a, b):
    val_a, exp_a = a
    val_b, exp_b = b

    operations = [
        (val_a + val_b, f"({exp_a} + {exp_b})"),
        (val_a - val_b, f"({exp_a} - {exp_b})"),
        (val_b - val_a, f"({exp_b} - {exp_a})"),
        (val_a * val_b, f"{exp_a} * {exp_b}")
    ]    
    
    if val_a != 0:
        operations.append((val_b / val_a, f"({exp_b}/{exp_a})"))
    if val_b != 0:
        operations.append((val_a / val_b, f"({exp_a}/{exp_b})"))

    return operations



def readFile(file_path):
    try:
        with open(file_path, 'r') as infile:
            nums = [int(num) for num in infile.readline().split()]
            target = int(infile.readline().rstrip('\n'))
        
        return nums, target
    
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_dir:
        print(is_dir)
    sys.exit(1)


def main(arg):
    nums, target = readFile(arg)
    cards = [(num, str(num)) for num in nums]
    mem = dict()
    ways = []
    built = builtExpression(cards, target, mem, ways)
    
    if built:
        print(f"Given {nums}, {target} can be built with:")
        for exp in ways:
            print(exp)
    else:
        print("No expression found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m:\033[0m python3 build_expression.py [filename]")
        sys.exit(1)
        
    main(sys.argv[1])