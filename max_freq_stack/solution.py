'''
solution to maximum frequency stack
'''
import sys
from typing import List
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.counter = dict()
        self.frstack = defaultdict(list)
        self.most = 0        

    def push(self, val: int) -> None:
        self.counter[val] = 1 + self.counter.get(val, 0)
        self.most = max(self.most, self.counter[val])
        self.frstack[self.counter[val]].append(val)

    def pop(self) -> int:
        if self.most == 0:
            print("\033[91m\033[4mINVALID TEST CASE\033[0m: Cannot pop empty stack\033[0m")
            sys.exit(1)
            
        val = self.frstack[self.most].pop()
        self.counter[val] -= 1
        if len(self.frstack[self.most]) == 0:
            self.frstack.pop(self.most)
            self.most -= 1
        if self.counter[val] == 0:
            self.counter.pop(val)
        
        return val
        
def readFile(file_path:str):
    try:
        with open(file_path, 'r') as infile:
            commands = [command for command in infile.readline().split()]
            inputs   = [input for input in infile.readline().split()]
        
        if len(commands) != len(inputs):
            raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: number of commands and inputs must match\033[0m")
            
        for command, input in zip(commands, inputs):
            if command == "push": 
                if not input.isdigit():
                    raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: push a number\033[0m")
            elif command == "pop":
                if input != "[]":
                    raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: pop has no input\033[0m")
            else:
                raise Exception("\033[91m\033[4mINVALID TEST CASE\033[0m: push or pop\033[0m")
        return commands, inputs
                        
    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_dir:
        print(is_dir)
    except Exception as error:
        print(error)
    
    sys.exit(1)
    
def output(commands:List[str], inputs:List[str], freqstack:FreqStack) -> None:
    result = []
    for command, input in zip(commands, inputs):
        if command == "push":
            freqstack.push(int(input))
            result.append('null')
        elif command == "pop":
            val = freqstack.pop()
            result.append(val)
    print(result)
    
def main(arg:str):
    commands, inputs = readFile(arg)
    freqstack = FreqStack()
    print(f"{commands}\n{inputs}\n->")
    output(commands, inputs, freqstack)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m:\033[0m python3 max_freq_stack.py [filename]")
        sys.exit(1)
        
    main(sys.argv[1])