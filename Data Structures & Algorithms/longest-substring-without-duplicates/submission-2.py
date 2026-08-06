"""
answer: return a number i.e length of the substring

condition-based window size
- keep on adding to length until you run into a duplicate character
- shrink window by moving left pointer if you run into duplicate
- to make tracking duplicates easy, use set() for O(1) lookup


FRESH START:
window = length of substring
maxValue = length of longest substring i.e longest window
set should be the current characters in the window 

the big question: when you end up seeing a duplicate character what happens?
- you have keep on closing the window (i.e moving left pointer) until that duplicate value we found is NOT in the window (i.e set())
=> after that happens, then you can add this duplicate value in since its no longer a duplicate
=> this is because a new substring can only begin after that original/first value is no longer in the substring
=> even if there are unique characters before it, they cannot be counted towards LONGEST SUBSTRING
=> since it wouldn't be consecutive

=> end condition  is still when r < len(s). cuz once r is equal/past that, there is no more chars to create a longer string
"""

# THIS CURRENT SOLUTION WAS JUST TRACKING NUMBER OF DISTINCT CHARACTERS. WE NEED TO TRACK CONSECUTIVE SUBSTRINGS
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        window = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in window: # if you found a duplicate, need to keep on incrementing left until that value is gone
                while s[r] in window:
                    print("still in window", s[r], r, s[l], l)
                    window.remove(s[l])
                    l += 1

            window.add(s[r])
            r += 1
            maxLength = max(maxLength, r - l)


        return maxLength
