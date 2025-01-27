
# Write a function in Python that accepts a credit card number. It should return a string where all the characters
# are hidden with an asterisk except the last four. For example, if the function gets sent “4444444444444444”,
# then it should return “***********4444”.


# num = input()   # string

# result = ''
# for i in range(len(num)):
#     if len(num) - i > 4:
#         result.join('*')
#     else:
#         result.join(num[i])

# print(result)


# 2nd approach

# result2 = num[0:-4] + '****'
# size = len(num)
# result2 = ('*' * (size-4)) + num[size-4:]
#
# print(result2)


# Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function,
# only a, e, i, o, and u will be counted as vowels — not y.


word = list(input())

vowel = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(len(word)):
    # print(word[i])
    if word[i] in vowel:
        count += 1

print(count)
