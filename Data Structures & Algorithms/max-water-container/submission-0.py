"""
answer: integer, want the maximum

how is maximum calculated? -> rectangle (l and r) where they are indexs in heights
- and the height used for caclulation is min(heights[l], heights[r])

instead of checking every possible combination in O(n^2), can we check in O(n)?
=> 2 pointer? -> how do we know when to move it left or right? -> always move the limiting one (i.e no max one)
-> this is because future bar can make a bigger water container with the existing max one.
-> you won't run into a combination that can't be made with bigger one, but can be made with the smaller one
=> THIS IS OUR ASSUMPTION AND CONDITION, similar to two pointer after sort in 2 sum.
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVal = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            val = (r - l) * min(heights[l], heights[r])
            if val > maxVal:
                maxVal = val

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxVal

