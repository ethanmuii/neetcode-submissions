"""
output should not contain duplicate triplets (meaning triplet of NUMBERS VALUES) cannot be same
- indices WITHIN the triplet should be unique, cannot use the same indice's value to make a triplet
=> BUT the value within the triplet can be the same as long as it comes from different indices
- triplets should sum to 0
=> no duplicate = use a set()
=> since order doesn't matter just iterate over set to return all values in a list

=> don't add an index's value to a set until we have finished checking ALL PAIRS that use that index before its the triplet value
"triplet value" can be defined as the needed value that we've seen in the past and have already checked pairs for

sets cannot hold mutable values
for groups of numbers in sets, need them to be sorted or have some sort of defined order to check for duplicates
sorted always returns a list
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        uniqueTriplets = set()
        seen_numbers = set() # don't need a hashmap since we don't need the index?
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                needed_value = 0 - nums[i] - nums[j]
                if needed_value in seen_numbers:
                    uniqueTriplets.add(tuple(sorted((nums[i], nums[j], needed_value))))
                
            # now that we are no longer using i in the original pair, we can add it to seen numbers
            seen_numbers.add(nums[i])
        ans = []
        # now grab all values from set
        for triplet in uniqueTriplets:
            ans.append(list(triplet))

        return ans

