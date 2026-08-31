"""
requirements:
- want to make the EXACT TARGET AMOUNT
- want the fewest number of coins to get there.
- you can use each coin/dollar amount avaliable to you unlimited amount of times as long as you are given that amount in coins somewhere then you can use that amount unlimited times (but want fewest)
- if impossible to make the EXACT target, then return -1

constraints:
- what would the state represent here? => you're considering amount trying to reach and coins you have access to. 
=> state could be number of coins used?, do you want to always choose the highest coin that you can add which still makes it <= amount? 
=> this is false for edge case 2


edge cases:
- impossible to make that target amount with that coin bank and any number of combinations of that coin bank. OR AL starting values are greating than amount.

- coins=[2, 4, 5] amount=6 => here we want to choose 4 first even though its not the BIGGEST Coin we can choose under 6. 

insight: i can kinda visualize the problem like backtracking/recursion where we try every path and a path ends when it puts us OVER THE AMOUNT. if no paths are right, then we return -1. -> how do we turn this into DP where we aren't calculating the subcases over and over. 
- try backtracking first


=> maybe state should be the number of coins to reach each amount from 0 to amount where you do [-1] to len(amount) + 1 so we account for number of coins to reach amount as one. 
number of coins to reach 0 is 0
=> each subcase builds off one another because the number of coins to reach 6 is just number of coins to reach 5 + however many coins it takes to reach 6?
=> if you can't reach an amount with your given coin bank, it stays -1, and you want to keep on iterating back until you find an amount that is not -1. if you can't build the target from that amount that isn't -1, its not possible?
=> if all values are -1, then its not possible

=> edge case: what if you get to a value that isn't -1, and you can't build to target amount, should you return -1 or should you TRY ALL possible amounts are not -1. you should try all values that are not -1 -> YES, for example this example: coins = [2, 7] and amount = 10. '9' can be made with 2 + 7, '8' can be made with 2 + 2 + 2 + 2. just because 10 can't be amde by looking at '9', it can be made if you look  at '8' and then add 2 which makes 10's min coins to be 5 coins to make 10. 
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [(amount + 1)] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j] and memo[i - coins[j]] != (amount + 1):
                    memo[i] = min(memo[i], memo[i - coins[j]] + 1)



        if memo[amount] == amount + 1:
            return -1
        return memo[amount]