"""
requirements:  
- want to find target value in a 2d list i.e matrix
- not where it exists, but whether it exists so return true if it exists, false otherwise

constraints:
- solution that runs in O(log(m * n) time) means eliminate half of the total search space each iteration we try to find it
- each row is sorted in ascending order
- first element in every row (and thus every element on the row) is greater than last integer of previous row or every integer of previous row.
- index values will always be positive so it won't affecting our rounding


edge cases:
- target element doesn't exist in any of the rows or matrix (greater than last element in a row, but smaller than first element in a row)
- element exists as either a first element or last element in a row. 

possible solution ideas:
- given constraints, we want to preform a binary search. 
- while the value set is a 2d matrix, we can technically preform a binary search on this by treating it as a 1d list. 
=> number of values is len(matrix) * len(matrix[0]), calc the midpoint, compare target to midpoint value, and then adjust range accordingly
=> need a 1d to 2d equation to convert indexing ex. given a int, use number to find row index and col index
=> row: int / len of each row (i.e number of columns),      col: int % len of each row -> leftover amount is the col in the actual row

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r: 
            midpoint = l + (r - l) // 2
            print(midpoint)
            # convert midpoint index to 2d index
            row = int(midpoint / len(matrix[0]))
            print(row)
            col = midpoint % len(matrix[0])
            print(col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = midpoint - 1
            elif matrix[row][col] < target: 
                l = midpoint + 1

        return False
        