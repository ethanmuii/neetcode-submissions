"""
answer: return a list of lists
- each list are words that are anagrams of each other

edge cases: 
- empty string which is a string of length 0. 
- [] not possible, but [""] is. 

=> hash map: key: tuple that holds each char and their frequency | value = list of words that have that char and frequency i.e anagram group 
- tuples are ordered so before you make it a key, you would need to sort 
=> this is because when you are making the dict of a word (key: letter, value: freq), depending on when you see the letters in the word, it affects insertion into python dict
=> thus affects ordering when you conver this dict to a tuple, and this affects the actual overall dict that holds anagram groups

=> sorting is O(n log n)
=> iterating through the list of strs is O(n) where n is len(strs) and then sorting per word is O(n^2 log n)

can you do a solution without sorting? 
instead of hashmap for chars and their frequency, use an array of length 26. and you ue ascii values
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for word in strs: 
            freq = [0] * 26
            for char in word: 
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            hashmap[key] = hashmap.get(key, []) + [word]

        for sublist in list(hashmap.values()):
            ans.append(sublist)
        
        return ans
        