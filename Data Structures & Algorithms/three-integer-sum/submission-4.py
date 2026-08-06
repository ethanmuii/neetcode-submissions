"""
answer: wants distrinct triplets (values that sum to 0)
- indice can not be reused within a same triplet
- even if different triple of indices make their values sum to 0, it doesn't matter if those triplet of values are already in the answer
- going to have at least 3 values in the array
- for each pair, check if the value you need already exists in the set, if it does then you can form a triplet.
=> need to make sure you check this before you add these values to the set, because you don't want to accidentally use the same index twice because your double counting the one you have and the one you just added even tho it was never there in the first place

hash set to make sure you aren't counting duplicate triplets. need to make sure you sort the triplet beacuse tuplets will count them as unique
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        ans = []
        unique = set()

        for i in range(len(nums) - 1): # want to exclude the last valid element since that's where j will be
            for j in range(i+1, len(nums)): # i and j can't be the same
                needed_value = 0 - nums[i] - nums[j]
                if needed_value in unique:
                    print(i, j, nums[i], nums[j], needed_value)
                    triplets.add(tuple(sorted((nums[i], nums[j], needed_value))))
            unique.add(nums[i])


        for triplet in triplets:
            ans.append(list(triplet))

        return ans