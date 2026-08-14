"""
requirements: 
- palindrome: substring reads the same forwards and backwards
- list of lists where each list is a LIST of palindromes that when combine form s. 

constraints:
- can split slice string "s" to create substrings that are palindrome
=> CANNOT just pick n choose letters in any order since its not a list, but a string
=> meaning you can only grab from a range of letters and they must be in the specific order from the start to the end. i.e consecutive
=> What are the valid partitions of the string s where each substring is PALINDROMIC. i.e all substrings from the partition are substrings


comes down 2 problems
- how to iterate over all the different types of partition(s) i.e similiar to inserting an element at every place in the list but partition before the whole s and after the whole s are considered the same
- how are you checking if a substring is a palindrome?
=> stop the branch as soon as a substring in the partition branch is invalid, no point in partitioning the rest if this specific partition already created an invalid choice (i.e non valid choice)

solution ideas:
- helper function to check if palindrome:  use 2 pointer method? most efficient method?
=> could either take in substring itself or just range of index i.e start and end (exclusive) and then slice the actual string itself. 

- need a backtrack function to partition at every possible position. i.e similiar to the possible valid parentheses
=> every possible valid sublist MUST include every letter i.e our index must get to the end!!!!
=> how and when, and where you partition is up to you as long as you use every letter.
=> if a partition in a branch (before we got to the final index) produced an invalid palindromic, stop continuing along that path and backtrack. 
=> need to keep track of curr substrings in this partition branch?

INSIGHT: all the possible space of partitions is determined whether at each n - 1 between characters to CUT or NOT CUT. 
- cutting at or after an index means including it. like cut at 0 means include 'a', and 'ab'

edge cases (thinking through partitions):
- a, a, b
- aa, b
- a, ab
- aab (no cuts is also possible)

- add in checking for is_palindrome last!
- im currently not updating the end counter properly when it backtracks
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # final variables
        ans = []

        # helper function to check if valid palindrome
        def is_palindrome(substring):
            l = 0
            r = len(substring) - 1
            while l <= r:
                if substring[l] != substring[r]:
                    return False
                l += 1
                r -= 1
            return True


        def backtrack(start, curr_list):
            if start == len(s):
                print(start, curr_list)
                ans.append(curr_list[:])
                return
            print(curr_list)
            for end in range(start, len(s)):
                piece = s[start:end+1]
                if not is_palindrome(piece):
                    continue
                curr_list.append(piece)
                backtrack(end + 1, curr_list)
                curr_list.pop()
        backtrack(0, [])
        return ans
        