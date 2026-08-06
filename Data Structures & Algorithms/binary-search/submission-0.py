"""
values in nums have no duplicates. sorted in ascending -> what does that tell us?
=> can eliminate values because if that value isn't a valid answer, the values to left or right wouldn't be either. 

Binary search left = starts with the leftmost possible answer in search array
binary search right = starts with the rightmost possible answer in search array

answer wants index returned
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r: # to check every possible value before we declarae no answer
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                l = mid + 1
            else:
                r = mid - 1

        return -1