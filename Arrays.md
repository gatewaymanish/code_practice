# Arrays with Python
Learning curve of Arrays, problem solving with Python, patterns, strategies and cheat sheet for interviews.

## How to Decide Which Method to Use
`Unsorted arrays → Linear search, hashing`\
`Sorted arrays → Binary search, two-pointer`\
`Contiguous subarray problems → Sliding window, Kadane’s`\
`Frequency/missing/repeating → Hashing/Counter`\
`Rotation/shift problems → Slicing or modular arithmetic`\
`Optimization problems → Prefix sums, dynamic programming`

## Array Interview Ladder so you can practice progressively from Easy → Medium → Hard.
🟢 Easy (Foundations & Warm‑up)\
Reverse an array → Tests basic indexing and in‑place swaps.\
Find min/max element → Simple traversal, checks attention to detail.\
Second largest element → Slightly trickier, requires tracking two values.\
Move all zeros to end → Common warm‑up for in‑place rearrangement.\
Check if array is sorted → Basic condition checks.

🟡 Medium (Patterns & Optimization)\
Rotate array by k → Tests slicing or modular arithmetic.\
Two sum / pair with target → Classic two‑pointer or hashing problem.\
Maximum sum subarray of size k → Sliding window efficiency.\
Kadane’s algorithm (max subarray sum) → Dynamic programming intuition.\
Find missing number in sequence → Prefix sum, XOR, or hashing.\
Merge two sorted arrays → Tests ability to handle sorted data efficiently.

🔴 Hard (Advanced & Tricky)\
Subarray sum equals k → Prefix sum + hashmap, tests deeper thinking.\
Product of array except self → Division not allowed, prefix/suffix trick.\
Maximum product subarray → Variation of Kadane’s, requires careful handling of negatives.\
Merge overlapping intervals → Sorting + greedy approach.\
Equilibrium index → Prefix sums, balance left vs right.\
Matrix problems (rotate matrix, search in 2D) → Extends array logic to 2D.

## Strategies
1. Pattern Recognition\
Don’t memorize problems — learn the patterns (two‑pointer, sliding window, prefix sums, hashing).\
When you see a new problem, ask: Which pattern fits here?\
Example: “Find subarray with sum k” → prefix sum + hashmap.

2. Brute Force → Optimize\
Always start with a brute force solution (nested loops, 𝑂(𝑛2)).\
Then refine to optimal (𝑂(𝑛) or 𝑂(log⁡𝑛)).\
Interviewers love seeing your thought process evolve.

3. Complexity Awareness\
After solving, state time and space complexity.\
Compare brute force vs optimized — shows maturity.

4. Dry Run & Edge Cases\
Walk through examples manually.\
Test with edge cases: empty array, single element, negatives, duplicates.

---
# 🟢 Easy Array Problems (Foundations & Warm‑up)

## 1. Reverse an Array
```python
arr = [1, 2, 3, 4, 5]
arr.reverse()   # modifies in place
print(arr)      # [5, 4, 3, 2, 1]

# OR
print(arr[::-1])  # creates a new reversed list
```
- **When to use:** Asked to reverse order of elements.
- ⚠️ **Attention:**
  - `arr.reverse()` → in‑place.
  - `arr[::-1]` → returns a new list.
  - Mistake: confusing the two and unintentionally modifying the original array.

---

## 2. Find Min/Max Element
```python
arr = [10, 3, 5, 7]
print(min(arr))  # 3
print(max(arr))  # 10
```
- **When to use:** Quick check for extremes.
- ⚠️ **Attention:**
  - Python has built‑ins (`min`, `max`).
  - Mistake: writing manual loops but initializing incorrectly (e.g., starting with `0` instead of `arr[0]`).

---

## 3. Second Largest Element
```python
arr = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in arr:
    if num > first:
        second, first = first, num
    elif num > second and num != first:
        second = num
print(second)  # 45
```
- **When to use:** Asked for “runner‑up” element.
- ⚠️ **Attention:**
  - Must handle **duplicates** (e.g., `[10, 10, 9]` → answer is 9).
  - Mistake: forgetting `num != first` check, which causes wrong results.

---

