# leetcode
Simulates Leetcode website by creating a solution program, user generated program, and test cases. Automated checking of all test cases with runtests.py in root directory. Can also run unit or batch test cases for specific problem with either the solution program or the user generated one.

## How To Run
To compare the user generated program to the solution on the given test cases for specific problem run
```
$ python3 runtests.py [problem_directory_name]
```
To run all test cases for all the problems run the following
```
$ python3 runtests.py all
```

To perform a unit test run the 
following, where number is a test case number in the tests directory
```
$ python3 runtests.py [problem_directory_name] solution|user [number]
```
To perform a batch test run the following
```
$ python3 runtests.py [problem_directory_name] solution|user all
```

Check the `Makefile` for running corresponding program

## Directory Structure
```
root
    -> runtests.py
    -> problem1
        -> solution.py
        -> problem1.py
        -> tests
            -> test1.in
            -> test2.in
            .
            .
    -> problem2
        -> solution.py
        -> problem1.py
        -> tests
            -> test1.in
            -> test2.in
            .
            .
    .
    .
```