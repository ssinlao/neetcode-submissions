class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the k most freq elements
        # bucket sort

        count = {} # map { num : amount }
        freq = [[] for i in range(len(nums) + 1)] # our buckets

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items(): # iterating through count map
            freq[cnt].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1): # most freq at end
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result