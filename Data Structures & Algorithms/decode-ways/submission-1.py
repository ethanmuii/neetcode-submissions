"""
requirements:
- only upper case letters. 
- possile valid number encodings are 1 - 26 and 'A' to 'Z'. 
- you are GIVEN a string of NUMBERS, not LETTERS. -> can only partition the numbers where the partitioned number equals a valid letter. 

constraints:
- leading zeroes are not allowed in any partitioned number of a message. 
- the partitioned number must also be within 1 - 26. i.e 27 is not allowed, if a letter can be encoded to '27', the only possible options are '2' and '7' not combined. 
- zeroes must be included after a valid number (i.e 1 - 9). it can never be a leading zero in any case or by itself. 


edge case: 
- the string cannot be decoded i.e "01" -> cannot be mapped to a letter. 
- s of length 1 meaning only 1-9
- "1012" can only be "10" "1" "2", "10", "12". it can never be "1" "0" "1" "2" since 0 cannot be by itself. 
- what about "112" -> "1""1""2", "11""2", "1""12" -> those are the only partitions
- "100" is a valid test case even though it is 0. 

insights:
- for a given string, get the possible partitions it can be where each sublist is a valid combination represented in a list of string format i.e ["1", "1", "2"]
=> WAIT THE NUMBER OF PARTITIONS IS BASICALLY THE NUMBER OF WAYS TO DECODE IT. -> you don't even have to decode it to a letter. 


how can be state represented?
- the index represents the number of ways to decode up to/including that index. 
- if there is adjacent 0's then it will always be 0. 
- a single zero is ok as long as it is after a 2 or 1.
- base case, the moment you see adjacent 0's, leading zeroes, or >3 + a zero is an instant 0 ways to decode since you can't decode it at all. 

how do subproblems relate?
- number of ways to decode "12" is number of ways to decode "1" + number of ways to decode "2"? or would it be number of ways to decode "12"
- number of ways to decode "1012" is "1"  = 1, "10" = 1, "101" = 1 + 1, "1012" = 2 + 1?
- visually, it can be mapped to a decision tree, just trying to understand how to view it as subproblems?
=> does each number add another way to decode it? except for base cases? => nope "11223" disproves it. 
- must use every letter in the string, can't skip any

lets try "11223":
"1" = 1 way to decode = "1"
"11" = 2 ways to decode = "11", "1""1"
"112" = 3 ways to decode = "11""2", "1""12", "1""1""2"
"1122" = 5 ways to decode = "1"1""2"2", "11""2"2", "11""22", "1""1""22", "1""12""2"

- do you even need DP? does the number of valid partitions of string s just give you the number of ways to decode it? 
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0] * (len(s) + 1)
        memo[0] = 1
        if s[0] == "0":
            memo[1] = 0
        else:
            memo[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                memo[i] += memo[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                memo[i] += memo[i-2]
        return memo[len(s)]
        