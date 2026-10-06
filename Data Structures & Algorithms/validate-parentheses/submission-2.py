class Solution:
    def isValid(self, s: str) -> bool:
        # keep track of opening sides and closing sides
        # cannot start with closing side
        # we are always going to be removing from the end of the list (top of the stack)
        # when a parenthese closes

        # initialize stack
        stack = []

        for c in s:
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False # if stack has stuff at end, false