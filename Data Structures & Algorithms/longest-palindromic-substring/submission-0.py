"""
requirements:
- want the MAX LENGTH of substring that is palindrome. -> not returning the length
=> it wants us to return the actual substring itself.
=> we will likely need to keep track of the indices i.e the start index of substring and end index of substring -> this will allow us to slice and get the substring path itself

- state needs to hold at least 2 indices. without it, how can we capture the substring itself? 
=> or you can make it 2d DP

constraints:
- checking if a substring is a palindrome takes at least O(n) unless you can some how convert it to be O(1) look up if this substring is a palindrome
=> O(n) because it takes 2 pointer to iterate and check that everything is equal. 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_l = 0
        max_r = 0
        def expand(left, right):
            l = left
            r = right
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                l -= 1
                r += 1
            return length, l + 1, r

        for i in range(len(s)):
            curr_length, curr_l, curr_r = expand(i, i)
            if i == 1:
                print(curr_length, curr_l, curr_r)
            if curr_length > max_length:
                max_length = curr_length
                max_l = curr_l
                max_r = curr_r
            curr_length, curr_l, curr_r = expand(i, i + 1)
            if i == 1:
                print(curr_length, curr_l, curr_r)
            if curr_length > max_length:
                max_length = curr_length
                max_l = curr_l
                max_r = curr_r
        return s[max_l:max_r]
