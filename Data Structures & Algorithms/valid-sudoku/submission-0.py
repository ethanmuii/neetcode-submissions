"""
[0][0] = top left corner
[0][8] = top right corner
[8][0] = bottom left corner
[8][8] = bottom right corner

key assumption: board does not need to be full or solvable to be valid.

prove a soduko board is invalid is best choice.
assumption: as soon as you know if one the rules is broken, the whole board becomes invalid. 


brute force: 
- look through each row and each col and checkk if there are duplicates via column like append to an array and say if num in [], then duplicate and is false. 
- time complexity is at least O(n^2)

problem questions:
how to efficiently check those rules?
what can we do so we don't have to recheck point that we already checked? 

hash map: key for each row, key for each col



NOTES AFTER SEEING HINT:
- hash set for every row, hash set for every column 
- dictionary (hash map) to efficiently check squares?
    - key: subbox, value = list of values in that subbox
        - which key you access depends on where you are in the (r, c)
        => what is the equation to convert (r, c) to a group 
            - visualize the 9x9 grid and need an equation to convert 9x9 in 3x3 grid of subboxes

- hash map vs hash set
=> for each row, column, square: 
key = number for row/col and number for square
value = hash set to check for duplicates

trick: usually always best to keep your problem in 0-indexed for any variable case
=> since the arrays in python are already formatted that way

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # storage and initialize the maps

        row_map = {i: set() for i in range(9)}
        col_map = {i: set() for i in range(9)}
        square_map = {i: set() for i in range(9)}
        
        # need proper index bounding 
        for r in range(len(board)): # num of rows
            for c in range(len(board[0])): # num of columns
                # need to check for duplicates in each row, col, square => return False
                # skip over '.'
                # do the work if it is not duplicate
                cell = board[r][c]
                square = (r // 3) * 3 + (c // 3)
                if cell != '.' and (cell in row_map[r] or cell in col_map[c] or cell in square_map[square]): # duplicate
                    return False
                else:
                    row_map[r].add(cell)
                    col_map[c].add(cell)
                    square_map[square].add(cell)
        return True