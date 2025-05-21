# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.
# Note: If the second largest element does not exist, return -1.

def second_largest(arr):
    arr.sort()
    n = len(arr)

    for i in range(n-2, -1, -1):
        if arr[i] != arr[n-1]:
            return arr[i]
    return -1


arr = [3, 4, 1, 66, -6, 0, 88]
print(second_largest(arr))

# second method using 2 traversals

def second_largest2(arr):
    largest = -1
    second_largest = -1
    n = len(arr)

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):
        if arr[i] != largest and arr[i] > second_largest:
            second_largest = arr[i]

    return second_largest

arr2 = [4, 3, 6, 77, 44, 33]
print(second_largest2(arr2))


# 3rd method using 1 pass search

def second_largest3(arr):
    largest = -1
    second_largest = -1
    n = len(arr)

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]

    return second_largest

arr3 = [4, 3, 55, 11, 0, 55, 77]
print(second_largest3(arr3))