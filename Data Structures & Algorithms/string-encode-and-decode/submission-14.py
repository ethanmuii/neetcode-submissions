"""
our encoding should allow us predictably tell the separate words in this bigger string
=> we need to tell which letters make up a word 
=> how do you tell whether a letter belongs to one word versus another
=> add a separator after each word
=> how do you know the separator is not a part of the word?
=> put the number of places/letters in the word with the separator.
=> how can you know the number doesn't make up the word => this is why we have a separator even if the number is like 10, how do you know whether its 10 or 1 and then 0 in the word. the seperator helps

=> how can you know the numbers + separator isn't in the word itself? 
=> PLACEMENT, if we place this combination before a WORD, we control this variable and know that this wasn't in the word since we appended or added it to the big string before adding the first word
=>  then we can predictably know when each word starts and how many letters are in it to stop before the next word

=> CONTROL YOUR ENVIRONMENT. When dealing with the unknown, can you make anything in your control or completely predictable or expected? by adding it before the unknown or after the unknown
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_list = []
        for word in strs:
            temp_list.append(str(len(word)))
            temp_list.append("#")
            temp_list.append(word)
        return "".join(temp_list)

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        length_list = []
        while index < len(s):
            if s[index] != '#':
                length_list.append(s[index])
                index += 1
            else: # you found the separator
                length = int("".join(length_list))
                print(length)
                ans.append(s[index + 1:index + 1 + length])
                length_list = []
                index = index + 1 + length
        return ans

