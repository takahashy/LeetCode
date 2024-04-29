'''
runtest
2024 Mar 13

Script that compares the solution output and the user solved output based on the
test cases in each directory. Can run all test cases in each subdirectory or unit 
test each subdirectory
    . subdirectory = name of problem
        -> solution.py = ground truth program
        -> [name].py   = user solved program
        -> test        = directory of testcases all with .in ext (test[num].in)

Also run unit or batch test cases for problems.
'''
import sys
from typing import List
from pathlib import Path
from subprocess import PIPE, Popen

CURR_DIR = Path.cwd()
PYTHON   = "python3"
SOLUTION = "solution.py"
TEST_DIR = "tests"
FAILED   = False

'''
PURPOSE: print path not found error if it doesn't exist
PARAMETERS: path object - path to a directory or file
            string      - directory or file
RETURNS: None
'''
def pathExists(path:Path, item:str) -> None:
    if not path.exists():
        print(f"\033[91m\033[4mPATH ERROR\033[0m: The {item} {path.name} does not exist\033[0m")
        sys.exit(1)
        

'''
PURPOSE: runs the passed in script on the test case and returns the output/error
PARAMETERS: path object - path to the script being run
            path object - path to the test case
RETURNS: output, error
'''
def outputProgram(script:Path, test_case:Path) -> tuple[bytes, bytes]:
    with Popen([PYTHON, script, test_case], stdout=PIPE, stderr=PIPE) as process:
        output, error = [out.decode('utf-8') for out in process.communicate()]
    return output, error

'''
PURPOSE: print the output of program and any errors
PARAMETERS: path object   - path to script program
            list of paths - paths to test cases
RETURNS: None
'''
def printOutput(script:Path, test_cases:List[Path]) -> None:
    global FAILED
    for test in test_cases:
        output, error = outputProgram(script, test)
        if error != "":
            print(f"\033[91m{test.name} FAILED\033[0m\n\033[4mExpected NO ERRORs but got\033[0m:\n{error}")
            FAILED = True
        else:
            print(f"\033[92m{test.name} RAN AS EXPECTED.\033[0m\n{output}")
        

'''
PURPOSE: compare the outputs of the user generated program and the solution on
         the test cases in that subdirectory
PARAMETERS: path object - path to subdirectory
RETURNS: None
'''
def compareOutput(problem:Path) -> None:
    global FAILED
    tests    = problem / TEST_DIR
    solution = problem / SOLUTION
    user_gen = (problem / problem.name).with_suffix('.py')
    
    # check valid paths
    pathExists(tests, "directory")
    pathExists(solution, "file")
    pathExists(user_gen, "file")
    
    print(f"\n\033[1m-------------------------- {problem.name} ---------------------------\033[0m")
    # for each test case compare the outputs of solution.py and user_generated
    test_cases = sorted([test for test in tests.iterdir()], key=lambda test: int(test.name.lstrip('test').rstrip('.in')))
    for test in test_cases:
        gt_out, _ = outputProgram(solution, test)
        us_out, e = outputProgram(user_gen, test)
        
        if e != "":
            print(f"\033[91m{test.name} FAILED\033[0m\n\033[4mExpected NO ERRORs but got\033[0m:\n{e}")
            FAILED = True
        elif gt_out != us_out:
            print(f"\033[91m{test.name} FAILED\033[0m\n\033[4mExpected\033[0m:\n{gt_out}\n\033[4mbut got\033[0m:\n{us_out}")
            FAILED = True
        else:
            print(f"\033[92m{test.name} PASSED. Same output\033[0m")    

