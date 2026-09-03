"""
requirements: returning the total number of substrings within s that are palindromes. 

what should the state hold?
- each state should return the total number of palindromes that can be made up to that index. i.e return dp[len(s) - 1] represents the number of palindromes of the whole string

how do you efficiently check if a substring is a palindrome? 
- since checking each substring in a string is O(n^2) and then checking if its a palindrome is O(n). -> we want to make it so were not constantly checking overlapping substrins if its a palindrome. 

how is it subproblems:
- the prefixs are overlapping should make it easier to check if each substring is a palindrome instead of O(n^3) total.


NEW INSIGHTS:
- state represents the number of substrings of that length? and you basically want the add the total number of palindromic substrings from each substring length to get your answer. 

currently, i'm not incrementing the number of palindromes. i'm just incrementing palindromes from possible every possible center point, so that increments a max of possible center point palindromes, which is not the same as possible substrings
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0

        def expand(left, right):
            l = left
            r = right
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        for i in range(len(s)):
            total_palindromes += expand(i, i)
            total_palindromes += expand(i, i + 1)
        return total_palindromes
        