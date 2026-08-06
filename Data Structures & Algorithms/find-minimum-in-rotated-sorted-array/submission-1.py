"""
- remember indexs wrap around
- rotating n times just gives back the original array
- problem: we don't know how many times it has been rotated so we don't know where the minimum element would be in the array
=> array used to be ascending order

IN B.S: we want to find what makes the search array predictable, allows us to limit it in O(log n) time.

- after rotation, there is technically 2 sorted arrays => the rotated part and then where the old sorted array part
=> ex. 3,4,5,6 is one sorted part and 1,2 is the other sorted part. 
=> basically want to find where the rotation ends and the new part begins again => that is where the minimum element is
=> however, we don't know how much it was rotated
=> can the 2 separate sorted arrays tell us enough

WHAT DOES THIS INSIGHT TELL US? i.e how can we narrow down the search range?
- either we are in the rotated part or non-rotated part
- if our midpoint is less than nums[len(nums) - 1], then we are in sorted part
- if our midpoint is greater than nums[len(nums) - 1], then we know we are in the rotated part
=> since in the original array, the lefter elements should always be smaller than rightmost element (the highest element)

answer: return the minimum element of the nums array

edge case: 1 element

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l ) // 2
            if nums[mid] > nums[len(nums) - 1]:
                l = mid + 1

            elif nums[mid] < nums[len(nums) - 1]:
                if nums[mid] < minNum:
                    minNum = nums[mid]
                    r = mid - 1

            elif nums[mid] == nums[len(nums) - 1] and nums[mid] < minNum:
                minNum = nums[mid]
                r = mid - 1

        return  minNum

        