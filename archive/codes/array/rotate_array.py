from typing import List


def rotate( nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    for i in range( n -1, -1, -1):
        if k:
            tmp = nums.pop(n-k)
            nums.insert(n-i-1, tmp)
            k -= 1

    print(nums)





nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)