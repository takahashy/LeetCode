'''
solution for k pairs with smallest sums
'''
import sys
import heapq
from typing import List

def find_k_pairs(nums1:List[int], nums2:List[int], k:int) -> List[List[int]]:
    n1, n2 = len(nums1), len(nums2)
    min_heap, result = [], []

    for i in range(min(n1, k)):
        heapq.heappush(min_heap, (nums1[i] + nums2[0], 0))
        
    while k > 0:
        sm_sum, ind2 = heapq.heappop(min_heap)
        val1 = sm_sum - nums2[ind2]
        result.append([val1, nums2[ind2]])

        if ind2 + 1 < n2:
            heapq.heappush(min_heap, (val1 + nums2[ind2 + 1], ind2 + 1))
        k -= 1
    
    return result


def validateInput(snum1:List[str], snum2:List[str], sk:str):
    if snum1 != '':
        num1 = [int(num) for num in snum1.split()]
    else:
        print("\033[91m\033[4mINVALID TEST CASE\033[0m: List cannot be empty\033[0m")
        sys.exit(1)
    
    if snum2 != '':
        num2 = [int(num) for num in snum2.split()]
    else:
        print("\033[91m\033[4mINVALID TEST CASE\033[0m: List cannot be empty\033[0m")
        sys.exit(1)

    if 0 <= int(sk) <= len(num1) * len(num2):
        k = int(sk)
    else:
        print("\033[91m\033[4mINVALID TEST CASE\033[0m: 0 <= k <= num1.length * num2.length")
        sys.exit(1)
        
    return num1, num2, k

def readFile(file_path:str) -> tuple[int, int, int]:
    try:
        with open(file_path, 'r') as infile:
            num1 = infile.readline().rstrip('\n')
            num2 = infile.readline().rstrip('\n')
            k    = infile.readline().rstrip('\n')
        return num1, num2, k        
            
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_dir:
        print(is_dir)
    sys.exit(1)

def main(arg) -> None:
    snum1, snum2, sk = readFile(arg)
    num1, num2, k = validateInput(snum1, snum2, sk)
    k_pairs = find_k_pairs(num1, num2, k)
    print(f"The first {k} pairs with smallest sum of \n{num1} and {num2} are\n{k_pairs}")
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m:\033[0m python3 k_smallest_sum_pairs.py [filename]")
        sys.exit(1)
        
    main(sys.argv[1])