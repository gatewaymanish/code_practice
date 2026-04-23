

def two_sum(nums, target):
    """
    Finds two numbers in a list that add up to the target value.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list containing the indices of the two numbers,
        or None if no such pair exists.
    """
    seen = {} # Dictionary to store numbers and their indices

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return None # No solution found


arr = [2, 1, 5, 3]
target = 4
result = two_sum(arr, target)
print(result)