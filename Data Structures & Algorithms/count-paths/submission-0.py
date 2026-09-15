"""
requirements:
- 2 choices, down or right -> this is where you could come from
- returning the number of TOTAL UNIQUE PATHS to reach bottom right corner from top left
- the state[m - 1][j - 1] should be the total number of unique paths
- each 2d state can store the number of paths to reach that index. and then the number of paths to reach a new space is just the combination of the up or left. 

constraints:
-


edge cases:
- 
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        state = [[0] * n for _ in range(m)]
        state[0][0] = 1 # 1 way to get that part
        for j in range(n):
            state[0][j] = 1
        for i in range(m):
            state[i][0] = 1


        for i in range(1, m):
            for j in range(1, n):
                state[i][j] = state[i-1][j] + state[i][j-1]

        return state[m-1][n-1]