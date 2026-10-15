class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # output the length of the longest in order sequence that can be made from array
        # for each number check if previous is less than next, if it is increment count
        # need to keep track of what the find num in the sequence will be
        
        numSet = set(nums) # since dupes arent relevant
        longest = 0
        # check if num has a left neighbor to determine first num in seq

        for n in nums:
            if(n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        
            
