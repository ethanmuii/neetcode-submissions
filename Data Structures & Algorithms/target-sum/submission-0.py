"""
requirements:
- given an array nums and target
- returning the number of DIFFERENT WAYS i.e paths that sum to target. 

constraints:
- duplicate numbers allowed in nums
- each index's number in the array can be used once in the "path"
- each index's number has 2 choices, plus or subtraction to the current total. -> it isn't choose or not choose.


how do you want to visualize this problem:
- variables are:
== number of different ways we have found to build target
== current total
== the choice if we subtracted it or added it. 

- the number in the 2d DP array can represent the number of ways we have found so far -> and our answer can be sum of both added and subtraction columns?
- 2 columns, one column represents the integer index and the other column represents 0 for subtracted this number, 1 for added this number. 
==> PROBLEM: how do you keep track of what the previous total so you know what the current total will be?
===? what if we track number of ways outside the DP array? and each number in the dp array represents the total

-> wait it becomes exponential in a sense since each index's number can be positive or negative and then that number can be added to either the positive or negative total of the previous number. so how does the gird look?

- should you prune prematurely and not count totals that are greater than target. 
=> maybe create an n x n grid where n = len(nums)
=> its still 2d, but how do you visualize the totals and base cases
since lets say you have a number and its starting possible total is +2, -2
-> then for the next number is 3, 3 can be used as +3 or -3
=> you can do +3 on +2 or +3 on -2, and you can do -3 on +2 or -3 on -2
=> and this keeps on happening for each number. 

edge cases:
- nums length guarantee to have at least 1 element


AFTER USING HINTS:
- what should your grid state store?
- row = each index, but how many number of possible columns should you have? and what should these columns represent
- need offset since you can't index w/ negative values. 
- out of bounds is 0 ways to make that


"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = 2 * sum(nums) + 1
        # create the array
        dp = [[0 for _ in range(n)] for _ in range(len(nums) + 1)]
        
        # base cases:
        dp[0][sum(nums)] = 1
        for i in range(1, len(nums) + 1):
            for j in range(0, n):
                val1 = 0
                val2 = 0
                if (j + nums[i-1]) >= 0 and (j + nums[i-1]) < n:
                    val1 = dp[i-1][j + nums[i-1]]
                if (j - nums[i-1]) >= 0 and (j - nums[i-1]) < n:
                    val2 = dp[i-1][j - nums[i-1]]
                dp[i][j] = val1 + val2

        if target < -sum(nums) or target > sum(nums):
            return 0
        return dp[-1][sum(nums) + target]