'''
PURPOSE: run unit or batch tests on problem
PARAMETERS: list of paths - paths to the problem directory
            string        - "solution" or "user"
            string        - "all" or number
RETURNS: None
'''
def runTest(problems:List[Path], program:str, test_case:str) -> None:
    for problem in problems:
        print(f"\n\033[1m-------------------------- {problem.name} ---------------------------\033[0m")
        tests = problem / TEST_DIR
        pathExists(tests, "directory")
        test_cases = []
            
        if test_case == "all":
            # batch tests
            for test in tests.iterdir():
                test_cases.append(test)
                test_cases.sort(key=lambda test: int(test.name.lstrip('test').rstrip('.in')))
        elif test_case.isdigit():
            # check test case exists
            pattern = '*' + test_case + '.in'
            for file in tests.glob(pattern):
                test_cases.append(file)
            
            if len(test_cases) == 0:
                print(f"\033[91m\033[4mINVALID TEST INPUT\033[0m: Test #{test_case} does not exist in {problem.name}\033[0m")
                sys.exit(1)
        else:
            print("\033[91m\033[4mINVALID COMMAND\033[0m: INDEX 3 should be 'all' or a test number\033[0m")
            sys.exit(1)

        # run solution or user generated program
        if program == "solution":
            solution = problem / SOLUTION
            pathExists(solution, "file")
            printOutput(solution, test_cases)       
        elif program == "user":
            user_gen  = (problem / problem.name).with_suffix('.py')
            pathExists(user_gen, "file")
            printOutput(user_gen, test_cases)
        else:
            print("\033[91m\033[4mINVALID COMMAND\033[0m: INDEX 2 should be 'solution' or 'user'\033[0m")
            sys.exit(1)
        

'''
PURPOSE: run all test cases or a specific subdirectory
PARAMETERS: string - 'all' or 'name' of a subdirectory to run
RETURNS: None
'''
def main(args:str) -> None:
    tests = []
    
    if args[0] == "all":
        # append all subdirectory abs paths to tests
        for items in CURR_DIR.iterdir():
            if items.is_dir() and (items != CURR_DIR / ".git"):
                tests.append(items) 
    else:
        # append specified subdir abs path to tests
        subdir = CURR_DIR / args[0]
        if subdir.exists() and subdir.is_dir():
            tests.append(subdir)
        else:
            print("\033[91m\033[4mINVALID COMMAND\033[0m: INDEX 1 should be an existing directory\033[0m")
            sys.exit(1)
    
    if len(args) > 1:
        # running unit or batch tests
        runTest(tests, args[1], args[2])
    else:
        # comparing outputs
        for test in tests:
            compareOutput(test)   
        print()
    
    # final check
    if FAILED:
        print(f"\033[91mSome tests failed. Check above\033[0m")
    else:
        print(f"\033[92mALL TESTS PASSED!")



if __name__ == '__main__':
    if (len(sys.argv) != 2) and (len(sys.argv) != 4):
        print(f"\033[91m\033[4mUsage\033[0m\033[0m: python3 runtests.py [all|dir_name] solution|user [all|number]")
        sys.exit(1)
        
    main(sys.argv[1:])
    
    
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Pathlib methods
    p.parent    - get the parent directory of p
    p.suffix    - get the extension of file(.txt, .pdf, .cpp)
    p.name      - get the name of the file including extension or directory
    p.iterdir() - iterate through all files and subdirectories in `p` directory
    p.is_file() - check if `p` is a file
    p.is_dir()  - check if `p` is a directory
    p.exists()  - check whether `p` exists
    p.cwd()     - current working directory (NOTE: Doesn't mean directory of file)
    p.glob(ptn) - given a pattern searches in the current directory (ptn = '*.py')
    p.rglob(ptn)- given a pattern searches in current and subdirectories
    p.rename(np)- rename the p file path to np file path
    p / "str.py"- returns the path object of "p/str.py" 
    
subprocess module
    Popen   - give control over what command to execute, what input to give, and
              output/error to return
              
              PARAMS: args   - list of command line arguments (ex: ['python3', 'runtests.py', 'all'])
                      stdin  - input usually equal to PIPE or some file
                      stdout - output PIPE
                      stderr - error PIPE
    
    Popen.communicate - returns output and error of program run but usually decode
                        to get readable output
                        out.decode('utf-8') for out in Popen.communicate()
                 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''