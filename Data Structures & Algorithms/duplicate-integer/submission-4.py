class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # practice speed round wooo
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False