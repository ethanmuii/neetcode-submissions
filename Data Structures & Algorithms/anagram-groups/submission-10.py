"""
need to put all words that share same char and freq per char in sublists
final answer should contain all the sublists

need to efficiently remember the char and freq per char for every word as you see them
so it becomes O(n^2)

hashmap: key = tuple where the count represents the freq for each char
26 letters so can do ord(letter) - ord('a') to create the mapping
can be an array at first, but need to make it a tuple for key since keys can only be immutable
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            hashmap.setdefault(tuple(freq), []).append(word)

        # need to return the ans
        for sublist in list(hashmap.values()):
            ans.append(sublist)
        return ans
