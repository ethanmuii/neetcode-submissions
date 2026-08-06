"""
REACTO
- order output doesns't matter
- anagram = same char, and same frequency per char
- need to return a list of lists. => each sublist are words that are anagrams of each other

- words are not anagrams if hashmap are of different length, check char content of hashmap, and then value frequency of hashmap

- gonna be at least O(n) where n is the length of strs. => Need to iterate through every word in the array and check if its an anagram of other words

- do you wanna store a new hashmap for each word? or reuse the rexisting hash map across all words
- also how do you manage the different sublists as we are iterating through strs

- every word in strs, is either an anagram of another word we've already seen, or it starts a new sublist (i.e it has no CURRENT anagram pairs)

- I feel like it will be hard to manage separate sublists that each represent anagram groups as we are iterating through strs.
    - it feels like multi tasking or juggling multiple balls
    - instead i think its better to find all words that are in the same anagram group, add them all to a sublist, and then add that sublist to the bigger list, and then RE-ITERATE
- do we need to keep the original strs in-tact? or can we edit the list as we iterate/go?

APPROACH #1:
- Choose a word (likely first one). Create its hash map (i.e anagram checker). Iterate through the words in strs, and check if its an anagram of the our original chosen word, if it is, add to a sublist.
- Delete the first chosen word, and then delete the word that matched, continue and iterate through rest of list, and repeat if there are anagrams with our orignal chosen word.
- then add that sublist to a bigger list called ans. 
- Now iterate through the "inline" edited original strs (which should have less words now given that we found some anagrams), and repeat the whole process as above
- END CONDITION: until strs is empty, then return
- EDGE CASE: every word is not an anagram of any other word. => no anagram groups at all


What is time and space complexity of approach #1?

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        for i in range(len(strs)):
            if not strs:
                return ans
            # create the sublist
            sublist = []
            # create the hash map of the first anagram check
            hmap = dict()
            for char in strs[0]:
                hmap[char] = hmap.get(char, 0) + 1
            sublist.append(strs[0])
            print("Word that needs to be matched for anagram group:", strs[0])
            strs.pop(0)
            print("Content of strs after we start a new anagram group:", strs)
            # indices that matched and need to get removed before next anagram group
            remove_indices = []
            # now iterate through edited-strs list and see if there are any matching pairs
            for i in range(0, len(strs)):
                cmap = dict()
                print("This is the current word we are checking for possible match:", strs[i])
                for char in strs[i]:
                    cmap[char] = cmap.get(char, 0) + 1
                # they are anagrams
                if hmap == cmap:
                    sublist.append(strs[i]) # add it to anagram group sublist
                    print("This is the matching word:", strs[i])
                    remove_indices.append(i)

            print("This is what strs looks like before we remove matching indices:", strs)
            print("The indices that will need to get removed", remove_indices)

            # gone through all possible checks
            ans.append(sublist)
            for index in reversed(remove_indices):
                print("removing this word from strs:", strs[index])
                strs.pop(index)
            print("This is the content after the anagram group is done:", strs)
        
        return ans

                
                    
                



        