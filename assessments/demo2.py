# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
# Example 1:
# Java
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Copy
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.


def myfunc(arr):

    cost = arr[0]
    sell = 0
    maxprofit = 0

    for i in range(len(arr)-1):
        if cost > arr[i]:
            cost = arr[i]
        if arr[i+1] > sell:
            sell = arr[i+1]
        tmp = sell - cos
        # print(cost, sell)
        if maxprofit < tmp:
            maxprofit = tmp

    return maxprofit

arr = [10,3,5,6,7,1]
print(myfunc(arr))



