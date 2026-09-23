class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # input: matrix
        # output: true if target exists, false otherwise

        # entire matrix is in non-decreasing order
        # use two pointers for each sub-array
        # check the start num of each sub array and based on that, choose which one to iterate through

        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False