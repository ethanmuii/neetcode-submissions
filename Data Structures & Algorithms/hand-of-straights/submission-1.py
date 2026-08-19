"""
requirements:
- groupsize is always less than or equal to hand length

constraints:
- groups is ultimatly len(hand) / group_size
- the numbers must be consecutively increasing by 1 if mentally sorted. 
- true or false based on whether you can do this

brute force: simulate this whole process and then return true or false whether you can.

insights:
- duplicate numbers must be in separate groups. If the freq of a number in hand is > group_size, its always false since a duplicate being in the same group would mean not consecutively increasing
- how do you know if there's a gap in group that's greater than 1? sort the array!!!
=> only the start of a group can be whatever number, but more the group to be valid it must be at least group_size - 1 numbers to follow up in increasing consecutive order

- only want a number to be the start if the previous number doesn't exist in the array.
=>



edge cases:
- hand could only have one number and its always true
- what if group size does divide the len(hand) evenly? - auto false
- only want a number to be the start if the previous number doesn't exist in the array.
=> but what if the number is the start of the array in one group, but not the other.
- how do you tell which group the number belongs to?
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base case
        if len(hand) % groupSize > 0:
            return False
        
        hand.sort()
        freq = {}
        max_groups = len(hand) / groupSize
        num_groups = 0
        # make freq map
        for i in range(len(hand)):
            freq[hand[i]] = freq.get(hand[i], 0) + 1


        # now form the groups
        for card in hand:
            if freq[card] > 0:
                for i in range(groupSize):
                    if card + i not in freq or freq[card + i] == 0:
                        return False
                    freq[card + i] = freq.get(card + i, 0) - 1
        return True