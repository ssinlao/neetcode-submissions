class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        freq = [[] for i in range(len(nums) + 1)]

        # make map of number frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n) # for every number and count, n occurs c times

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result