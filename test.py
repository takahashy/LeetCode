'''
py runtests.py 
runTest(problem: directory, program: "solution" or "user", test_case: number or "all"):
'''
import sys
from pathlib import Path
from subprocess import Popen, PIPE

CURR_DIR = Path(__file__).parent
PYTHON3  = "python3"
SOLUTION = "solution.py"
TESTS  = "tests"
ARGC   = len(sys.argv)
FAILED = False

def pathExists(problem: Path, subdir: str):
    path = problem / subdir
    if not path.exists():
        print(f"{path} does not exist")
        sys.exit(1)
    return path

def compareOutput(problem: Path):
    global FAILED

    solution = pathExists(problem, SOLUTION)
    user     = pathExists(problem, problem.name + ".py")
    tests    = pathExists(problem, TESTS)

    test_cases = sorted([test for test in tests.iterdir()], key=lambda test: int(test.name.lstrip('test').rstrip('.in')))

    print(f"\n----------{problem.name}----------")
    for test in test_cases:
        gt_output, _        = runProgram(solution, test)
        us_output, us_error = runProgram(user, test)

        if us_error:
            print(f"ERROR: Expected no error but got the following: {us_error}")
            FAILED = True
        elif gt_output != us_output:
            print(f"Expected\n{gt_output}\nBut got:\n{us_output}")
            FAILED = True
        else:
            print(f"{test.name} PASSED. Same Output")
            

'''
program: "solution" or "user"
test_case: number or "all"

if tests_case is all then append all the tests in the tests subdirectory
else find the tests case number 

run the program and get the output
'''
def runTest(problem: Path, program: str, test_num: str):
    global FAILED
    tests = pathExists(problem, TESTS)
    test_cases = []
    
    if test_num == "all":
        test_cases = sorted([test for test in tests.iterdir()], key=lambda test: int(test.name.lstrip('test').rstrip('.in')))
    elif test_num.isdigit():
        pattern = "*" + test_num + ".in"
        for test in tests.glob(pattern):
            test_cases.append(test)

        if len(test_cases) == 0:
            print(f"test #{test_num} does not exist")
    else:
        print("error: should be all or a number")
        sys.exit(1)

    script = ""
    if program == "solution":
        script = pathExists(problem, SOLUTION)
    elif program == "user":
        script = pathExists(problem, problem.name + ".py")
    else:
        print("invalid command, should be solution or user")
        sys.exit(1)
    
    for test in test_cases:
        output, error = runProgram(script, test)
        if error:
            print(f"{test.name} failed. expected no errors but got {error}")
            FAILED = True
        else:
            print(f"{test.name} success!\n{output}")

    


def runProgram(program: str, filename: str):
    with Popen([PYTHON3, program, filename], stdout=PIPE, stderr=PIPE) as process:
        output, error = [out.decode("utf-8") for out in process.communicate()]
    return output, error

def main(args):
    if args[0] == "all":
        for subdir in CURR_DIR.iterdir():
            if subdir.is_dir() and (subdir != CURR_DIR / ".git"):
                compareOutput(subdir)
    
    else:
        problem = CURR_DIR / args[0]
        if problem.exists():
            runTest(problem, args[1], args[2])

    if FAILED:
        print("FAILED: some of the tests FAILED")
    else:
        print("SUCESS: All tests PASSED")


if __name__ == "__main__":
    if ARGC != 2 and ARGC != 4:
        print("Usage: python3 test.py all|directory_name [solution|user] [all|number]")
        sys.exit(1)

    main(sys.argv[1:])