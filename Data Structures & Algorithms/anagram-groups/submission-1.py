class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # practice speed round

        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # code maker that words will be matched to
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(s)
        return list(result.values())