"""
- don't want duplicate characters in the substring: use a set or dict?
- substring is a contiguous sequence of characters so like indexes should be adjacent to each other

- every time you see a character add it to set, 
- sliding window solution should be O(n) meaning you read a character from the array and do something with it only once
- as soon as you see a duplicate, the next possible substring cannot start until that character is no longer in the substring
=> whether that means deleting multiple duplicates but shouldn't be possible in this case
=> or deleting non-duplicates (unique) characters that come before the original character

- if you skip and start from where the duplicate was found then you miss possible substrings that could be made after the original but before the duplicate
""" 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        uniqueChars = set()
        l = 0
        r = 0
        currLength = 0
        while r < len(s):
            if s[r] not in uniqueChars:
                currLength += 1
                uniqueChars.add(s[r])
                maxLength = max(maxLength, currLength)
            elif s[r] in uniqueChars:
                while s[r] in uniqueChars:
                    uniqueChars.remove(s[l])
                    currLength -= 1
                    l += 1
                # then add the character back into the set again since we deleting all the elements up to the original duplicate element
                uniqueChars.add(s[r])
                currLength += 1
            r += 1

        return maxLength

