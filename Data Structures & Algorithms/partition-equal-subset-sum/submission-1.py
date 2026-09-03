"""
requirements:
- return boolean if we can partition the array into two subsets where the sums of subsets are equa
- partitions don't have to be CONTINIGIOUS like with substrings. partition just means choosing which elements to be in one subset vs another.
- each element has 2 options, be in partition A or partition B. 
=> THUS, the number of possible combinations (i.e partition the array of elements into 2 different subsets IS 2^len(nums))

constraints:
- brute force of checking every possible combination (of partitions), it would take O(2^len(nums)) time to iterate through every possible combination, and then you have to compare the sums between the partition and save the answer which could be at max O(n) if one partition has all the elements
=> THERE HAS TO AT LEAST ONE VALID PARTITION and then we can return true. If no valid combinations/partitions are possible, then return False. 

KEY PROBLEM: how can we check every possible combination since technically you can choose 2 elements to be in one partition that are not in continigious, its not like substrings. like if we wanted [1, 4] to be one subset in [1,2,3,4]
- we don't want the state to hold the sum at that index since it varies at partition points
- paritioning the array into 2 subsets means we basically get 2 PARTITION POINTS
=> we could do like a l and r partition points. any elements within (inclusive) these bounds is one subset, but then how would you effectively count the other stuff outside of it. like 1 and 4, if the partitiion boundaries don't reach the fully exterior like 0 or len(nums). => wait you could just do sum(nums[O:l]) and sum(nums[r:len(nums)]). YES LIKE THAT


- what should dp[i] state store?
- how can you map the partition points. don't care what the partition points (i.e left, right) as long as it equals condition.


- currently our solution is O(n^3) since it takes O(n^2) to check every possible combination of partition points (l and r), and then it takes O(n) to sum up the subsets and then compare them. 
=> is there anything we can pre-compute ahead of time to know each prefix/postfix's or partition's sum, and then the check just becomes O(1)? if we already know the sum's.


- doing the expand around the center way: could just check each possible center point and if sum of the the partition is equal to half of the total of len(nums), then we can return True and break form the array. 
=> WAIT BOTH MY SOLUTIONS ASSUME THAT YOU HAVE AT LEAST ONE CONTINIGIOUS SEQUENCE OF ELEMENTS IN A PARTITION, but what if you go an the alternating route like index 0 in sub1, index 1 in sub2, index 2 in sub1, my code doesn't properly handle that i.e nums = [14, 9, 8, 4, 3, 2]
-> I don't even know how to do it, if I can't precompute possible combinations too. 


edge cases:
- nums can't be empty. 
- what happens if nums has one element? => auto false, elements can't be in both subset1 and subset2.
- do subsets have to be same length? => NO, a valid case is [1,2,3] which should return True. 

insights:
- answer can only be valid if its a whole number
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        memo = [False] * (target + 1)
        memo[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                memo[i] = memo[i] or memo[i - num]


        return memo[target]