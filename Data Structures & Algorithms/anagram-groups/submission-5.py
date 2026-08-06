"""
answer = lists of (sub)lists = [ [], [], [] ]

anagram = same chars and same freq per char

edge cases: 
 - strs can only be 1 word
 - word can be 0 letters ex.

 GOAL: group the words into anagram sections
    - a word can belong to a max of one group

problem: 
- how do we manage each word's chars and their frequencies = python dict
- how do we efficiently check for a word being anagram of another word
    - could check length first? => that filters it down more, but doesn't necessarily fix time complexity a significant amount
- make sure we aren't creating duplicate group (same anagram as separate groups)


- brute force: make a python dict for each word, and then use 2 pointer or double for loop to check every comparison of anagram group
    - either joins existing anagram group, makes a new one (i.e not a part of one)



optimal sol: 
- one big hash map: key = a list of chars and their frequency | value = list of the words that have that char and that char frequency
- dicts cannot be used as a key in another dict => use tuple of tuples instead?


pattern:
- iterate over each word, make hash map of each word's char + freq
- convert it to a tuple 
- check if that tuple exists in the dict as a key:
    - does? => add that word to the list of words that have that char + freq i.e group of anagrams
    - doesn't => creates it own key in the hash map and its own anagram group

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        overall = {}
        # need to iterate over each word in list, 'i' indexs over each word
        for i in range(len(strs)):
            key = [0] * 26
            for j in range(len(strs[i])): # iterate over each letter and make hash map of word
                index = ord(strs[i][j]) - ord('a')
                key[index] += 1
            key = tuple(key)
            overall[key] = overall.get(key, []) + [strs[i]]


        # iterate over the overall dict and then append each value of a key into ans => list of sublists
        for val in list(overall.values()):
            ans.append(val)

        return ans



        