### Notes
Solution is in `solution.py`.

Added `solution_checks_all_files.py` which checks against all .json's provided. (Added `20_points_with_empty.json` that will fail test on purpose)

I did not build this with speed in mind, only to calculate the correct solution. An easy speed increase could be gained by parallelizing the for loop (for large query and/or phrase lists) ([some example code here](https://stackoverflow.com/questions/20190668/multiprocessing-a-for-loop)), or using numpy.

## Instructions
- Clone the repository and use it to create a *public* repository in your GitHub account.
- The problem statement is described in the `problem_statement.pdf` file.
- Write the solution into the `fuzzy_phrases/solution.py`. Please do not change the input and output contract of the `def phrasel_search(P, Queries) -> [[string]]` function as the testing of the code correctness will be done programmatically.
- Note - You can only use standard python libraries. ex - json, random, etc