"""
- n = len(nums) - 1)
- every value in the array is from 1 to n
- just because the value CAN be in that, doesn't mean it is technically in the array
=> ex 1. technically  4 can be in the array as well, but it isn't.
=> every integer can appear at most once => i.e 1 or 0 times
=> and one integer is repeated. 

brute force:
- use a set() and check for the number that causes duplicate 
=> O(n) space, O(n) time
- sort the array and then check for repeated numbers now that they are adjacent to each other
=> O(n log n) time and O(1) space
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniqueNumbers = set()
        for num in nums:
            if num in uniqueNumbers:
                return num
            else:
                uniqueNumbers.add(num)
                