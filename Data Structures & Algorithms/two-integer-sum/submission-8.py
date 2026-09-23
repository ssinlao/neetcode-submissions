class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # practice speed round

        tracker = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in tracker:
                return [tracker[diff], i]
            tracker[n] = i
        return result