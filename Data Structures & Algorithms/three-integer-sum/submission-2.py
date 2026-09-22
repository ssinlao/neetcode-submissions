class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # important! sort numbers
        nums.sort()

        # make result array
        result = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # checks if number has already been put in a triplet
                continue

            # now use two sum 2 approach
            left = i + 1
            right = len(nums) - 1

            while left < right:
                target = a + nums[left] + nums[right]
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right: # skips dupes again
                        left += 1

        return result