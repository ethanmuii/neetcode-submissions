"""
answer: return indices of the number(pair) that equal target. cannot use the same index in the pair
- only one right answer
- smaller index in answer first. return answer as tuple or array?

- if we have to return small index, might as well remember the earlier indexs first in the pairs. 

solution(s:
    - brute force: double for loop through every possible combination => will check same pairs again
    - two pointer: utilizes 2 pointers to check every combination and moves left to right so you aren't re-checking the same pairs again. => need to be careful with index boundaries
    - hash map: for each index's number, it needs a specific number for it to meet the target value. as you iterate through the list, you are guaranteed to find that value. => this way you have indices and values. 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            neededValue = target - nums[i]
            if neededValue in ref.keys():
                return [ref[neededValue], i]
            ref[nums[i]] = i
            