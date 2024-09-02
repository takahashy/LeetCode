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

ARGC     = len(sys.argv)
CURR_DIR = Path(__file__).parent
PYTHON   = "python3"
SOLUTION = "solution.py"
TEST_DIR = "tests"
FAILED   = False

'''
PURPOSE: print path not found error if it doesn't exist
PARAMETERS: path object - path to a directory or file
            string      - directory or file
RETURNS: path object to the subdirectory
'''
def pathExists(problem:Path, item:str) -> Path:
    path = problem / item
    if not path.exists():
        print(f"\033[91m\033[4mPATH ERROR\033[0m: The {item} does not exist\033[0m")
        sys.exit(1)
        
    return path


'''
PURPOSE: runs the passed in script on the test case and returns the output/error
PARAMETERS: path object - path to the script being run
            path object - path to the test case
RETURNS: output, error
'''
def runProgram(script:Path, test_case:Path) -> tuple[bytes, bytes]:
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
        output, error = runProgram(script, test)
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

    tests    = pathExists(problem, TEST_DIR)
    solution = pathExists(problem, SOLUTION)
    user_gen = pathExists(problem, problem.name + ".py")
    test_cases = sorted([test for test in tests.iterdir()], key=lambda test: int(test.name.lstrip('test').rstrip('.in')))
    
    print(f"\n\033[1m-------------------------- {problem.name} ---------------------------\033[0m")
    # for each test case compare the outputs of solution.py and user_generated
    for test in test_cases:
        gt_out, _ = runProgram(solution, test)
        us_out, e = runProgram(user_gen, test)
        
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
PARAMETERS: Path   - path to the problem directory
            string - "solution" or "user"
            string - "all" or number
RETURNS: None
'''
def runTest(problem:Path, program:str, test_num:str) -> None:
    print(f"\n\033[1m-------------------------- {problem.name} ---------------------------\033[0m")
    tests = pathExists(problem, TEST_DIR)
    test_cases = []
        
    # batch tests
    if test_num == "all":
        test_cases = sorted([test for test in tests.iterdir()], key=lambda test: int(test.name.lstrip('test').rstrip('.in')))

    # check test case exists
    elif test_num.isdigit():
        pattern = '*' + test_num + '.in'
        for file in tests.glob(pattern):
            test_cases.append(file)
        
        if len(test_cases) == 0:
            print(f"\033[91m\033[4mINVALID TEST INPUT\033[0m: Test #{test_num} does not exist in {problem.name}\033[0m")
            sys.exit(1)
    else:
        print("\033[91m\033[4mINVALID COMMAND\033[0m: INDEX 3 should be 'all' or a test number\033[0m")
        sys.exit(1)

    # run solution or user generated program
    script = ""
    if program == "solution":
        script = pathExists(problem, SOLUTION)    
    elif program == "user":
        script = pathExists(problem, problem.name + ".py")
    else:
        print("\033[91m\033[4mINVALID COMMAND\033[0m: INDEX 2 should be 'solution' or 'user'\033[0m")
        sys.exit(1)
    
    printOutput(script, test_cases)


'''
PURPOSE: run all test cases or a specific subdirectory
PARAMETERS: string - 'all' or 'name' of a subdirectory to run
RETURNS: None
'''
def main(args:str) -> None:
    if args[0] == "all":
        for subdir in CURR_DIR.iterdir():
            if subdir.is_dir() and (subdir != CURR_DIR / ".git"):
                compareOutput(subdir)
            print()
    
    else:
        problem = CURR_DIR / args[0]
        if problem.exists() and problem.is_dir():
            if ARGC > 2:
                runTest(problem, args[1], args[2])
            else:
                compareOutput(problem)
        else:
            print("\033[91m\033[4mINVALID COMMAND\033[0m: INDEX 1 should be an existing directory\033[0m")
            sys.exit(1)

    # final check
    if FAILED:
        print(f"\033[91mSome tests failed. Check above\033[0m")
    else:
        print(f"\033[92mALL TESTS PASSED!")


if __name__ == '__main__':
    if ARGC != 2 and ARGC != 4:
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