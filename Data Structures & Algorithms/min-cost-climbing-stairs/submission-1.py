"""
- we are using the indexs in this example
- min cost to reach len(cost) where len(cost) represents the index past the last valid index
- can start at cost[0] or cos[1]
- from each floor (after adding the cost), you can either jump 1 floor or 2 floors.

we can break it down into subcases by defining the min cost to REACH this index. not including this index. 
- ultimately you are just comparing the min cost between i - 1 floor and i - 2 floor and whatever one is cheaper is the cheapest version to reach ith floor after adding cost[i -1] 

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        n = len(cost)   
        dp = [0] * (n+1) # n represents the min cost to reach len(cost) i.e the index past last index in cost

        # base cases of starting at index 0 or index 1
        dp[0] = 0 # 0 cost to start there
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]
