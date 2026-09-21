class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # function that takes
        # input: nums []
        # returns [i, j, k] where they equal 0 summed up
        # 1. sort input array
        # 2. like 2sum, but using pointers for j and k
        # 3. iterate through array with i

        result = []
        nums.sort() # sort the nums like 2sum
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            count[nums[i]] -= 1

            if i and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    result.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return result
