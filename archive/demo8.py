import copy

## find the second-largest element in an array
arr = [3, 4, 1, 66, -6, 0, 88]
largest = arr[0]
second_largest = arr[0]
for elem in arr:
    if elem > largest:
        second_largest = largest
        largest = elem
    elif second_largest < elem != largest:
        second_largest = elem
# print(second_largest)



## remove duplicates
arr = [3, 4, 1, 66, -6, 0, 88, 3, 4, 1, 66, -6, 0, 88]
new_arr = []
for elem in arr:
    if elem not in new_arr:
        new_arr.append(elem)
# print(new_arr)

# second method to remove duplicates
for i in range(len(arr)):
    frequency = 0
    for j in range(len(new_arr)):
        if arr[i] == new_arr[j]:
            frequency += 1
    if frequency == 0:
        new_arr.append(arr[i])
# print(new_arr)


## find the sum of all the elements in an array
arr = [3, 4, 1, 66, -6, 0, 88, 3, 4, 1, 66, -6, 0, 8]
total_sum = 0
for i in arr:
    total_sum += i
# print('sum of array: ', total_sum)


## count even and odd numbers
arr = [3, 4, 1, 66, -6, 0, 88, 3, 4, 1, 66, -6, 0, 8]
even = []
odd = []
even_count = 0
odd_count = 0
for item in arr:
    if item % 2 == 0:
        even.append(item)
        even_count += 1
    else:
        odd.append(item)
        odd_count += 1
# print('Here are even numbers: ', even ,' with count ', even_count)
# print('Here are odd numbers: ', odd, ' with count ', odd_count)

## Find the maximum and minimum elements in an array
arr = [3, 4, 1, 66, -6, 0, 88, 3, 4, 1, 66, -6, 0, 8]
largest = arr[0]
smallest = arr[0]
for item in arr:
    if item > largest:
        largest = item
    elif item < smallest:
        smallest = item
# print('Largest number: ', largest, ' and Smallest number: ', smallest)

## Reverse an array
arr = [3, 4, 1, 66, -6, 0, 88, 3, 4, 1, 66, -6, 0, 8]
new_arr = []
for i in range(len(arr) - 1, -1, -1):
    new_arr.append(arr[i])
# print('Reversed array is: ', new_arr)

# second method
new_arr = []
for i in range(len(arr)):
    new_arr.append(arr[len(arr)-1-i])
# print('Reversed array is: ', new_arr)


## fibonaci series
def fib(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        first, second = 0, 1
        series = [first, second]
        for _ in range(n-2):
            next_num = first + second
            first = second
            second = next_num
            series.append(next_num)
        return series
# print('Fibonaci series of 10 numbers is: ', fib(10))


## factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        for x in range(1, n+1):
            res *= x
        return res
# print('Factorial of number 5 is: ', factorial(10))


## Find Frequency of Each Element
arr = [8, 0, -6, 66, 1, 4, 3, 88, 0, -6, 66, 1, 4, 3]
freq = {}
for x in arr:
    if x not in freq.keys():
        freq[x] = 1
    else:
        freq[x] += 1
# print('Frequency of elements in array is: ', freq)


## Find the maximum sum of k consecutive numbers
k = 3
arr = [4, -2, 9, 3, 5, 6, 4, 11, 2]
left, right, n = 0, k, len(arr)
window_sum = sum(arr[0:k]) # initial window
max_sum =  copy.deepcopy(window_sum)
while right < n-1:
    window_sum = window_sum - arr[left] + arr[right]
    max_sum = max(max_sum, window_sum)
    left += 1
    right += 1
# print(f'Max sum of k sequence {arr[left:right]} is: ', max_sum)


## Find the longest sequence where total sum < s
s = 15
arr = [4, -2, 9, 3, 5, 6, 4, 11, 2, 2, 3, 2, 1, 4, 3, 2]
left, right, n = 0, 1, len(arr)
longest = 0
longest_subarray = []
while right < n:
    subarray = arr[left:right]
    while sum(subarray) < s:
        if len(subarray) > longest:
            longest = len(subarray)
            longest_subarray = subarray
        subarray = arr[left:right]
        # print('Debug: subarray is: ', subarray, ' and sum is: ', sum(subarray))
        right += 1
    else:
        if left < right:
            left += 1
            # right = left + 1
print('Longest subarray is: ', longest_subarray)












