class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set for check checking
        numSet = set(nums)
        longest = 0 # get max

        for n in nums:
            if (n - 1) not in numSet: # no left neighbor means it's the start of seq
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest