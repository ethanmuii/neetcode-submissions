"""
- similiar problem setup as House Robber I except the first house and last house are now neighbors (cycle)
- cycle just makes it where if there is 3 values, you can only choose 1. 
i.e 1st element depends on last element, choosing the 2nd element depends on first element, and last element also depends on first element (since last element is next to first)

requirements:
- still need the max_amount variable
- base case: 0 elements return 0
- base case: 1 element return nums[0]
- base case: 2 elements? the first element now also depends on the last element so its optimal value is also the optimal between nums[0] and nums[-1] while nums[1] optimal is between nums[0] and nums[1]. 
=> THIS IS THE SAME EXPRESSION WHEN len(nums) == 2
return max(nums[0], nums[-1])

- what happens when len(nums) there is 3 elements?
- by choosing the first element, you can't choose the LAST ELEMENT or by choosing the last element, you can't CHOOSE THE FIRST ELEMENT.  -> how do you represent this in code?


- not quite idiomatic, but could add another base case where at memo[3], its the max between all 3. this way u can still use i - 2, nope this doesn't work because the base cases aren't accurate

THE BIGGEST CHANGE IS THAT you have to account for both the future and prev house. 
- with 3 elements, the answer is the max between the future and prev for every house where the prev of the 1st element is the last element and the future of the last element is the first element

- how does this concept apply when you go to 4 houses?
input: nums=[1,2,3,1]
- 3 can choose 1 since its not the last element, but 2 or the last 1 cannot. 
- the last element can only choose whats at memo[1] i.e memo[i - 2] in this case IF memo[1] isn't us choosing the first element. -> if the last element wants to choose memo[i - 2], it would have to have been the value at nums which is 2 in this case. 


edge cases:
nums = [3,4,3]

nums = [2,9,8,3,6]
max_amount = TODO
memo[0] = max(nums[0], nums[-1]) = max(2, 6) = 6
memo[1] = max(memo[i - 1], nums[1]) = max(6, 9) = 9
memo[2] = max(memo[i - 1], nums[2] + memo[i - 2]) = max(9, 10) = 10
memo[3] = max(memo[i - 1], nums[3] + memo[i - 2]) = max(10, 3 + 9) = 12
memo[4] = max(memo[i - 1], nums[4] + memo[i - 2]) = max(12, 6 + 10) = 16 -> but this can't be allowed since the 10 from memo[2] included the FIRST ELEMENT which is not allowed if you choose the second element. 

nums=[1,1,3,3]

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        first = nums[0:len(nums) - 1]
        second = nums[1:len(nums)]
        def helper(sliced_array: List[int]) -> int:
            memo = [0] * len(sliced_array)
            memo[0] = sliced_array[0]
            memo[1] = max(sliced_array[0], sliced_array[1])
            for i in range(2, len(sliced_array)):
                memo[i] = max(memo[i - 1], memo[i - 2] + sliced_array[i])

            return memo[len(sliced_array) - 1]
        first_max = helper(first)
        second_max = helper(second)
        print(first_max, second_max)
        return max(first_max, second_max)