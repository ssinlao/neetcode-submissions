class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # get difference
        # diff = target - nums[i]
        # since we have the first num, we can check if the second num is in there
        
        # 3 4 5 6 

        check = {}

        for i in range(len(nums)):
            check[nums[i]] = i
        print(check)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in check and check[diff] != i:
                return [i, check[diff]]

        return []
            