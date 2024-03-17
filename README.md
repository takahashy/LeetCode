# leetcode
Simulates Leetcode website by creating a solution program, user generated program, and test cases. Automated checking of all test cases with runtests.py in root directory. To compare the user generated program to the solution on the given test cases for specific problem run
```
$ python3 runtests.py [problem_directory_name]
        OR
$ make [problem_directory_name]
```
To run all test cases for all the problems run the following
```
$ python3 runtests.py all
        OR
$ make all
```

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