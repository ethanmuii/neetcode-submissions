"""
requirements:
- nums has no duplicates
- subset: a unique combination or "group" of nums

constraints:
- solution set must not contain duplicate subsets, either check via combination like only iterate forward where a value is globally taken across all branches once used doesn't matter at what "depth" or "order"
=> or can just use a set to not store duplicate subsets but requires sorting a tuple solution. NOT AS OPTIMAL

edge case: empty [] is a valid subset of nums
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        active = []
        def backtrack(start):
            if active not in ans:
                print(active)
                ans.append(active[:])
            for i in range(start, len(nums)):
                active.append(nums[i])
                backtrack(i + 1)
                active.pop()


        backtrack(0)
        return ans