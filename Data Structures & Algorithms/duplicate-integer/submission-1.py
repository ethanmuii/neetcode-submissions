"""
- iterate over the array = check condition in any value in array
- condition (duplicate value) = must remember what you've seen => set or dictionary
    - key = number, value = count of that number
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
            if numFreq[num] != 1:
                return True
        return False

        