# aaabbbcde
# aaabbbbdddee
# first
# non
# repeating
# c


def func(s):

    count = 0
    last = s[0]
    result = None

    for i in range(len(s)):
        if s[i] == last:
            count += 1
            continue
        elif s[i] != last and count == 1:
            result = last
            break
        elif s[i] != last:
            last = s[i]
            count = 1


    return result



s = 'aaabbbcde'
# s = 'aaabbbbdddee'
print(func(s))