## 4. Move All Zeros to End
```python
arr = [0, 1, 0, 3, 12]
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
print(arr)  # [1, 3, 12, 0, 0]
```
- **When to use:** Rearrangement problems where order matters.
- ⚠️ **Attention:**
  - Sorting is **not acceptable** (changes order).
  - Interviewers expect **stable rearrangement** (non‑zeros keep original order).

---

## 5. Check if Array is Sorted
```python
arr = [1, 2, 3, 4]
print(all(arr[i] <= arr[i+1] for i in range(len(arr)-1)))  # True
```
- **When to use:** Validate sorted input before binary search.
- ⚠️ **Attention:**
  - Mistake: only checking first and last elements.
  - Must check **every adjacent pair**.

---

# 🚨 Common Mistakes Programmers Make
- Forgetting **edge cases**: empty array, single element, duplicates.
- Confusing **in‑place vs new list** operations (`reverse()` vs slicing).
- Ignoring **stability** in rearrangements (zeros problem).
- Overcomplicating when Python has **built‑ins** (`min`, `max`, `sorted`).
- Not explaining **time complexity** — even for easy problems, interviewers expect it.

---

✅ These “easy” problems are **traps** — they look simple, but interviewers watch if you handle **duplicates, edge cases, and in‑place vs copy** correctly.

---

Here’s the **Medium Array Problems** section in clean **Markdown format** with code, explanations, and pitfalls to watch out for 👇

---

# 🟡 Medium Array Problems (Patterns & Optimization)

## 1. Rotate Array by k
```python
def rotate(arr, k):
    k %= len(arr)   # handle k > n
    return arr[-k:] + arr[:-k]

print(rotate([1,2,3,4,5], 2))  # [4,5,1,2,3]
```
- **When to use:** Problems asking to “rotate” or “shift” elements.
- ⚠️ **Attention:**
  - Forgetting `k %= len(arr)` → causes index errors when k > n.
  - In-place vs new list: clarify what’s expected.

---

## 2. Two Sum (Pair with Target)
```python
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return (seen[target - num], i)
        seen[num] = i
    return None

print(two_sum([2,7,11,15], 9))  # (0,1)
```
- **When to use:** Classic interview problem for hashing.
- ⚠️ **Attention:**
  - Mistake: using nested loops → \(O(n^2)\).
  - Hashmap reduces to \(O(n)\).
  - Handle duplicates carefully (don’t overwrite indices blindly).

---

## 3. Maximum Sum Subarray of Size k (Sliding Window)
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_sum_subarray([2,1,5,1,3,2], 3))  # 9
```
- **When to use:** Optimize contiguous subarray problems.
- ⚠️ **Attention:**
  - Mistake: recalculating sum each time → \(O(nk)\).
  - Correct approach: update window sum in \(O(1)\).

---

## 4. Kadane’s Algorithm (Max Subarray Sum)
```python
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print(kadane([-2,1,-3,4,-1,2,1,-5,4]))  # 6
```
- **When to use:** Asked for “maximum subarray sum.”
- ⚠️ **Attention:**
  - Mistake: not handling all-negative arrays (should return max element).
  - Always initialize with `arr[0]`, not `0`.

---

## 5. Find Missing Number in Sequence
```python
def missing_number(arr):
    n = len(arr) + 1
    total = n * (n+1) // 2
    return total - sum(arr)

print(missing_number([1,2,4,5]))  # 3
```
- **When to use:** Sequence problems (1 to n).
- ⚠️ **Attention:**
  - Mistake: forgetting formula for sum of first n numbers.
  - Edge case: duplicates → this method fails, use hashing instead.

---

## 6. Merge Two Sorted Arrays
```python
def merge_sorted(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:]); res.extend(b[j:])
    return res

