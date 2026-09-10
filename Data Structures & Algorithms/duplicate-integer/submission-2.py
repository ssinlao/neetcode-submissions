class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()

        for value in nums:
            if value in checkSet:
                return True
            checkSet.add(value)
        
        return False


