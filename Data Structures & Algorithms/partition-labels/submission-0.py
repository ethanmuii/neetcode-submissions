"""
requirements:
- basically finding subsets in the given string s
- not returning the substrings themselves but the LENGTH of each substring in a list
=> returning a list of ints. 
- want the MAX number of substrings given constraints

constraints:
- can't pick n choose letters/indexs. ==> substrings must be formed by consecutive strings
edge cases:
- each UNIQUE letter can only appear in at most ONE substring (wouldn't it be at least 1? or is there a scenario where a letter doesn't appear at all) 
=> regardless of whether there is duplicate letters from different indexs (can still only appear in one substring -> describes constraint on partition, can't drop letters
- the partition must be a full split on the string: every index from 0 to n - 1 must be in a substring, pieces have to be contiguous. letter can only appear in one piece. 


insights:
- likely need a set to track used unique letters
- ans array to contain length of each substring
- since a letter can only be in one substring, the curr substring we are operating on must keep on extending its length/boundary until it captures ALL of its duplicates.
=> same thing applies for any letter you see along the way -> must also meet this condition and must keep extending. 

- how do you know when to stop a substring like you know you've seen all of the occurrences?
=> if you could keep track of each unique letter in a substring i.e a set, then check if the current letter is in any or which set. if its in the lastest set , then extend that curr substring, if its not, the set/substring that has that letter boundary must be updated to include that letter and any substrings that were after or now a part of that substring. 
- problem: that is a set per substring and we have to delete it as soon a previous substring boundary gets expanded. 

hash map??

NEW IDEA:
- iterate through string s and to create a freq map of each unique letter, key: letter, value: freq of that letter
- ur current substring needs to keep on incrementing until its freq for each unique letter in substring equals each char's freq in the global string map. -> AS SOON AS IT DOES, then we can stop. and create a new substring 


the constraint of the problem isn't the freq of the letter, but more where does this char occur last gloibally like what index
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        hashmap = {}
        # create this map of last index for each letter
        for index, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = index
            elif index > hashmap[char]:
                hashmap[char] = index
        print(hashmap)
        start_index = 0
        goalpost = hashmap[s[0]]
        for index, char in enumerate(s):
            # check if goalpost needs to get extended
            if hashmap[char] > goalpost:
                goalpost = hashmap[char]

            # create new substring if curr_index = goalpost
            if index == goalpost:
                ans.append(1 + index - start_index)
                start_index = 1 + index


        return ans

