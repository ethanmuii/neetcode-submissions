"""
requirements:
- permutations, order of the numbers matters
- must use all values once in the array i.e can't just use 1 number in the array like [1] => not valid
- all values in the array are unique
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr_path = []
        used = [False] * len(nums)
        def backtrack():
            if len(curr_path) == len(nums):
                ans.append(curr_path[:])
                return
            # now need to perform backtracking
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                curr_path.append(nums[i])
                backtrack()
                curr_path.pop()
                used[i] = False

        backtrack()
        return ans

