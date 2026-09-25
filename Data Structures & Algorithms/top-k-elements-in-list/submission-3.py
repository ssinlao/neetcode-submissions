class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count {} -> { number : occurences }
        count = {}
        # array for result
        result = []
        # array of frequencies
        freq = [[] for i in range(len(nums) + 1)] # length is set to length of array bc thats the most occurences a num can have

        # first make count hashmap
        for num in nums:
            count[num] = count.get(num, 0) + 1 # set num val to 0 and add 1

        for n, c in count.items():
            freq[c].append(n)
     
        for i in range(len(freq) - 1, 0, -1): # go backwards bc the most freq will be at end
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result