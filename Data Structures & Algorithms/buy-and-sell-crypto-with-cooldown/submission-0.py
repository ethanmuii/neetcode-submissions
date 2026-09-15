"""
requirements:
- return the MAXIMUM PROFIT YOU CAN CREATE. -> after buying-selling multiple times

constraints:
- can hold one neetcoin at a time, i.e you can't buy a coin until you sell the current one you are holding
- can't buy a coin the day after you sell -> MUST WAIT ONE DAY. 
- unlimited transactions. 

insights: 
- possible solution, not optimal would be to buy whenever you know there is a future price that is bigger. -> creates a profit, but doesn't account for is this the most profit NOR you can't buy the following day which could have created a bigger profit

- at each item, you can either buy it or skip it. 
- whenever you currently hold an item, you can sell it. 
- hardest part to figure out is how to track STATE?
=> i could be like up to 'i' items?
=> value should represent the maximum profit you can create up to 'i' items
=> however, how do you represent buying/selling dates? should i mean like bought and j mean sell it dates? 
=> like prices[0][1] means i bought at price 1 and sold at price 3 and the value is 2?

- should we like pre-calculate the total amount of money each transaction could make which is just a double for loop? since you can't sell later than you bought, and then do DP to get the max amount of money you can make since we can access the max amount buying on that day could make or we could skip it. 


edge cases:
- if length of prices is only 1, you can't make any profit so return 0. 

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        grid = [[0] * 2 for _ in range(len(prices))]

        # base cases:
        grid[0][0] = 0
        grid[0][1] = -prices[0]

        grid[1][0] = max(0, prices[1] - prices[0])
        grid[1][1] = max(-prices[0], -prices[1])

        for i in range(2, len(prices)):
            grid[i][0] = max(grid[i - 1][0], grid[i-1][1] + prices[i])
            grid[i][1] = max(grid[i-1][1], grid[i-2][0] - prices[i])


        return grid[-1][0]