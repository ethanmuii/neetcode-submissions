"""
REACTO

- Want to check if there are any duplicates (2+) in an array.
- How preform this check using least space complexity? and time complexity?
- Return true if THERE ARE DUPLICATES / False if NO DUPLICATES

- An array with no duplicates is just an array with ALL unique elements

- Double For Loop is brute force
- Set to check for duplicates => If set length is not equal to array length => There are duplicates

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for num in nums:
            ans.add(num)

        if len(ans) != len(nums):
            return True

        return False
        