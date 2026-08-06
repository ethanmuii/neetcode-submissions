"""
answer: want the length of LCS

LCS: increases by 1 each time in the sequence. the indexs don't have to be consequential  or incrementing
=> you can grab indexs in any order, just want the actual values to be incrementing

the fact the ANSWER says write an answer in O(n) time. it wants us to look at each element once to create LCS.
=> we can't randomly guess and check indexs so likely read from left to right
=> need a data structure that would allow us to track back to what we've seen

- insight: you know an element is the start of an LCS if the value before it exists in the array
=> problem you don't if the value exists until after you've seen it
- need a hashmap
=> what does it contain, what keys, what values






edge cases:
- 
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        if not nums:
            return 0
        for num in nums:
            unique.add(num)
        maxLength = 0
        for num in unique: # originally i was iterating through the array which considers duplicates, don't consider duplicates since that's work you already did lie considering if its an LCS or part of an LCS. 
            if (num - 1) not in unique:
                length = 1
                while (num + length) in unique:
                    length += 1
                maxLength = max(length, maxLength)
                
        return maxLength
