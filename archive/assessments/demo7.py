
arr = [3, 4, 2, 7, 11, 0, 23, 4, 11, 4]


output = [3, 4, 2, 7, 11, 0, 23]


res = []

n = len(arr)

for i in range(n):

    if arr[i] in res:
        continue
    else:
        res.append(arr[i])

print(res)
