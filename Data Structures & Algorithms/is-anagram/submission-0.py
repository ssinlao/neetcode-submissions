class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # thought process:
        # need to make hash table (dictionary) for each word, freq_s and freq_t
        # if the char is already in dict, add 1 else set to 1
        # return the equivalence of the two dictionaries
        # (can also be done with Counter but manually code for learning purposes)
        
        freq_s = {}
        freq_t = {}

        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1

        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1
        
        return (freq_s == freq_t)