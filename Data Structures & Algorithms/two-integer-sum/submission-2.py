"""
REACTO
- Guaranteed to have a pair of values that can sum to target?
- Can't reuse the same indice in the answer pair
- Return the smaller index first in the pair
- RETURN THE PAIR OF INDICIES!!! NOT values. Return the answer as an array of length 2. 
- all values unique in the array?

- brute force (double for loop) => checks every possible combination
- two pointer => allows you to check every combination w/o re-checking combinations you have already checked before
    - this condition only uphelds itself if the array is sorted.
    - the sorting allows you to move the pointer in the right direction and eliminates choices. w/o sorting, the direction of the pointer is random
- hash map: instead of checking every combination, it allows you to 


- Why is the hash map method better than the two pointer method? 
    - hash map method is O(n) time complexity, while two pointer method is O(n log n)

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key = value, value = index value of element
        # the hash map can double as the elements we've currently seen AS we iterate through nums
            # also allows us iterate through the values in smallest index seen first
        # check if target - current_value is in the hash map => allows us to see if we can make a pair
        hashmap = dict()

        ans = []
        # iterating through array
        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                ans.append(hashmap[(target - num)])
                ans.append(i)
                return ans
            else:
                hashmap[num] = i # ordeer of this check is important because remember we can't use same indices twice. 
                
        return 0 # just need to return something. this condition should never execute



        