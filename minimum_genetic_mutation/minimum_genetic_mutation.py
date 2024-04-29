'''
A gene string can be represented by an 8-character long string, with choices 
from 'A', 'C', 'G', and 'T'. Suppose we need to investigate a mutation from a 
gene string startGene to a gene string endGene where one mutation is defined as
one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. 
A gene must be in bank to make it a valid gene string. Given the two gene 
strings startGene and endGene and the gene bank bank, return
the minimum number of mutations needed to mutate from startGene to endGene. 
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included
in the bank.
'''
import sys
from typing import List
from collections import deque

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    q = deque([(startGene, 0)])
    while q:
        gene, depth = q.popleft()
        if gene == endGene:
            return depth
        
        for i in range(8):
            for base in ['A','C','G','T']:
                new_gene = gene[:i] + base + gene[i + 1:]
                if new_gene in bank:
                    q.append((new_gene, depth + 1))
                    bank.remove(new_gene)
    return -1

def readFile(file):
    try:
        with open(file, 'r') as infile:
            start = infile.readline().rstrip('\n').split()[1]
            end   = infile.readline().rstrip('\n').split()[1]
            bank  = infile.readline().rstrip('\n').split()[1:]
        return start, end, bank
            
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_dir:
        print(is_dir)
    sys.exit(1)

def validateInput(start, end, bank):
    try:
        if (len(start) != 8) or (len(end) != 8):
            raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: Genes are composed of 8 bases here")
        if len(bank) == 0:
            raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: Bank cannot be empty")
        
        genes = [start, end] + bank
        for gene in genes:
            for base in gene:
                if base not in ['A', 'C', 'T', 'G']:
                    raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: There are 4 types of bases: A, C, G, T")

    except Exception as testCaseInvalid:
        print(testCaseInvalid)
        sys.exit(1)

def main(arg):
    start, end, bank = readFile(arg)
    validateInput(start, end, bank)
    mutations = minMutation(start, end, bank)

    if mutations == -1:
        print(f"The '{start}' cannot be mutated to '{end}' given the bank")
    else:
        print(f"The '{start}' can be mutated into '{end}' in {mutations} mutations")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m:\033[0m python3 minimum_genetic_mutation.py [testfile]")
        sys.exit(1)

    main(sys.argv[1])