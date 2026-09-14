class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # two strings are anagrams if we sort their chars and they are equal
        # take each string and sort them (high time complexity)
        # each char is from a - z no uppercase 
        # counting chars is O(m*n)
        # use hashmap, key is going to be num of each letter, value will be the list of strings that match this key

        result = defaultdict(list) # mapping charCount to list of Anagrams, preventing KeyError with regular dict

        for word in strs:
            count = [0] * 26

            for character in word:
                count[ord(character) - ord("a")] += 1 #ascii value subtraction to count each char

            result[tuple(count)].append(word) # group all anagrams with this count together

            # lists cannot be keys so tuple is used

        return list(result.values()) # cast back to list


