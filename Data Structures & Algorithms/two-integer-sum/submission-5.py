class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two inputs, list of nums and target int
        # output returns indices where two nums added in the list = target

        # thought process:
        # need to track:
        # - addend1
        # - addend2
        # - sum == target
        # - indices where sum == target

        # not binary tree search bc nums are not guaranteed to be in order
        # linear search (brute force)
        # dictonary (hash table)

        value_table = {}

        for index, num in enumerate(nums):
            value_table[num] = index

        for index, num in enumerate(nums):
            complement = target - num

            if complement in value_table and value_table[complement] != index:
                return [index, value_table[complement]]

        return []