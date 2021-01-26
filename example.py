"""Computes if a given number can be expressed as the sum of two fibonnaci numbers."""

def fib(n):
    """Computes the first n numbers of the fibonnaci sequence.

    Args
    ----
    n : int
        How many fibonnaci numbers to compute (including n)

    Returns
    -------
    list[int]
        The first n numbers of the fibonnaci sequence
    """
    if n == 0:
        return [0]

    fib_seq = [0, 1]
    for _ in range(n-1):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def two_sum(nums, target):
    """Checks if there exists a pair of numbers in nums that sum to target.

    Args
    ----
    nums : list[int]
        List of numbers
    target : int
        Target sum

    Returns
    -------
    bool
        Returns True if two different elements in nums sums to target,
        else returns False
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (nums[i] + nums[j]) == target:
                return True
    return False

def test_two_sum():
    assert two_sum([1, 2], 3) == True
    assert two_sum([4, 2, 3, 1], 5) == True
    assert two_sum([4, 2, 3, 1], 100) == False
    assert two_sum([4, 2, 3, 1], 8) == False

test_two_sum()
print("tests passed")

N = 10
target = 15
fibonacci_seq = fib(N)
result = two_sum(fibonacci_seq , target)
print("target =", target)
print("nums =", fibonacci_seq)
print("result =", result)



### todo ###
# install python extension for language
# features like intellisense, code completition, symbols, go to definition, debugging, run, etc ...

# run using the run button
# run using integrated terminal

# debug code

# commit one of the previous files using git gui
# commit another of the previous files using terminal git
# stage the above fix using the git gutter
# git diff with previous version

# wrap code in __main__ using code snippet
# add command line arguments for --test, --n, and --target
# add custom code snippet for argparse

# add linting (pylint)
# add formatting (black)

# see launch.json (more debugging configurations)
# see tasks.json (build tasks, testing tasks, code quality, etc ...)

# useful settings
# - auto format on save
# - auto trim trailing whitespace on save
# - auto add new line to end of file
# - editor ruler at 80
# - language specific settings
# - for more editing space, toggle
#     - status bar
#     - minimap
#     - breadcrumbs
#     - side bar
#     - activity bar
