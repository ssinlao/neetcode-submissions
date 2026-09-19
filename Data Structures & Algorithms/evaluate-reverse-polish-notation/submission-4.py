class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack to keep track of top two operands
        # vars left and right can be used to track the operands when executing operation\
        # for each op, pop the top two and then append result as new operand

        st = [] # number stack

        for i in tokens:
            if i == '+':
                st.append(st.pop() + st.pop())
            elif i == '-':
                a, b = st.pop(), st.pop()
                st.append(b - a)
            elif i == '*':
                st.append(st.pop() * st.pop())
            elif i == "/":
                a, b = st.pop(), st.pop()
                st.append(int(float(b) / a))
            else:
                st.append(int(i))
        return st[0]

