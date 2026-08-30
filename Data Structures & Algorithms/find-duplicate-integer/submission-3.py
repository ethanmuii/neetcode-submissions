"""
requirements:
- each integer (1 to n inclusive) is used at most once in the array except for value that is duplicated
- return that duplicated integer
- n + 1 integers in the array because the default values are 1 to n and then there's one duplicated value that could be ANYTHING between [1 to n] which is that '+1 integer'

constraints:
- the highest 'n' can be is len(nums) - 1. This happens when all numbers are 1 to n and the + 1 is a ONCE duplicated integer where len(nums) is basically n + 1 = len(nums). The highest n can be is when all numbers are unique and there's only integer repeated ONCE. If all values were unique, then there would be no repeated integers at all. 
- ONLY ONE INTEGER CAN BE DUPLICATED (not multiple)

edge case:
- length of 1 for list
- the repeated/duplicated integer can be USED more than 1+ times i.e it can be duplicated any number of times
- nums=[1,2,4,2,2] -> if an integer is repeated more than 1 time, then it means we won't see one of the values in the possible value range i.e 3 in this case. it doesn't necessarily shrink the space each time by 1 i.e the range becomes 1 to 3 because there are 3 2's. you can also not have 3, and include 4. i'm trying to say the space doesn't shrink like that. 


CAN YOU MAKE A SOLUTION IN O(1) space?
n = 4 from len(nums) - 1 then 4 + 3 + 2 + 1 = 10 and then the total of nums - 10 gives the value that was duplicated.  -> this doesn't work since we are addin up to 4 numbers together while nums has 5 and depending on the duplicated value it could equal the same. 

- summing up numbers and trying to calculate the sum numbers versus expected does not help. we don't know the order of the integers nums or how many times the duplicate number appears.
=> every number appears 0 or 1 time, besides 1 that appears 1+ times. 

- what if you manipulate it where if you see the nubmer again its flip the sign? like if you see another 2 it becomes -2 or something. 
- constraint: you don't the expected values in the future and you can't remember the values in the past so how do you solv ethis problem?

slow and fast pointers
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        