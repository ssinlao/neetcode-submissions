class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use dictionary to save letters and freq
        # { letter : times it appeared }

        map_s = {}
        map_t = {}

        # need two for loops to get maps for each string

        for c in s:
            map_s[c] = map_s.get(c, 0) + 1
        
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1

        return map_s == map_t