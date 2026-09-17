class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # function that multiplies all of the elements except for the current index
        # that the for loop is on

        # result [] each product appended
        # understand how to build cumulative products from left-to-right and right-to-left

        # compute prefix and postfix of i O(n)
        # 1 2 3 4
        # prefix 1 2 6 24
        # postfix (reverse order) 24 24 12 4
        # prefix x postfix
        # 24, 12, 8, 6

        result = [1] * len(nums) # initial value of 1

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # reverse order
            result[i] *= postfix
            postfix *= nums[i]
        return result
