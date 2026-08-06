"""
REACTO

- Anagram = words with same characters, and for each character there is the same frequency of that char
- Think of like if you had a character box, can you use all of the characters in the box to make the same 2 words
- true if words are anagrams, false if NOT

- how do we optimally check and know the characters in the word, but also their frequency of char => hash map?
    - key = character, value - frequency

- A: iterate through each word, and append to the hash map. will need 2 separate for loops, and 2 hash maps

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        if s_map == t_map:
            return True

        return False
        