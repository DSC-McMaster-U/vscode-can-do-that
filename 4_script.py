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

if __name__ == "__main__":
    test_two_sum()
