"""
matrix[0][0] = top left
matrix[len(m) - 1][len(n) - 1] = bottom right

can view the whole matrix in ascending order if you were to flatten it where you add each row at a time to a bigger list 
the far most right element is less than the first element in the row below it
its like left to right then diagonal back to left

solution that runs in O(log(m * n)) time means binary search

brute force:
- search each row to check if target is in the leftmost element and rightmost element of that row's range,
=> if yes, then for loop through it to find the target
=> if you reach the end of the row, then target is not in there. return False

optimization: 
- once you find the correct row then you can binary search through the columns of that row
=> to find the target and if you don't find it then return False. 
=> allows you to eliminate half of the column space each iteration
=> O (n log(m))

optimization: can you binary search on the rows?
- calc the midpoint row, and then do if target < leftmost element in that midpoint row
=> move possible rows from 0 to that row - 1
=> if target > rightmost element in that midpoint row
=> move possible rows fromm that row + 1 to len(matrix) - 1
=> else: the value is in this row's range possibly so preform binary search on the columns
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # preform binary search on the rows
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                l = mid + 1
            else: # preform column binary search
                l_c = 0
                r_c = len(matrix[0]) - 1
                while l_c <= r_c:
                    mid_c = l_c + (r_c - l_c) // 2
                    if target < matrix[mid][mid_c]:
                        r_c = mid_c - 1
                    elif target > matrix[mid][mid_c]:
                        l_c = mid_c + 1
                    else:
                        return True
                return False

        return False