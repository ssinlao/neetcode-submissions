import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use converging pointers

        s = s.lower()
        s = re.sub(r'[^0-9a-zA-Z]', '', s) # use regex to remove nonalphanumeric chars
        print(s)

        left = 0
        right = len(s) - 1

        while left < right: # ensures right index is always more than left
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

                