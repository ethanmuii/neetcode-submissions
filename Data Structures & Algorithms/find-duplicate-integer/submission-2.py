"""
- n = len(nums) - 1)
- every value in the array is from 1 to n
- just because the value CAN be in that, doesn't mean it is technically in the array
=> ex 1. technically  4 can be in the array as well, but it isn't.
=> every integer can appear at most once => i.e 1 or 0 times
=> and one integer is repeated. 

brute force:
- use a set() and check for the number that causes duplicate 
=> O(n) space, O(n) time
- sort the array and then check for repeated numbers now that they are adjacent to each other
=> O(n log n) time and O(1) space


***FOLLOW-UP: CAN YOU SOLVE THE PROBLEM WITHOUT MODIFYING THE ARRAY NUMS AND USING O(1) EXTRA SPACE?
- O(1) extra space means only using pointers or variables
- no extra data structures besides the array and can't even do anything with the array

we know
- len(nums)
- possible values in array is 1 to n
n = len(nums) - 1
- can access element in O(1) time
- every integer appears 0 or 1 time besides one (which appears at least 2). 

ideas:
- could do a running count?
- what if we sum of all numbers from 1 to n, and then as we through the list we do n - that number, the number leftover at the last index has to be repeat of something we saw before, and the subtraction crosses out all the numbers we have seen

# if we are making nums a hashset inside, how do we do it without affecting values we  have already seen
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        n = length - 1
        # after seeing hint 3, you can tell an element is a duplicate if you the value the value goes from negative to positive
        # this is because none of the starting values can be negative
        # if we seen it once, it will turn negative and then if we see it again it will turn positive
        
        # you can't just check for the values that are still positive as duplicates after you've performed all the actions
        # this is because there could be a number that has been seen 3 times and the number would still be negative at the very end
        for i in range(len(nums)):
            before = nums[abs(nums[i]) - 1]
            nums[abs(nums[i]) - 1] *= -1
            after = nums[abs(nums[i]) - 1]
            if before < 0 and after > 0: # it was negative and turned positive
                return abs(nums[i]) # need it to be positive, since the correct repeated value should be the positive version, not NEG
