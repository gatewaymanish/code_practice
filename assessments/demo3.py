# reverse list

def func1(arr):

    result = []
    n = len(arr)

    while n:
        result.append(arr[n-1])
        n -= 1

    return result


arr = [4, 2, 8, 1, 0, 7]
# print(func1(arr))


def func2(arr):

    n = len(arr) # 6
    x = n-1 # 5

    for i in range(n): # 0, 1, 2, 3,4, 5
        tmp = arr[x-i]
        arr.append(tmp)

        arr.pop(x-i)

    return arr

print(func2(arr))

