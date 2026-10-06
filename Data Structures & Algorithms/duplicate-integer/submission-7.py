class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set for unique vals

        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False