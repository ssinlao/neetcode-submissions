class Solution:
    def isPalindrome(self, s: str) -> bool:
        # get rid of punctuation and spaces and make everything lowercase
        # need to use ascii values
        # use pointers to compare information

        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True