class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        subboxes = {(x, y): set() for x in range(3) for y in range(3)}

        # iterate through sudoku board
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                x = r // 3
                y = c // 3
                if value != '.':
                    #is it already in its row, col, or subbox
                    if value in rows[r] or value in cols[c] or value in subboxes[x, y]:
                        return False
                    else:
                        rows[r].add(value)
                        cols[c].add(value)
                        subboxes[x,y].add(value)



        return True