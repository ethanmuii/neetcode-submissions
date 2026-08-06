"""
answer format:
- must be values, not indices
- indices cannot be reuses
- list of lists where each sublist is length 3. 
- each sublist should be unique in values (regardless of order of the triplet)
- actual groups themselves can be returned in any order

problem notes:
- values can be the same though
- looking for valid solutions tha tmeet a condition

problem questions:
-> can we do it in O(n)? or O(n^2)?
=> O(n) is not possible since we need to check every combination and not possible to do with triplets
=> also cannot eliminate where to look since its not sorted
- brute force is O(n^3) to check every combination
-> to make sure we don't use duplicate triplets, we can store them in a set as tuples? and then return it as a list later on

solutions:
- can turn it into a 2sum non-decreasing problem if you choose to sort the nums array
=> time complexity becomes at least O(n log n) then though.


solution:
- use 2 pointers, but also use a hash map to remember if you've seen a value that you need. 
=> its how you don't need to check duplicate triplets you've already seen and if it can form a valid triplet 
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        solutions = set()
        hashmap = {} # key: value, value: index
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                needed_value = 0 - nums[i] - nums[j]
                if needed_value in hashmap and tuple(sorted((nums[i], nums[j], needed_value))) not in solutions: # needed_value is in hashmap
                    print(i, nums[i], j, nums[j], needed_value)
                    solutions.add(tuple(sorted((nums[i], nums[j], needed_value))))
                # if is not a possible triplet currently, just add that value to hashmap
            hashmap[nums[i]] = i
        # convert tuples in set to lists
        for triplet in solutions:
            ans.append(list(triplet))

        return ans 
                    





        