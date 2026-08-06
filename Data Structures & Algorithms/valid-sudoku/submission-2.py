"""
hashmap for rows so we can check possible duplicates in O(1)
hashmap for cols so we can check possible cols in O(1)
hashmap for 9 subboxes (3x3) for possible duplicates

and we can append to each of these boxes as we iterate through the all values in board
- only do actions and check if its not equal to '.'
- return false as soon as you run into a condition where there is a duplicate
- every time you see a value append to its respective hashmaps 

space complexity is 3 * O(n) which is total number of rows which rounds to O(n)

time complexity is O(n^2) because you might have to iterate over every value on board if there is no duplicates earlier
=> so O(n^2)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {key: set() for key in range(9)}
        cols = {key: set() for key in range(9)}
        subboxes = {(x,y): set() for x in range(3) for y in range(3)}

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                x = r // 3
                y = c // 3
                if value != ".":
                    if value in rows[r] or value in cols[c] or value in subboxes[(x,y)]:
                        return False
                    rows[r].add(value)
                    cols[c].add(value)
                    subboxes[(x,y)].add(value)






        return True