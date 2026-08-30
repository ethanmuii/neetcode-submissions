"""
what does dp[i] i.e state mean? -> number of ways to get to the i-th step out of n. 
- we need to include n
what are base cases?
- base case is 0 since there are 0 ways to reach the ith step, 1 way to reach 1st step. 
recurrence/translation: 
- since you can climb 1 or 2 steps at a time. the number of ways to get to the i-th step is the number of ways to get to i - 1 step and i - 2 step. would it also be + 2 for each way to get to that step i.e + 1 for the 1 step and + 2 second step. 
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        def dp(i):
            if i in memo:
                return memo[i]
            if i <= 1:
                return i
            result = dp(i-1) + dp(i-2)
            memo[i] = result
            return result

        return dp(n)