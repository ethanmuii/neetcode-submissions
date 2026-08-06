"""
answer: returning the index of where TARGET is 

with rotated sorted arrays, there is 2 sorted parts within one big array
=> we should know where to look for target based on how it compares to midpoint and boundaries?
=> in a normal sorted array, target > midpoint -> look right
=> target < midpoint -> look left
=> target == midpoint -> return that index

- problem: you don't know if target is in rotated part or sorted part 
=> since depending on where the pivot is target could be both be less than highest element in rotated part AND greater than lowest element in original
=> thus, finding out where the pivot is exactly doesn't help you

- what if you split up into 4 cases considering how midpoint compares to target but also how it compares to boundaries
- if you are in the rotated part


EDGE CASE:
nums [3, 5, 1] target = 3
nums = [3, 4, 5, 6, 1] target = 1
=> it ruins the fact that ur target could be less than the midpoint, and your midpoint tells u whether you are in sorted or rotated part
=> but you could have to look either left or right. not predictable

=> midpoint can't tell you where you are but if you use the target? 

AFTER READING HINT 2: 
1) first find the deflection point (cut) -> basically trying to find rightmost pointer for left cut and leftmost pointer for right cut
=> its found when nums[left] <= nums[right] b/c if nums[left] > nums[right] we are still breaking the sorted ascending rule of a normal array
=> this means we are still not in correct order as one left is in rotated part and right side is original sorted part

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first find inflection cut
        l = 0
        r = len(nums) - 1
        minVal = float('inf')
        minIndex = 0
        while l <= r: 
            mid = l + (r - l) // 2
            if nums[mid] < nums[len(nums) - 1]:
                if nums[mid] < minVal:
                    minVal = nums[mid]
                    minIndex = mid
                r = mid - 1
            elif nums[mid] > nums[len(nums) - 1]:
                l = mid + 1

            elif nums[mid] == nums[len(nums) - 1] and nums[mid] < minVal: # only 1 element edge case
                minVal = nums[mid]
                minIndex = mid
                r = mid - 1
        deflect_p = minIndex # you have your deflection point, cut represents minVal in WHOLEL ARRAY
        # preform binary search on 2 separate cuts
        #1st cut = 0 to cut - 1, 2nd cut cut to len(nums) - 1
        print(deflect_p)

        l = 0
        r = deflect_p - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        l = deflect_p
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return -1

