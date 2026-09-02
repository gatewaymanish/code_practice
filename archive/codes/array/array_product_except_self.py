# Input: arr[] = [10, 3, 5, 6, 2]
# Output: [180, 600, 360, 300, 900]



arr= [10, 3, 5, 6, 2]

result = []

for i in range(len(arr)):
    tmp = 1
    for j in range(len(arr)):

        if i != j:
            tmp *= arr[j]
    result.append(tmp)

print(result)

#second method
result = []
full_prod = 1
for i in range(len(arr)):
    full_prod *= arr[i]

for i in arr:
    tmp = full_prod // i
    result.append(tmp)

print(result)






