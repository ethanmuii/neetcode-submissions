"""
requirements:
- all integers in nums are unique, no duplicates
- list of unique combinations that sum to target
=> don't care about ordering, don't care about duplicates (and no duplicates anyway)
=> combination length as long as it sums to target
- ALL integers in nums must be positive numbers (> 0)

constraints:
- nums basically represents the number bank. you can choose the same number multiple times. i.e choosing 2 twice or three times, etc. 
- you want to return early though i.e not keeping choosing the same number over and over IF your current value is greater than target. i.e prune it because there's no point in adding more to it

- do we need to keep track of frequency of each chosen numbers or iterate it in a way where we need a set to keep track of unique combinations? -> YES, WE DO. 
- we can still use a start index, but keep it at 0, to start, and then it gets incremented each time. 
=> unique combinations while allowing object re-use is like combinations + permutations mixed

insight: pruning would be easier if you sort the nums, then you can prune faster because if the earlier index is bigger than target, don't have to check the rest. 

edge case:
- my solution doesn't properly handle different orderings but same freq of each number
=> TODO: need to figure out a way to NOT check duplicate combinations, extra pruning that is NEEDED.

ways to handle this problem:
- keep ans in a set? and then when you add to set, sort the list and make it into a tuple?

FIRST SUBMIT: code is too inefficient so need to prune more, sort the list
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr_value = 0
        curr_path = []
        unique_combinations = set()
        nums.sort() # ascending
        def backtrack(start):
            nonlocal curr_value
            nonlocal curr_path
            nonlocal ans
            if curr_value == target:
                unique_combinations.add(tuple(sorted(curr_path[:])))
                # TODO
            elif curr_value > target:
                # TODO

                return
            else:
                for i in range(start, len(nums)):
                    curr_path.append(nums[i])
                    curr_value += nums[i]
                    if curr_value > target:
                        curr_value -= nums[i]
                        curr_path.pop()
                        break
                    else:
                        backtrack(i)
                        curr_value -= nums[i]
                        curr_path.pop()
    
        backtrack(0)
        for combination in unique_combinations:
            ans.append(list(combination))
        return ans

            
        