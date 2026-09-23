class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # occurences of each char
        result = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # count[char at right ptr], if char doesnt exist return 0
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1) # r - l + 1 = length of our window
        return result