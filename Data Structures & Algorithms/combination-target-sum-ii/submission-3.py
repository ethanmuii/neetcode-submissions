"""
requirements:
- list of unique combinations (order doesn't matter) that meet target
- input array contains duplicate values (you can only use a value as much as the freq it appears in the input array)

constraints: 
- index from input array may be chosen AT most once. i.e either choose it or don't choose it. => do you have to make decision to choose it or not choose it based on given state? or should you just brute force try both.
- because duplicates are allowed: need to skip duplicate elements being the first element regardless of whether they are next to each other or not.
=> ONLY THE LEFT MOST ONE should be recursed upon, the righter duplicate(s) will check a subset of the left original one, which is pointless and leads to duplicate combinations

- because of recursion and combination, we should still keep track of start pointer. 
- just need to backtrack both with the value and not with the value? - binary choices


THE PROBLEM: you don't want to start with the same value (even from different indexs) more than once, leads to duplicate combinations. 
=> need to append it to a "used" set but only for the first function, don't want it to happen for every recursion. we also don't want it
=> checking that you aren't recursing on the same starting ensures some no duplicate solutions like [2,6] and [2,6] are the same even though they come from different index 2's.

TODO: still need to figure out [1,7] and [7,1]
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr_value = 0
        curr_path = []
        candidates.sort()
        def backtrack(start):
            nonlocal curr_value
            nonlocal curr_path
            nonlocal ans
            if curr_value == target:
                ans.append(curr_path[:])
            else:
                for i in range(start, len(candidates)):
                    #print(i, curr_value, curr_path)
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    if curr_value + candidates[i] > target:
                        break
                    curr_value += candidates[i]
                    curr_path.append(candidates[i])
                    backtrack(i + 1)
                    curr_value -= candidates[i]
                    curr_path.pop()
                    
        backtrack(0)
        return ans
