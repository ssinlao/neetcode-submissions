class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = "" # output string
        # use int and # to track word lengths and where they start
        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s: str) -> List[str]:
        result = [] # output list
        i = 0 # beginning of word pointer

        while i < len(s):
            j = i # second pointer for the end of the word

            while s[j] != '#':
                j += 1
            length = int(s[i : j]) # counting the string chars

            result.append(s[j+1 : j+1+length]) # append to result
            i = j + 1 + length # move to the end of the string

        return result