print(merge_sorted([1,3,5], [2,4,6]))  # [1,2,3,4,5,6]
```
- **When to use:** Combining sorted arrays efficiently.
- ⚠️ **Attention:**
  - Mistake: appending leftovers incorrectly.
  - Must handle remaining elements after loop.

---

# 🚨 Common Mistakes in Medium Problems
- Forgetting **edge cases** (k > n, all negatives, duplicates).
- Using brute force when **optimized patterns exist** (sliding window, hashing).
- Not clarifying **in-place vs new list** requirements.
- Overlooking **time complexity** improvements.

---

✅ These medium problems test if you can **spot patterns** and avoid brute force. Interviewers want to see you jump from naive to optimized solutions.

---

Here’s the **Hard Array Problems** section in clean **Markdown format** with code, explanations, and pitfalls to watch out for 👇

---

# 🔴 Hard Array Problems (Advanced & Tricky)

## 1. Subarray Sum Equals k (Prefix Sum + Hashmap)
```python
def subarray_sum(nums, k):
    count, curr_sum = 0, 0
    prefix = {0: 1}
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix:
            count += prefix[curr_sum - k]
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
    return count

print(subarray_sum([1,1,1], 2))  # 2
```
- **When to use:** Asked for number of subarrays with a given sum.
- ⚠️ **Attention:**
  - Mistake: using nested loops → \(O(n^2)\).
  - Correct approach: prefix sum + hashmap → \(O(n)\).
  - Edge case: must initialize `prefix = {0:1}` to handle sums starting at index 0.

---

## 2. Product of Array Except Self
```python
def product_except_self(nums):
    n = len(nums)
    left, right, res = [1]*n, [1]*n, [1]*n
    for i in range(1, n): left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1): right[i] = right[i+1] * nums[i+1]
    for i in range(n): res[i] = left[i] * right[i]
    return res

print(product_except_self([1,2,3,4]))  # [24,12,8,6]
```
- **When to use:** Division not allowed, classic interview favorite.
- ⚠️ **Attention:**
  - Mistake: using division → fails with zeros.
  - Must use prefix/suffix arrays.

---

## 3. Maximum Product Subarray
```python
def max_product(nums):
    curr_max = curr_min = result = nums[0]
    for num in nums[1:]:
        temp = curr_max
        curr_max = max(num, num*curr_max, num*curr_min)
        curr_min = min(num, num*temp, num*curr_min)
        result = max(result, curr_max)
    return result

print(max_product([2,3,-2,4]))  # 6
```
- **When to use:** Variation of Kadane’s algorithm with negatives.
- ⚠️ **Attention:**
  - Mistake: ignoring negative numbers — they can flip min → max.
  - Must track both `curr_max` and `curr_min`.

---

## 4. Merge Overlapping Intervals
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
```
- **When to use:** Scheduling, meeting rooms, ranges.
- ⚠️ **Attention:**
  - Mistake: forgetting to sort intervals first.
  - Must merge in sorted order.

---

## 5. Equilibrium Index
```python
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total -= num
        if left_sum == total:
            return i
        left_sum += num
    return -1

print(equilibrium_index([1,3,5,2,2]))  # 2
```
- **When to use:** Asked for index where left sum = right sum.
- ⚠️ **Attention:**
  - Mistake: recalculating sums each time → \(O(n^2)\).
  - Correct approach: track running sums → \(O(n)\).

---

## 6. Matrix Problems (2D Arrays)
**Rotate Matrix 90°**
```python
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
# [[7,4,1],[8,5,2],[9,6,3]]
```
- **When to use:** Image rotation, grid problems.
- ⚠️ **Attention:**
  - Mistake: forgetting transpose step before reversing rows.
  - Must do both steps for correct rotation.

---

# 🚨 Common Mistakes in Hard Problems
- Forgetting **initialization tricks** (prefix sum map with `{0:1}`).
- Ignoring **edge cases** (zeros in product, negatives in max product).
- Not sorting before merging intervals.
- Using brute force when optimized solutions exist.
- Overlooking **time complexity** — these problems test efficiency.

---

✅ These hard problems are **classic FAANG interview questions**. They test if you can combine **patterns (prefix sums, DP, greedy)** with careful handling of **edge cases**.

---

# 📚 Array Interview Cheat Sheet (Python)

## 🟢 Easy (Foundations & Warm‑up)

### 1. Reverse an Array
```python
arr = [1, 2, 3, 4, 5]
arr.reverse()   # in-place
print(arr)      # [5,4,3,2,1]

# OR
print(arr[::-1])  # new list
```
- ⚠️ **Pitfall:** Confusing in‑place vs new list.

---

