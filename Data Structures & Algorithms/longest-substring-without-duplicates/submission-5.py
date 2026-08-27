"""
requirements:
- must be a substring i.e no gaps, can't pick n choose characters can only choose when to start and end it. must keep everything in between. 

constraints:
- substring cannot have duplicate characters

insights:
- you can extend a substring only when it doesn't contain any characters in the current substring
- when you run into a duplicate character, have to start substring from a different place (move left pointer of window inwards) => DOES NOT NECESSARILY MEAN START WHERE YOU FOUND THE DUPLICATE CHARACTER
=> a valid edge case could be starting with the next letter
- stop iterating when your right pointer has reached the end. moving the left pointer inwards can only make the max_length smaller. 
- since we need to track every char's index, keep it in a hash map where key: char and value = index and update it when you remove the original and add duplicate. update max_length whenever you have to change starting points or after every iteration?


edge case:
- s = "zxyzabc", if you start from where you found the duplicate character max is 4 when in reality it should be 6 for "xyzabc"
- s = "zxyabyz", if you just move the left pointer inwards by 1 when you encounter the second y, the substring will still contain. -> you want to start the new left pointer at the original of the duplicated character's index + 1.
- s doesn't exist so just return 0?
- s="abba", if you always move l to duplicate's original char index + 1, in this case the stringw ould be "bba". need to keep it the max between them?
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        tracker = {}
        if not s:
            return 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in tracker:
                tracker.setdefault(s[r], r)
            else: # duplicate char
                l = max(tracker[s[r]] + 1, l)
                tracker[s[r]] = r
            r += 1
            max_length = max(max_length, r - l)
        
        return max_length

