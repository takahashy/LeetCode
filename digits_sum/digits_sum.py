'''
Given an integer X and Y return the number of integers less than or equal to X
whose digits sum to Y


100, 4
{4 13 22 31 40}
'''
import sys

def readFile():
    pass

def digits_sum(x:int, y:int):
    digits = list(map(int, str(x)))
    n = len(digits)
    dp = {}
    result = []

    def digit_dp(ind, sums_to, tight, number):
        if sums_to == y:
            result.append((number))
            
        if ind == n:
            return 1 if sums_to == y else 0
        
        if (ind, sums_to, tight) in dp.keys():
            return dp[(ind, sums_to, tight)]
        
        limit = digits[ind] if tight else 9
        res = 0

        for digit in range(limit + 1):
            res += digit_dp(ind + 1, sums_to + digit, tight and (limit == digit), number + str(digit))
            # if res > 0 and sums_to == y:

        dp[(ind, sums_to, tight)] = res
        
        return res
    
    count = digit_dp(0, 0, True, "")
    print(f"There are {count} numbers that are less than {x} whose digits sum to {y}\n{result}")


def main(args):
    x, y = 0, 0
    if args:
        x, y = readFile()
    else:
        x, y = map(int, input("Enter two integers X and Y to find the number of integers less than X whose digits sum to Y: ").split())

    digits_sum(x, y)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("")