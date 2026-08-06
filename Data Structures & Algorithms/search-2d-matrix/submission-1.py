"""
matrix[0][0] = top left
matrix[len(matrix) - 1][len(matrix[0])]
rows = first index into matrix
cols = second index or the indexs into a matrix's row

key notes:
- in a row, it is increasing order = predictable condition
- first index in the next row is always bigger than last index into previous row
- if you were to make the matrix one big number line, it would be adding the rows from top to down in one big array and keeping the indexs within each row the same
    => not an actual viable solution cuz this would be O(n) at least
=> use the existing matrix


INSIGHT: binary search just eliminates search space to find answer thru process of elimination
- don't view as specifcally using midpoint to guess what it is. => what can we eliminate??


PLAN:
leftmost possible value = l = matrix[0][0]
rightmost possible value = r = matrix[len(matrix) - 1][len(matrix[0])]

=> need to split them up into separate values since they aren't the same dimensions
l_r = 0
l_c = 0
r_r = len(matrix) - 1
r_c = len(matrix[0]) - 1


how to calculate the midpoint between the 2?, would need to calculate it for both row and column?
- need to calculate midpoint for both row and for col

if matrix[mid_r][mid_c] < target: mid_c - 1 if r_c is not 0, else update mid_c to rightmost value, and decrement r instead
- same process would apply to matrix[mid_r][mid_c] is > target

"""

"""
solutions after seeing hints 1 - 2: check if target is between first element in row and last elemtn in row
if not, increment row, if yes: preform normal BFS on it
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r = 0
        r_r = len(matrix) - 1
        while l_r <= r_r:
            mid_r = l_r + (r_r - l_r) // 2
            # 3 cases
            if target >= matrix[mid_r][0] and target <= matrix[mid_r][len(matrix[0]) - 1]:
                print("found correct row")
                # preform BS on this column to find the column within the correct num range of the row
                l_c = 0
                r_c = len(matrix[0]) - 1
                while l_c <= r_c:
                    mid_c = l_c + (r_c  - l_c) // 2
                    if target == matrix[mid_r][mid_c]:
                        return True
                    elif target < matrix[mid_r][mid_c]:
                        r_c = mid_c - 1
                    elif target > matrix[mid_r][mid_c]:
                        l_c = mid_c + 1
                return False
            elif target < matrix[mid_r][0]:
                r_r = mid_r - 1
            elif target > matrix[mid_r][len(matrix[0]) - 1]:
                l_r = mid_r + 1

        return False


      
        