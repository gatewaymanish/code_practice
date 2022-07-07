

def bubble_sort(arr):
    print(f'Before sorting: {arr}')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(f'After sorting: {arr}')


arr = [4, 3, -5, 8, 33, 0, 21]
bubble_sort(arr)