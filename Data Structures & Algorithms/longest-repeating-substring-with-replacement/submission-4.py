"""
requirements:
- string only contains uppercase letters
- can replace a max of K characters -> do we actually have to replace or just mentally?. K is wildcard, can be anything. 
 
constraints:
- can replace a MAX of k characters. 
- length of substring can only contain 1 distinct character. (after necessary replacements)
- substring so it must be continious

insights:
- when do you need to use k if you have it? -> if character is different from the current distinct char in substring. 
- what happens if you have used up all of k and you run into another different char? -> need to go to the earliest indexed different char and start from there + 1
- which character should be the distinct character (that you don't use K) on? -> the most freq character found in the curr substring. 

*Now, how do you keep track of all these cases as you iterate across substring. 
- keep track of highest char that has highest freq and update if it ever changes. 
- difference between highest freq of char and current substring length cannot differ by more than k.
- and if it does, you gotta keep on moving left pointer until it goes back to that condition. 
=> but then when do you check max_length?, only on valid conditions?
edge cases:
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        hashmap = {} # key = char, value = freq
        l = 0
        r = 0
        max_freq = 0
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_freq = max(max_freq, hashmap[s[r]])
            while (r - l + 1) - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

        