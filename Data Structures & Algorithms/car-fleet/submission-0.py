class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)] # zip is a tool to combine multiple iterables

        stack = []
        # sort array of pairs
        for p, s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s) # decimal division to get time that car reaches target

            # check if stack has two elements (to compare)
            # if the top of stack reaches target before the car ahead of it, pop top of stack
            # decreasing # of car fleets

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)