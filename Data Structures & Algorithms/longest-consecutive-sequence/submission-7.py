"""
elements do not have to be consecutive in the original array -> we can just grab elements from anywhere in the list to form the LCS.

can only read/use a value once for it to be O(n)

how can we remember what values we have seen or know values come ahead

need to remember the max LCS even if multiple CS can be formed
ignore duplicate values since we only use a value once

possible solution:
- add all items to a set
- iterate over the values:
=> a LCS can only start if the value - 1 does not exist in the set
=> if the value - 1 does exist in the set, it isn't the start of LCS but instead in one
=> if you find the start of the LCS, keep on iterating up?
=> don't do anything if the value is in the set, its how we keep it O(n). a value is only used once
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueSet = set()
        for num in nums:
            uniqueSet.add(num)
        maxLength = 0
        for num in uniqueSet:
            if num - 1 not in uniqueSet:
                length = 0
                currNum = num
                while currNum in uniqueSet:
                    length += 1
                    currNum += 1
                if length > maxLength:
                    maxLength = length

        return maxLength
                
