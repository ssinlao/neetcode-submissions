class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix problem
        # multiply everything before and after current index

        result = [1] * len(nums) # since we are mulitplying, 1 should be in each space rather than 0 or null
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            result[i] = prefix # result = whatever is to the left
            prefix *= nums[i] # prefix is multiplied by all other numbers

        # iterate backwards for postfix
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix # mulitplying elements by the right side product each time
            postfix *= nums[i] # multiply by other nums
        return result