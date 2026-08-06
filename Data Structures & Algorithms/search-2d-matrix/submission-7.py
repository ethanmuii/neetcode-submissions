"""
- the matrix's setup can be viewed the same if you were to flatten the matrix into a 1d list
- adding row by row to a list also keeps the elements in sorted ascending order
=> this is because "first integer of every row is greater than the last integer of previous row"


- using this insight, we can preform binary search on the flattened list and just convert between 2d and 1d indices

** REMEMBER ITS 0-INDEXED
2d indice can be converted into 1d index by doing:
# of rows * len(rows) + col

1d index can be converted into 2d index by doing:
rows: 1d index // len(rows) -> divsion finds the number of rows since it finds which row's range it basically falls into
cols: 1d index % len(rows) -> modulo works because it finds the remainder you have after trying to fit as many rows into the number, and what's leftover that isn't enough to be a part of a new row is a column
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        print(m, n)
        l = 0
        r = (m * n) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # convert 1d index to 2d index, need to keep everything 0=indexed
            row = mid // n
            col = mid % n
            print(row, col, mid)
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False