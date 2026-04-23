# Python Program for Maximum Subarray Sum using Kadane's Algorithm

def maxSubarraySum(arr):
    # Initialize with the first element
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        # Either extend the previous subarray or start a new one
        maxEnding = max(arr[i], maxEnding + arr[i])
        # Update result if current max is greater
        res = max(res, maxEnding)

    return res

# Sample input
arr = [2, 3, -8, 7, -1, 2, 3]
print("Maximum subarray sum is:", maxSubarraySum(arr))