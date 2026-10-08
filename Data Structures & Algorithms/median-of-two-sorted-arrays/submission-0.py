class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two array inputs
        total = len(nums1) + len(nums2)
        half = total // 2
        # run binary search on smaller of two arrays

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2 # get the middle of our partition
            j = half - i - 2 # index of the mid point

            nums1_l = nums1[i] if i >= 0 else float("-infinity")
            nums1_r = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            nums2_l = nums2[j] if j >= 0 else float("-infinity")
            nums2_r = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if nums1_l <= nums2_r and nums2_l <= nums1_r: # we found median
                # odd
                if total % 2:
                    return min(nums1_r, nums2_r)
                # even
                return((max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2)
            elif nums1_l > nums2_r:
                r = i - 1 # reduce size of left partition
            else:
                l = i + 1 # increase size of left partition