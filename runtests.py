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
    
    # check valid paths
    pathExists(tests, "directory")
    pathExists(solution, "file")
    pathExists(user_gen, "file")
    
    print(f"\n\033[1m-------------------------- {problem.name} ---------------------------\033[0m")
    # for each test case compare the outputs of solution.py and user_generated
    test_cases = sorted([test for test in tests.iterdir()])
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
        print(f"\n\033[92mALL TESTS PASSED!")



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"\033[91m\033[4mUsage\033[0m\033[0m: python3 runtests.py [all|dir_name]")
        sys.exit(1)
        
    main(sys.argv[1])
    
    
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Pathlib methods
    p.iterdir() - iterate through all files and subdirectories in `p` directory
    p.is_file() - check if `p` is a file
    p.is_dir()  - check if `p` is a directory
    p.suffix    - get the extension of file(.txt, .pdf, .cpp)
    p.name      - get the name of the file including extension
    p.exists()  - check whether `p` exists
    p.cwd()     - current working directory
    p.glob(ptn) - given a pattern searches in the current directory (ptn = '*.py')
    p.rglob(ptn)- given a pattern searches in current and subdirectories
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
                        out.decode('utf-8')
                 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''