import sys

def longestCommonSubsequence(text1:str, text2:str) -> str:
    n1, n2 = len(text1), len(text2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    lcs = ""
    for i in range(n2):
        if dp[0][i] > dp[0][i + 1]:
            lcs += text2[i]    
        
    return dp[0][0], lcs

def readFile(file_path):
    try:
        with open(file_path, 'r') as infile:
            t1 = infile.readline().split('\n')[0]
            t2 = infile.readline()
        return t1, t2
    except FileNotFoundError as file_not_found:
        print(file_not_found)
        sys.exit(1)
    except IsADirectoryError as is_directory:
        print(is_directory)
        sys.exit(1)

def main(arg):
    t1, t2 = readFile(arg)
    length, lcs = longestCommonSubsequence(t1, t2)
    print(f"Longest common subsequence of `{t1}` `{t2}` is\n`{lcs}` of length {length}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[91m\033[4mARGUMENT COUNT ERROR\033[0m\n\033[0mUsage: python3 sudoku.py [filename]")
        sys.exit(1)
        
    main(sys.argv[1])