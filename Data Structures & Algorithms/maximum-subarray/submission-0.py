"""
requirements:
- find the largest sum in the array. sum can only be made up of consecutive elements (subarrays) i.e can't pick and choose elements
- array is non empty, at least 1 element


constraint:
- we don't know what elements will be in the future
- want to keep solution O(n)

insight:
- we know whether to restart or keep an element based on whether an element max subarray sum will become bigger than the number itself or if its better to just use that number.
=> the moment you have/get a sum that is less than (or more negative) than what you are currently working with, its better to drop it.
=> do  you want to take dead weight basically?

edge element:
- current_sum and max_sum have to be the first element in the array (guaranteed). can't be 0 since negative elements are technically allowed.
- if you really wanted to start with a base value the sum has to be like the most negative value * (num elements in the array) for a valid max comparison
- since we are already adding the first element, need to make sure we start from the 1 whether that's a valid index or not,
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            # do we want to keep this element or start over?
            current_sum = max(nums[i], current_sum + nums[i])
            # then is this new current_sum greater than existing max_sum?
            max_sum = max(max_sum, current_sum)
        return max_sum
