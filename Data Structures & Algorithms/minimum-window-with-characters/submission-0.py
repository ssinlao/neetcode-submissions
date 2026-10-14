class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # sliding window problem
        # as long as s has a matching hashmap with t its valid

        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1 # count the letters in t

        have, need = 0, len(countT) # length of countT gives us unique num of chars in t that we need
        result, resultLen = [-1, -1], float("infinity") # return left and right pointer indices
        l = 0
        for r in range(len(s)): # right boundary of our window
            c = s[r]
            window[c] = 1 + window.get(c, 0) # making our window table now

            # does count satisfy what we were looking for
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result when condition met
                if (r - l + 1) < resultLen:
                    result = [l, r]
                    resultLen = (r - l + 1) # size of our window
                # pop from the left to get smallest window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # if we removed char & made too small
                    have -= 1
                l += 1

        l, r = result
        return s[l:r+1] if resultLen != float("infinity") else ""