class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for num in nums:
            check.add(num)

        if len(check) == len(nums):
            return False
        
        return True