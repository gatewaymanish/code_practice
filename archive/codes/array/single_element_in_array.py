"""
PROBLEM STATEMENT:
Given a sorted array in which every element appears twice consecutively except for one element 
that appears only once, find and return that single element.

Example:
    Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
    Output: 2
    
Constraints:
    - Array is sorted
    - All elements except one appear exactly twice
    - Must solve in O(log n) time complexity
"""


def singleNonDuplicate(nums):
    """
    Find the single element in a sorted array where every other element appears twice.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        
        # Align mid to even index for pair checking
        if mid % 2 == 1:
            mid -= 1
        
        # Single element is on the right if pair is intact
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        # Single element is on the left or at mid
        else:
            hi = mid

    return nums[lo]


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(singleNonDuplicate(nums))