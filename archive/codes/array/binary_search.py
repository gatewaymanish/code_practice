# binary search in a sorted array with complexity O(log n)

def search(arr, key):
    left = 0    # index to left
    right = len(arr) - 1    # index to right

    while left <= right:
        mid = left + (right - left) // 2    # index at middle of array

        if arr[mid] == key:
            print(f'found element {key} at index', mid)
            return key

        elif arr[mid] < key:    # if element at mid index is smaller than key
            left = mid + 1       # update left index

        else:                   # if element at mid index is bigger than key
           right = mid - 1                     # update the right index

    print(f'key {key} not found')
    return -1 # if key not found


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 24
search(arr, key)




