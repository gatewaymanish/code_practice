

def singleNonDuplicate(nums):

        # occr = {}

        # for i in range(len(nums)):


        #     if nums[i] in occr:
        #         occr[nums[i]] = 2
        #     else:
        #         occr[nums[i]] = 1

        # for k, v in occr.items():
        #     if v == 1:
        #         return k

        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        #
        # i = 0
        # while i < n:
        #     if i == n - 1:  # end case
        #         return nums[i]
        #
        #     elif nums[i] == nums[i+1]:
        #         if i+2 <= n-1:
        #             i += 2          # jump to next comparison
        #             continue
        #     else:
        #         return nums[i]


        ## O(log n) solution
        arr = nums
        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            # If repeating element is at even position,
            # then single element must be on the right side
            if arr[mid] == arr[mid + 1]:
                lo = mid + 2

            # Else single element must be on the left
            else:
                hi = mid

        return arr[lo]



nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))