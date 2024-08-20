'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length): 
    Initializes an array-like data structure with the given length. 
    Initially, each element equals 0.

void set(index, val):
    sets the element at the given index to be equal to val.

int snap():
    takes a snapshot of the array and returns the snap_id: the total number 
    of times we called snap() minus 1.

int get(index, snap_id):
    returns the value at the given index, at the time we took the snapshot 
    with the given snap_id

snap_id = 0
{
    index : [(snap_id, value), (snap_id, value)]

    0 : [(0,0), (2,1)]
    1 : [(0,0), (1,3)]
}

0: [0, 0]
1: [0, 3]
2: [1, 3] 
'''
import sys

class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.snapshot = {i : [(0,0)] for i in range(length)}

    def set(self, index: int, val: int) -> None:
        snap = self.snapshot[index][-1][0]

        if snap != self.snap_id:
            self.snapshot[index].append((self.snap_id, val))
        else:
            self.snapshot[index][-1] = (snap, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.snap_id:
            print("\033[91m\033[4mINVALID TEST CASE\033[0m: snap id is greater than snaps\033[0m")
            sys.exit(1)

        array = self.snapshot[index]
        l, r = 0, len(array) - 1

        while l <= r:
            m = (l + r) // 2
            if array[m][0] == snap_id:
                return array[m][1]
            elif snap_id < array[m][0]:
                r = m - 1
            else:
                l = m + 1

        return array[l - 1][1]

def readFile(file):
    try:
        with open(file, 'r') as infile:
            length = int(infile.readline().rstrip('\n'))
            commands = infile.readline().split()
            values = [(string.lstrip() + ']' if ']' not in string else string.lstrip()) for string in infile.readline().rstrip('\n').split("],")]

        return validateInput(length, commands, values)

    except FileNotFoundError as file_not_found:
        print(file_not_found)
    except IsADirectoryError as is_directory:
        print(is_directory)

    sys.exit(1)

def validateInput(length, commands, values):
    if len(commands) != len(values):
        print("\033[91m\033[4mINVALID TEST CASE\033[0m: Number of commands and values should be same\033[0m")
        sys.exit(1)

    vals = []
    for value in values:
        val = value[1:-1]
        if val == '':
            vals.append([]) 
        else:
            ind, val = list(map(int,val.split(',')))   
            if ind >= length:
                print("\033[91m\033[4mINVALID TEST CASE\033[0m: Index exceeds length\033[0m")
                sys.exit(1)

            vals.append([ind,val])
            
    return length, zip(commands, vals)

def main(arg):
    length, zipped = readFile(arg)
    snap = SnapshotArray(length)
    result = []

    for command, value in zipped:
        method = getattr(snap, command)

        if value:
            res = method(value[0], value[1])
        else:
            res = method()
        result.append(res)

    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[91m\033[4mUsage\033[0m\033[0m: python3 snapshot.py [filename]")
        sys.exit(1)

    main(sys.argv[1])