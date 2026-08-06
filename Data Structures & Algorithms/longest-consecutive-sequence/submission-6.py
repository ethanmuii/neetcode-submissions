"""
O(n) - can only see and do work on an element once
ANSWER: length of longest consecutive sequence, don't really care about what elements are in 
consecuive sequence: every element increments by 1 each time. 
=> you grab the elements in any order, but it must increment by 1 each time

=> since we want the LONGEST sequence, if the element - 1 exists in the array, that should be the start of the list
since only those elements can be the start of the list, we should only increment from that element to see the longest possible element that can be created with that list. 

=> double while loop, but its O(n) ammortized
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add all numbers to a set
        uniqueNums = set()
        maxLength = 0
        for num in nums:
            uniqueNums.add(num)
        index = 0
        while index < len(nums):
            if (nums[index] - 1) not in uniqueNums:
                length = 0
                number = nums[index]
                while number in uniqueNums:
                    length += 1
                    number += 1
                maxLength = max(length, maxLength)
            index += 1
        return maxLength