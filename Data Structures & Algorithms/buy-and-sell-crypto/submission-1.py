"""
single day to buy is left pointer
different day to sell is a right pointe
profit = right pointer - left pointer

looking for the max profit you can make from the array

insight: right pointer always has to come after left pointer i.e you can't sell before you even bought it

brute force: O(n^2) nested for loop

can we do it in O(n)?

should be greedy: calc profit everytime right > left, no point in calculating neg profit

when do you move the variable window? -> if you find a value that is less than left pointer. 
=> this is because if you find a value less than left pointer, that value will be able to create 
=> a bigger profit with any future possible values than the existing pointer because this new value is less than that one
=> so greater distance
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 # default value if you don't make any transactions
        l = 0
        r = 1
        # double check the end condition.
        while l != len(prices) and r != len(prices):
            
            if prices[r] < prices[l]:
                l = r

            if prices[r] >= prices[l]:
                currProfit = prices[r] - prices[l]
            r += 1
            maxProfit = max(currProfit, maxProfit)


        return maxProfit