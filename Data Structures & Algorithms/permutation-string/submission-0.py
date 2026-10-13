class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check if s2 letters are included in s1 (order does not matter)
        # sliding window problem
        # use length of s2 to get window size
        # use a hashmap to get frequency of each letter in substring (like group anagrams)

        if len(s1) > len(s2):
            return False
        
        # initialize both hashmaps that matches will be incremented for
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        # get out initial matches
        matches = 0
        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        return matches == 26

        