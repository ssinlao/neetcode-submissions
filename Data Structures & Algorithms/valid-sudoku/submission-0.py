class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking 3 arrays for duplicates
        # since each needs to be unique use set 
        
        # make 3 sets, hor, ver, square
        # - not sure if box can be a set
        # read board input using "." as delimiter
        # square index: (row / 3) * 3 + (col / 3) 

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # delimiter
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True