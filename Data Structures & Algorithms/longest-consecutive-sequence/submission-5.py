"""
longest consecutive sequence:
- sequence must be incrementing by 1 with each element
- can pick and grab elements out of order, do not have to be consecutive index wise, only value wise
- want the length not the actual values that make up the length

- O(n) solution time means no nested work

problem statement:
- might be duplicates values in nums but technically only need to use it once in a sequence and CAN ONLY USE IT ONCE
=> can basically ignore duplicates => i.e set??
=> add all elements to a set

how do we know when the beginning of a sequence should occur?
=> if number - 1 is not in the set. this is because if number - 1 in the set, then THAT'S WHEN the sequence should start, not at number. 
=> once we find the start of sequence, keep on incrementing until the next number is not in the set. 
=> and save that maxLength

=> time complexity would be O(n) still, just multiple separate loops, not nested
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(num)

        for num in nums: 
            currLength = 0
            if num - 1 not in uniqueNums: # then this is a start of possible list
                number = num
                while number in uniqueNums:
                    currLength += 1
                    number += 1
                maxLength = max(maxLength, currLength)

        return maxLength