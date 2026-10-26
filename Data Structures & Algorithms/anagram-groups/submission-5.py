class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use O(26) storage technique

        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # our pattern matching code
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())