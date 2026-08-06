"""
answer: list, same length as the original nums array. 

goal: for each index in ans, need to multiply all the numbers before that index, and after that index. 
brute force: 
- double for loop, where outer for loop iterates gets an answer for each number/index
- inner for loop does the work of calculating the before and after

how does prefix and postfix relate to this?
- for each number in nums, there is a product of the subarray before it and product of subarray after it. 
=> want to find a formula to calculate each of those subarrays in O(1) time after precomputing

with division: 
product of subarray before a nums[i]: just look at the prefix
product of subarray after a nums[i] using prefix array: P(L, R) = P(R) / P(L) - 1 


without division: 
prefix_multiplication = [1, 2, 8, 48]
postfix_multiplication = [48, 48, 24, 6]

product of array except num[i] = prefix_multiplication[i - 1] or 1 * postfix muultiplication[i + 1] or 1
=> then just need to be careful proper index bounding
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # calc prefix product
        prefix_list = []
        running_prefix = 1
        for num in nums:
            running_prefix *= num
            prefix_list.append(running_prefix)

        print(prefix_list)
        # calc postfix product
        postfix_list = [] # can build it from prefix??
        running_postfix = 1
        for num in reversed(nums):
            running_postfix *= num
            postfix_list.append(running_postfix)
        postfix_list = list(reversed(postfix_list)) # is there a way to do it without this

        print(postfix_list)
        # now calculate the prefix and postfix except num[i]
        for i in range(len(nums)):
            l = i - 1
            r = i + 1
            if l < 0: 
                prefix = 1
            else:
                prefix = prefix_list[l]

            if r >= len(nums):
                postfix = 1
            else:
                postfix = postfix_list[r]

            ans.append(prefix * postfix)
        

        return ans

        