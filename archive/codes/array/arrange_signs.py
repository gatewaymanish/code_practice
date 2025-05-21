


def arrange_signs(arr):

    left = []
    right = []

    for i in arr:
        if i < 0:
            left.append(i)
        else:
            right.append(i)

    left.extend(right)
    return left


arr = [1, 2, 3, -4, -1, 4]
print(arrange_signs(arr))








