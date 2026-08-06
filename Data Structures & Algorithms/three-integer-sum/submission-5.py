"""
answer = list
- return all the unique triplets (numbers)
- triplets with same numbers, but different triplet indexs used are still considered the same
- cannot use the same index twice within the same triplet
- can use the same index with different triplets
- output doesn't have to be in any order
- output can't contain duplicate triplets -> use set to store triplet pairs
=> need to make sure different order of numbers in the triplet but same numbers are recognized as same 
so need to sort the triplet number so set() treats them the same

O(n^3) brute force but we are duplicate checking

better solution: two pointer + hashmap 
key: value we need given the values of 2 pointers
do we need only the value? like i don't think we need the index for anything, but i guess we can store the index as value

be careful about your ordering. remember the same index cannot be used twice within the same triplet
**ONLY WANT TO ADD A VALUE AS SEEN ONCE WERE NOT CREATING ANY MORE PAIRS WITH IT
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        hashmap = {}
        triplets = set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                needed_value = 0 - nums[i] - nums[j]
                if needed_value in hashmap:
                    triplets.add(tuple(sorted((nums[i], nums[j], needed_value))))
            hashmap[nums[i]] = i

        for triplet in triplets:
            ans.append(list(triplet))

        return ans






