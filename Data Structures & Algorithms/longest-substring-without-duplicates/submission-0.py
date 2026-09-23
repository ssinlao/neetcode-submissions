class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        charSet = set()
        l = 0
        # right pointer changing dynamically

        for r in range(len(s)):
            while s[r] in charSet: # this character at right ptr is already in set (dupe), update window
                charSet.remove(s[l]) # remove left character from set
                l += 1 # update left ptr
            charSet.add(s[r]) # non dupe added
            result = max(result, r - l + 1) # comparing window size
        return result