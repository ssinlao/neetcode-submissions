class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair of values [temp, index]

        for i, t in enumerate(temperatures): # i is the index and t is the temperature
            while stack and t > stack[-1][0]: # top of stack is stack[-1] and the temp is first value [0] in pair
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd # calculate the difference of indices to get result
            stack.append((t, i))
        return result