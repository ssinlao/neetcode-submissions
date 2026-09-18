class Solution:
    def isValid(self, s: str) -> bool:
        # function that checks parentheses validity
        # use stack, push: append(), pop: pop(), peek: stack[-1]
        # use hashmap to make valid pair 

        validPairs = { ")" : "(", "]" : "[", "}" : "{" }

        st = []

        for c in s:
            if c in validPairs:
                if st and st[-1] == validPairs[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False

            