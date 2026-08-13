"""
requireements:
- return a list of lists where each sublist is a subset of the given input array
- empty arary is considered a subset
- no duplicate subsets
- subset: a group of numbers (if not empty) from the input array. different lengths and also different amounts

constraints:
- no duplicate subsets but there are duplicates in the input array
- sort the input array so we can skip using the same number on the same recursion/tree level
=> not necessarily if they are at different levels. 
- rest of the process stays similiar to original subset problem. 

identify base case(s):
- order should mean you always add to array, not specific condition needed to be met.
- no duplicate subsets can be started meaning, one branch should cover adding all of that value whether its 1, 2, 3 depending on how many duplicate values there are of that value
=> the next branch shouldn't have that value in it at all. 
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        def backtrack(start, curr_path):
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr_path.append(nums[i])
                ans.append(curr_path.copy())
                backtrack(i + 1, curr_path)
                curr_path.pop()
        print(nums)
        backtrack(0, [])
        return ans