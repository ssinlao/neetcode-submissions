class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # input is the list of numbers and how many freq elements to return
        # output is the k amount of freq elements

        # keep track of number and how many times it appears
        # hashmap {element : appearances}

        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, counter in count.items():
            freq[counter].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result