### 2. Find Min/Max Element
```python
arr = [10, 3, 5, 7]
print(min(arr))  # 3
print(max(arr))  # 10
```
- ⚠️ **Pitfall:** Wrong initialization when using manual loops.

---

### 3. Second Largest Element
```python
arr = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in arr:
    if num > first:
        second, first = first, num
    elif num > second and num != first:
        second = num
print(second)  # 45
```
- ⚠️ **Pitfall:** Not handling duplicates correctly.

---

### 4. Move All Zeros to End
```python
arr = [0,1,0,3,12]
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
print(arr)  # [1,3,12,0,0]
```
- ⚠️ **Pitfall:** Sorting instead of stable rearrangement.

---

### 5. Check if Array is Sorted
```python
arr = [1,2,3,4]
print(all(arr[i] <= arr[i+1] for i in range(len(arr)-1)))  # True
```
- ⚠️ **Pitfall:** Only checking first and last elements.

---

## 🟡 Medium (Patterns & Optimization)

### 1. Rotate Array by k
```python
def rotate(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]
```
- ⚠️ **Pitfall:** Forgetting `k %= n`.

---

### 2. Two Sum (Hashmap)
```python
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return (seen[target - num], i)
        seen[num] = i
    return None
```
- ⚠️ **Pitfall:** Using nested loops → \(O(n^2)\).

---

### 3. Max Sum Subarray of Size k
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```
- ⚠️ **Pitfall:** Recomputing sum each time.

---

### 4. Kadane’s Algorithm
```python
def kadane(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```
- ⚠️ **Pitfall:** Not handling all‑negative arrays.

---

### 5. Missing Number in Sequence
```python
def missing_number(arr):
    n = len(arr) + 1
    total = n*(n+1)//2
    return total - sum(arr)
```
- ⚠️ **Pitfall:** Fails if duplicates exist.

---

### 6. Merge Two Sorted Arrays
```python
def merge_sorted(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res
```
- ⚠️ **Pitfall:** Forgetting to append leftovers.

---

## 🔴 Hard (Advanced & Tricky)

### 1. Subarray Sum Equals k
```python
def subarray_sum(nums, k):
    count, curr_sum = 0, 0
    prefix = {0:1}
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix:
            count += prefix[curr_sum - k]
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
    return count
```
- ⚠️ **Pitfall:** Missing prefix initialization `{0:1}`.

---

### 2. Product of Array Except Self
```python
def product_except_self(nums):
    n = len(nums)
    left, right, res = [1]*n, [1]*n, [1]*n
    for i in range(1, n): left[i] = left[i-1]*nums[i-1]
    for i in range(n-2, -1, -1): right[i] = right[i+1]*nums[i+1]
    for i in range(n): res[i] = left[i]*right[i]
    return res
```
- ⚠️ **Pitfall:** Using division → fails with zeros.

---

### 3. Maximum Product Subarray
```python
def max_product(nums):
    curr_max = curr_min = result = nums[0]
    for num in nums[1:]:
        temp = curr_max
        curr_max = max(num, num*curr_max, num*curr_min)
        curr_min = min(num, num*temp, num*curr_min)
        result = max(result, curr_max)
    return result
```
- ⚠️ **Pitfall:** Ignoring negative numbers.

---

### 4. Merge Overlapping Intervals
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```
- ⚠️ **Pitfall:** Forgetting to sort first.

---

### 5. Equilibrium Index
```python
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total -= num
        if left_sum == total:
            return i
        left_sum += num
    return -1
```
- ⚠️ **Pitfall:** Recomputing sums each time → inefficient.

---

### 6. Rotate Matrix 90°
```python
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
```
- ⚠️ **Pitfall:** Forgetting transpose step before reversing rows.

---

# 🚨 General Interview Pitfalls
- Ignoring **edge cases** (empty array, single element, duplicates, negatives).
- Confusing **in‑place vs new list** operations.
- Forgetting **time complexity** explanation.
- Overcomplicating when Python has **built‑ins**.
- Not clarifying **requirements** (stable rearrangement, sorted input).

---

✅ This cheat sheet gives you **Easy → Medium → Hard** problems with code, explanations, and pitfalls. It’s your one‑stop prep guide for array interviews.

---

