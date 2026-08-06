"""
each anagram group is a sublist and each sublist is appended to a final ans list

anagrams has the same chars and same frequency per char as another word
how do you plan on recognizing past char and frequency of a word after you passed it.

hash map: key=array of 26 letters, value = list of all words that have that frequency
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for word in strs:
            freq = [0] * 26 # frequency map
            for char in word:
                diff = ord(char) - ord('a')
                freq[diff] += 1
            
            hashmap.setdefault(tuple(freq), []).append(word)

        for val in list(hashmap.values()):
            ans.append(val)

        return ans

