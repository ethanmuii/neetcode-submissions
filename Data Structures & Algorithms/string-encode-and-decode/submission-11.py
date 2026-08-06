"""
encode: need to turn a list of strings into one string
- this string needs to be made where it can be read and turned back into the original list of strings
- algorithm: how can we know when a string starts and ends? within that big string
    - this algorithm will be used by our decoder to split up the strings

=> include a separator in between each string => how do you know if that separator is not included the string itself
=> include the length of the string => how do you know that number is not in the string 
= include number + separator

=> where to include it? => in the front, NOT the back. having it in the front allows us to control what we read right away in the very beginning
=> if was in the back, there would be no way to know if a string ended with that separator + number
=> separator is needed for double digits



decode: does the work of decoding the new string back into the original list of strings
- just follow the algorithm and the assumptions you created from encoding 

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        if not strs:
            return ""
        for string in strs:
            ans.append(str(len(string)))
            ans.append("#")
            ans.append(string)
    
        return "".join(ans) # efficient way instead of making new strings. strings are immutable

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []
        ans = []
        # read the number until hashtag 
        index = 0
        size = []
        while index != len(s):
            if s[index] != '#': # number
                size.append(s[index])
                index += 1
            else: # it a hash tag so we know its end of string
                start = index + 1
                sizeNum = int("".join(size))
                end = start + sizeNum
                ans.append(s[start:end])
                # move index and clear size
                index = end
                size = []
        return ans