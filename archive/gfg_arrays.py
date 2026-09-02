
## 1. Print the alternative numbers
# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 10 30 50
arr = [10, 20, 30, 40, 50]
res = []
for i in range(0, len(arr), 2):
    res.append(arr[i])
print('Alternative numbers are: ',res)


## Find the leaders in an array # time complexity O(n^2)
# leaders are the elements which has all smaller elements to the right
arr = [16, 17, 4, 3, 5, 2]  # 17, 5, 2 are leaders
leaders = []
n = len(arr)
for x in range(n):
    is_leader = True
    for y in range(x+1, n):
        if arr[x] < arr[y]:
            is_leader = False
            break
    if is_leader:
        leaders.append(arr[x])
print('Leaders in array are: ', leaders)

# 2nd method, time complexity O(n)
arr = [16, 17, 4, 3, 5, 2]  # 17, 5, 2 are leaders
leaders = []
n = len(arr)
max_right = arr[-1]
leaders.append(max_right)
for x in range(n-1, -1, -1):    # reverse loop
    if arr[x] > max_right:
        max_right = arr[x]
        leaders.append(max_right)
leaders.reverse()
print('Leaders in array are: ', leaders)


## Generate all subarrays O(n^2)
arr = [1, 2, 3]
n = len(arr)
subarr = []
for x in range(n):
    for y in range(x+1, n+1):   # n+1 because slicer takes range less than right limiter
        subarr.append(arr[x:y])
print('All possible subarray are: ', subarr)


## Maximum sum of k elements
arr = [5, 2, -1, 0, 3, 4, 2]
k = 3
max_sum = 0
n = len(arr)
for i in range(n):
    if i+k <= n:
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
print('Max sum of k elements is: ', max_sum)


## Rearrange array to make arr[i] = i
# Input: arr[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# Output: [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
# Explanation: In range 0 to 9, all except 0, 5, 7 and 8 are present. Hence, we print -1 instead of them.
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
result = []
n = len(arr)
for i in range(n):
    if n >= i >= 0 and i in arr:
        result.append(i)
    else:
        result.append(-1)
print('Result for arr[i] = i is: ', result)


## max sum circular array O(n^2)
# input: arr[] = [8, -8, 9, -9, 10, -11, 12]
# Output: 22
# Explanation: The circular subarray [12, 8, -8, 9, -9, 10] gives the maximum sum, which is 22.
arr = [8, -8, 9, -9, 10, -11, 12]
n = len(arr)
max_sum = 0
for i in range(n):
    curr_sum = 0
    for j in range(n):
        index = (i+j)%n
        curr_sum += arr[index]
        max_sum = max(curr_sum, max_sum)
print('Max sum of circular array: ', max_sum)

# 2nd method with complexity O(n) using maxsum and minsum method
total_sum = 0
# Variables for Max Subarray (Standard Kadane)
curr_max = 0
max_sum = arr[0]
# Variables for Min Subarray (Inverted Kadane)
curr_min = 0
min_sum = arr[0]
for item in arr:
    total_sum += item
    # 1. Standard Kadane to find maximum normal subarray
    curr_max = max(item, curr_max + item)
    max_sum = max(max_sum, curr_max)
    # 2. Inverted Kadane to find minimum normal subarray
    curr_min = min(item, curr_min + item)
    min_sum = min(min_sum, curr_min)
# Edge Case: If all numbers are negative, total_sum == min_sum.
# In that case, total_sum - min_sum would equal 0, which is incorrect
# because an empty subarray isn't allowed. We must return the max_sum (the least negative number).
if max_sum < 0:
    result = max_sum
# Return the maximum of the non-wrapped and wrapped scenarios
result = max(max_sum, total_sum - min_sum)
print('Max sum kadence algo: ', result)