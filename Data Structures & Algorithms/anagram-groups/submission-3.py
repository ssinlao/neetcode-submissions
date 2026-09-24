class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array for each word will be [0] * 26 with letters being incremented
        # use ascii value to set count dictionary
        result = defaultdict(list) # make our list of sublists { countVal : words[] }

        for s in strs:
            count = [0] * 26 # array for each word
            for c in s:
                count[ord(c) - ord("a")] += 1 # increment freqs of letter per word
            result[tuple(count)].append(s) # cast tuple to count for python syntax
        
        return list(result.values())
