"""
- if something is rotated n times, that means the last 4 elements were rotated to the front
- can view like a circle
- want to return the INDEX of the target in the SORTED ARRAY, not original ascending order

- in the original array where everything is ascending, we can perform binary search since the array is predictable.
=> we know where to look based on how something compares

KEY INSIGHT: in a rotated sorted array, the behavior is still predictable based on comparisons
=> in a rotated sorted array, there are 2 sorted arrays within the big array
=> there is a pivot point where the array goes from ascending to descending
=> and that behavior is created from rotation happening in the array. 
=> technically no pivot point if the whole array is rotated because then it just stays in the original ascending order

- if we are past the pivot point, then we are in the original array
=> if we are before the pivot point, we are in the rotated part

QUESTION: how do we know which part we are in O(log n) time?
- the last element in the original array should be the max value
- so if our mid is less than or equal < to last element, we are in original part
- if our mid is greater than the last element, that means we are in the rotated part
=> because no element should greater than the last element if the last element is at the correct place. 

=> then our conditions on where to look left or right vary based on which part we are in
**** UNDERSTAND WHY EVERYTHING IN THIS BOX IS WRONG
 THIS WRONG BECAUSE IT TELL US WHERE OUR MIDPOINT IS, BUT NO WHERE OUR TARGET IS
 ULTIMATELY, WE WANT TO KNOW AREA OUR TARGET IS IN BECAUSE THATS'S WHAT TELL US WHERE TO LOOK
our midpoint can be greater than the end but less than target and still be on the right side
our midpoint can be greater than the end  but the target can still be less than the midpoint
****
you don't know where the PIVOT happens

how to find when the pivot occurs?
- when the element is greater than element after it. 
- once you find the pivot point that is how you know where to look
- inflection point occurs if element is greater than element after it
=> or if element is less than element before it
=> but how does midpoint tell you where to look for inflection, can you do binary search on it? 

*** AFTER LOOKING AT HINT 2, I HAD THE RIGHT ALGORITHM AND SOLUTION. I JUST DIDN'T KNOW HOW TO IMPLEMENT IT PROPERLY IN CODE. 
- I DON'T KNOW HOW TO PERFORM BINARY SEARCH TO FIND THE CUT

where idx = deflection point
one array = [0:deflection point]
one array = [deflection point: end of array]



07/13:
- you can't tell where the pivot is just by looking at the number at the end at the very beginning.
=> this would only tell the pivot if the numbers are incrementing at 1 and the list started at 1
=> cuz then this adds predictability because by looking at last element you know how many elements were rotated
=> however while elements were in ascending order, they AREN'T in consecutive sequence (incrementing by 1)

- to find the pivot in O(n) time, you can just loop through the list until the value is greater than next value.
=> if you get to the last element and you haven't found a condition, then no technical pivot and it was rotated n times. 
=> the list is basically the same as the original list

how can you find the pivot in O(log n) time?
- want to find the highest value you can get to that is higher than the last element
- if you find a higher value, move right there might be a higher value
if you find a lower value move left

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use b.s to find pivot point
        l = 0
        r = len(nums) - 1
        # find the deflection point
        maxPivotValue = -1001
        pivot = -1 # no pivot found, array is original, what should be the default value when there is no pivot
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
                currPivotValue = nums[mid]
                pivot = mid
                maxPivotValue = max(maxPivotValue, currPivotValue)
            elif nums[mid] <= nums[-1]:
                r = mid - 1
        # we now have 2 sorted lists: 0 to pivot, and pivot + 1 to end of list. 
        # what if there's no pivot? 
        if target >= nums[pivot + 1] and target <= nums[-1]:
            # search originally sorted part
            l = pivot + 1
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
        elif target >= nums[0] and target <= nums[pivot]:
            # search rotated part or fully rotated
            l = 0
            r = pivot
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
        return -1