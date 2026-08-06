"""
default = false
condition  true

do the 2 strings meet the condition?
    - order of characters does not matter
    - does string contain the exact same characters? character itself and frequency?


MUST: track character itself and frequency of it 
    - key = character, value = frequency of it
    - preform it for each string, then check if hash maps equal 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        
        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        if s_chars == t_chars:
            return True

        return False