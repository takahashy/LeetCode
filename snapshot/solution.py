'''
solution for snapshot array
'''
import sys

class SnapshotArray:
    def __init__(self, length: int):
        self.array = [0] * length
        self.snap_id = -1
        self.indSnap = [[-1] for _ in range(length)]
        self.indVal  = [[0]  for _ in range(length)]
        self.changed = set()
        
    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.changed.add(index)
        
    def snap(self) -> int:
        self.snap_id += 1
        
        for ind in self.changed:
            self.indSnap[ind].append(self.snap_id)
            self.indVal[ind].append(self.array[ind])
        self.changed.clear()
            
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.snap_id + 1:
            print("\033[91m\033[4mINVALID TEST CASE\033[0m: snap id is greater than snaps\033[0m")
            sys.exit(1)

        snaps = self.indSnap[index]
        l, r = 0, len(snaps) - 1
        
        while l <= r:
            m = (l + r) // 2
            if snap_id == snaps[m]:
                return self.indVal[index][m]
            elif snap_id < snaps[m]:
                r = m - 1
            else:
                l = m + 1
        
        return self.indVal[index][l - 1]

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