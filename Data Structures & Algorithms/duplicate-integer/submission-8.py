class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unique val = set

        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False