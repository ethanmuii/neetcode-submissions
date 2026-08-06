"""
overall goal: we want to return the length of longest substring that contains only one character
- can be duplicates, but duplicates must be same of 1 character
- since we want the MAX length, k should always be the current most freq character in our consecutive string
=> this is because this will take the least amount of replacements allowing us to maximize the length
- can view k as like free-bees => the more k's you have the longer you can make the string and the less k's you have to use the better

- longest substring length should reset to 0 when we run out of k's and the character differs from the current char with most freq.
=> i.e we can't replace the letter to continue the substring since were out

Where should the string start from then? 
- it shouldn't start from where you found a non-replacable character because then
=> you miss possible longest substrings that start somewhere in between
=> your left boundary window and that non-replaceable character where one of the
=> chars in the window could be the same as the non-replaceable character
=> and continue the longest window. 

need a hashmap to store key = letter, and value = freq of that char
as you go keep track of the mostfreq char. 
TRICK: don't need to update or decrement the value of highest freq char because
=> the only way a substring will be longer is if there is another char that 
=> creates a more freq char within a substring where length - most freq char
=> is still less than k. 

=> update the counts in the hashmap, but not the value mostFreq since thats a max value we need to keep
=> cuz a string needs a larger value to make a longer substring. 
=> global optimal variable

edge case: k = 0

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        l = 0
        r = 0
        hashmap = {}
        maxFreq = 0
        currLength = 0
        while r < len(s):
            hashmap[s[r]] = hashmap.setdefault(s[r], 0) + 1
            maxFreq = max(maxFreq, hashmap[s[r]])
            currLength += 1
            # if true, we need to shorten the window so move left inwards
            while currLength - maxFreq > k:
                hashmap[s[l]] -= 1
                currLength -= 1
                l += 1
            maxLength = max(maxLength, currLength)
            r += 1

        return maxLength
        