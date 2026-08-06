"""
[0][0] is top left corner
[8][8] is bottom right

- happy path is return true, return false elsewhere if this never happens
- just need to return false if this condition ever gets broken
=> board does not need to full or solvable, it just can't break the given constraints

- checking for duplicates: use a set
- use a list to store a set where each index represents a row/column/or a subbox
- or could also use a dict where key is the row, col, or for a subbox you need an equation to conver the rows + columns to a subbox. since its a 9x9 and there are 9 subboxes so 3x3 subboxes, just divide by 3
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {key: set() for key in range(9)} 
        cols = {key: set() for key in range(9)}
        subboxes = {(x,y): set() for x in range(3) for y in range(3)}
        # iterate through each point in the board
        for r in range(9):
            for c in range(9):
                point = board[r][c]
                x = r // 3
                y = c // 3
                if point != ".":
                    if point in rows[r] or point in cols[c] or point in subboxes[(x, y)]:
                        return False
                    else:
                        rows.setdefault(r, set()).add(point)
                        cols.setdefault(c, set()).add(point)
                        subboxes.setdefault((x,y), set()).add(point)


        return True