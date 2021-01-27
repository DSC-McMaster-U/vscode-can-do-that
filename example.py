"""Checks if a given number can be expressed as the sum of two fibonnaci numbers."""

def fib(n):
    """Computes the fibonnaci sequence up to and including n."""
    if n == 0:
        return [0]

    fib_seq = [0, 1]
    for _ in range(n-1):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def two_sum(nums, target):
    """Checks if there exists a pair of numbers in nums that sums to target."""
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (nums[i] + nums[j]) == target:
                return True
    return False

def test_two_sum():
    """Run tests for two_sum function."""
    assert two_sum([1, 2], 3) == True
    assert two_sum([4, 2, 3, 1], 5) == True
    assert two_sum([4, 2, 3, 1], 100) == False
    assert two_sum([4, 2, 3, 1], 8) == False

# main code
test_two_sum()
print("tests passed")

N = 10
target = 15
fibonacci_seq = fib(N)
result = two_sum(fibonacci_seq , target)
print("target =", target)
print("nums =", fibonacci_seq)
print("result =", result)


####################
### Things To Do ###
####################
"install python extension for language features like intellisense,"
"code completition, symbols, go to definition, debugging, etc ..."

"run using the run button"
"run using integrated terminal"

"debug code"

"stage and commit edit.py using git gui"
"stage and commit navigate.js using integrated terminal"
"wrap code in __main__ using code snippet"
"demonstrate git gutter diff"
"demonstrate a complete git diff of the file"
"stage and commit fix and addition of __main__ in seperate commits"

"add command line arguments for --test, --n, and --target"
"demonstrate code snippet for parser and add_argument"

"add linting (pylint)"
"add formatting (black)"

"see settings.json under .vscode"
"see launch.json"
"see tasks.json"

"""
useful settings
- auto format on save
- auto trim trailing whitespace on save
- auto add new line to end of file
- editor ruler at 80
- for more editing space, toggle
    - status bar
    - minimap
    - breadcrumbs
    - side bar
    - activity bar
"""

"""
    "files.trimTrailingWhitespace": true,
    "editor.formatOnSave": true,
    "files.insertFinalNewline": true,
    "editor.rulers": [
        80
    ],
"""
