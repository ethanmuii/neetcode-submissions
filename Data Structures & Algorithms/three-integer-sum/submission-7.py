"""
- return triplet of VALUES -> set of values must sum to zero.
- indices cannot used be more than once in a triplet. BUT can use the same value as long as its from a different index

- output should not contain DUPLICATE TRIPLETs even if they are created using different set of indices. 

algo:
use hash map to track what values you've seen like you did in 2sum, but only add it to the seen hashmap AFTER you aren't using it at all during the 2 pointer check. 

time complexity is O(n^2) since you are iterating over each value once, and then once again of the inner loop during two pointers. 

the two pointer and hashmap makes sure you don't check the same triplet twice

hashmap: key is the value, value is the index
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        ans = []
        uniqueSets = set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # calc the needed value that we may have seen
                neededValue = 0 - nums[i] - nums[j]
                # yes we've seen it?
                if neededValue in seen:
                    uniqueSets.add(tuple(sorted((nums[i], nums[j], neededValue))))
            seen[nums[i]] = i

        for triplet in uniqueSets:
            ans.append(triplet)

        return ans