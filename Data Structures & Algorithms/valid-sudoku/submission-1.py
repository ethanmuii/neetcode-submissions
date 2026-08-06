"""
board[0][0] = top left
board[8][8]] = bottom right

there's basically 3 conditions that could disprove a valid soduko board
first try O(n^2) where you scan each element once, and you should be collect information to know whether something breaks one of those three conditions
it would be hard to prove a soduko board is valid without scanning every element, meaning your predicting or calculating based on some information

hashmap for rows: key = row index, value = set() // doesn't need to be [] since don't need to know values just need to know if value is already inset which disprove it
hashmap for columns: key = column index, value = set()

for converting a 2d point into 3x3 subbox. -> could convert 2d point into number like boxes 1 - 9 or could convert it into boxes rows 0-2, and cols 0-2

if you do boxes 0-8, how do you calculate the rows + columns
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {key: set() for key in range(9)}
        columns = {key: set() for key in range(9)}
        subboxes = {(x, y): set() for x in range(3) for y in range(3)}
        for r in range(9):
            for c in range(9):
                point = board[r][c]
                if point != ".":
                    # add it to its rows if its not in row already
                    if point in rows[r]:
                        return False
                    rows.setdefault(r, set()).add(point)
                    # add it to its column if its not in col already
                    if point in columns[c]:
                        return False
                    columns.setdefault(c, set()).add(point)
                    subbox_r = r // 3
                    subbox_c = c // 3
                    if point in subboxes[(subbox_r, subbox_c)]:
                        return False
                    subboxes.setdefault((subbox_r, subbox_c), set()).add(point)

        return True