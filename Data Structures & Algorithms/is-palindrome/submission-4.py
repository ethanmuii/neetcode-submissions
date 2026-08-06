"""
- ignore all nonalphanumeric characters and case-insensitive (i.e conver tto lowercase if char)
- reads same forward and backward = symmetrical
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 # left index
        r = len(s) - 1 # end index
        string = s.lower() # makes it easier to ignore case sensitive
        while l < r:
            # cases: both are nonalpha numeric, l is only, r is only
            if not string[l].isalnum():
                l += 1
            elif not string[r].isalnum():
                r -= 1
            else:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1

        return True