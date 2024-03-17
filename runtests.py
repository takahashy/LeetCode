'''
2024 Mar 13

Script that compares the solution output and the user solved output based on the
test cases in each directory. Can run all test cases in each subdirectory or unit 
test each subdirectory
    . subdirectory = name of problem
        -> solution.py = ground truth program
        -> [name].py   = user solved program
        -> test        = directory of testcases all with .in ext (test[num].in)
'''
import sys
from pathlib import Path
from subprocess import PIPE, Popen

CURR_DIR = Path.cwd()
SOLUTION = "solution.py"
TEST_DIR = "tests"
FAILED   = False


'''
PURPOSE: compare the outputs of the user generated program and the solution on
         the test cases in that subdirectory
PARAMETERS: path object - path to subdirectory
RETURNS: None
'''
def runTest(problem:Path) -> None:
    global FAILED
    tests    = problem / TEST_DIR
    solution = problem / SOLUTION
    user_gen = (problem / problem.name).with_suffix('.py')
    
    print(tests.name, solution.name, user_gen.name)
    # check solution exists and get output
    # check problem.py exists and get output with error
    # for each test case in tests
        # if error on problem.py failed 
        # compare the output and if different failed


'''
PURPOSE: print path not found error if it doesn't exist
PARAMETERS: path object - path to a directory or file
            string      - directory or file
RETURNS: None
'''
def pathNotFound(path:Path, file_dir):
    pass

'''
PURPOSE: run all test cases or a specific subdirectory
PARAMETERS: string - 'all' or 'name' of a subdirectory to run
RETURNS: None
'''
def main(arg:str) -> None:
    tests = []
    
    # append all subdirectory abs paths to tests
    if arg == "all":
        for items in CURR_DIR.iterdir():
            if items.is_dir() and (items != CURR_DIR / ".git"):
                tests.append(items)
    
    # append specified subdir abs path to tests
    else:
        subdir = CURR_DIR / arg
        if subdir.exists() and subdir.is_dir():
            tests.append(subdir)
    
    # run each subdir
    for test in tests:
        runTest(test)
    
    # final check
    if FAILED:
        print(f"\n\033[91mSome tests failed. Check above\033[0m")
    else:
        print(f"\n\033[92mALL TESTS PASSED!\n")



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"\033[91m\033[4mUsage\033[0m\033[0m: python3 runtests.py [all|dir_name]")
        sys.exit(1)
        
    main(sys.argv[1])