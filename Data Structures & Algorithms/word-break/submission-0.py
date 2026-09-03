"""
requirements:
- only lowercase letters
- string has at least one char, never EMPTY. 
- returning a BOOLEAN
- can check if a substring/partition is VALID if it is in wordDict in O(n) time by just doing 'in wordDict' -> similiar to checking if something is a palindrome. except this time we need to check randomly possibly?

constraints:
- can re-use words in wordDict.
- don't have to use every word avaliable in wordDict.
=> you can think of it as the string just needs to be able to be partitioned and consumed completely by the words in wordDict

edge cases:
- what if a word in wordDict is a prefix of another word in wordDict i.e "race" and "racecar". -> when would you want to use "race" versus "racecar" -> should you always partition the biggest chunk off possible i.e if you partition 'racecar' off the string s, then do that. don't just partition 'race' off since car or whatever maybe leftover might not be able to handle the 'car' prefix. 


insights:
- at a high level, what if you check each possible substring in s, and if the substring is in wordDict -> it is valid. Then you just need to check if there's a combination of partitions (i.e chosen substrings in s) that consumes all the indexs i.e len(s) like 0 to len(s), not just summing the lengths themselves but making sure it covers all indexs. 


"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True          # empty prefix

        for i in range(1, n + 1):
            dp[i] = False
            for j in range(i):
                if dp[j]: 
                # only want to continue off possible states that left off with valid partitions, so then our last piece starting from j to i, should be a valid partition if possible
                    piece = s[j:i]           # candidate last partition
                    if piece in wordDict:
                        dp[i] = True

        return dp[n]
            