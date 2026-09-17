"""
requirements:
- given array of numbers (different denominations)
=> can use the coin as many times as you want, would want to prune early though if it created amount greater than "amount" I.E TARGET
- values in coins are unique


constraints:
- number of distinct combinations i.e combinations can be of different lengths, the freq of each coin in an answer can't be the exact same i.e same coins used and same freq per coin
- no coin is negative or 0


breaking down the problem:
- each row should be represented by that index maybe? like including that coin as a possibility choice?
- need to track current amount?
- and possibly number of distinct combinations
- our answer should ideally we be last row and the target[amount]. 
=> we can for sure get past that number, its just whether we can get exactly that number since no coins are negative


= since no coins are negative, we basically only need to track 0 to amount right? and the number of ways to reach '5' for example wiht this current coin i, is just 5 - current coin i. i.e lets say current coin was  1 and we want to reach 5. the number of ways to reach 5 is just number of ways to reach 4 and you are adding coin to each of the ways to reach 1. 
=> however this statement is under the assumption that we can only use a coin once. 

maybe think about this backwards: number of ways to reach target is just target - (each number in coins)
ex. amount = 4, coins = [1,2,3]
-> dp[-1][4] is just dp[-1][4-1] + dp[-1][4-2] + dp[-1][4-3]
=> HOW DO YOU ACCOUNT FOR THE FACT THAT YOU CAN CHOOSE/USE THE COIN MULTIPLE TIMES
- for each possible total i.e 0 to amount, you try every possible total you can make with unlimited coins betweent he subset and don't prune unless you go over the amount its like a tiny recursive helper function for each possible total amount

with each coin (you can use it unlimited amount of times) so its like you need to check number of ways you can make total - coin * 1, total - coin * 2, total - coin * 3, as long as the total is above 0. and thats ur answer. 

do you want inner or outer loop to be totals or coins?

edge cases:
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # base case: with zero coins, there is one way to make amount 0. 
        for x in range(len(coins) + 1):
            dp[x][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                val = 0
                if j - coins[i-1] >= 0:
                    val = dp[i][j-coins[i-1]]

                dp[i][j] = dp[i-1][j] + val

        return dp[-1][amount]



        