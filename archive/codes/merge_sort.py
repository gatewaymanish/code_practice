## pseudo code - Merge Sort
# MergeSort(arr):
#          if length(arr) <= 1:
#              return arr
#          middle = length(arr) // 2
#          left = arr[0:middle]
#          right = arr[middle:length(arr)]
#          return merge(MergeSort(left), MergeSort(right))
#
#      merge(left, right):
#          result = []
#          while left and right:
#              if left[0] < right[0]:
#                  result.append(left.pop(0))
#              else:
#                  result.append(right.pop(0))
#          while left:
#              result.append(left.pop(0))
#          while right:
#              result.append(right.pop(0))
#          return result

## Code

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[0:middle]
    right = arr[middle:len(arr)]
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


arr = [6, 9, 4, 22, 0, 11, 55, 33]

print(mergesort(arr))