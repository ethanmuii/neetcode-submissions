"""
- returning a list of lists, and given a list of strings.
- each sublist should be words that are anagrams of one another
- anagram means each word has the same exact letters and the same freq per letter

for ideal time complexity, we need some way to remember past words + the anagram layout as we iterate through the list. 
=> this will allow us to create a new or add a word to an existing to group in O(1) time
=> key could be a list of letters and their freq and the value can be the  list of words that have that combination
=> this allows us to check if there is a previous added word that is anagram of this new word, or add this word to an existing group

for key, instead of using a key:value or a list, we should use a tuple. keys can only be immutable in python
=> simplest way to do this, is to realize that there are only 26 letters in a word. use ord(char) - ord('a') to find out the index position where 0 represents number of "a" 's .
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        groups = {} # key = tuple, value = [list of words]
        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1

            groups.setdefault(tuple(freq), []).append(word)
        for group in list(groups.values()):
            ans.append(group)
        return ans