class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search means to continously check the middle of segments
        # can be done iteratively or recursively

        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # look in right half
            else:
                right = mid - 1 # look in left half
        return -1