"""
need to turn the list of strings into one string where you can later tell where each string starts and ends in that big string
- need separators
- could use how many letters are in each word, how do you know if those numbers are not a part of that original word. 
- need numbers + separator => still how do you know that isn't included in the word
-> make the assumption: when you create the encoded string you always start with the number + separator so you know IT HAS to be the length of the word

- how do you tell the difference between [] and [""], empty list versus empty string in a list, len(1). 
- create a encoded elements in a list first before you try to make the string. prevents you from doing string editing and creating a new string each time

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_list = []
        for word in strs:
            temp_list.append(str(len(word)))
            temp_list.append('#')
            temp_list.append(word)
        return "".join(temp_list)
    def decode(self, s: str) -> List[str]:
        num = []
        ans = []
        idx = 0
        while idx < len(s):
            if s[idx] == '#':
                length = int("".join(num))
                num = []
                start = idx + 1
                end = idx + length + 1 # range index is exclusive
                ans.append(s[start:end])
                idx = end

            else: # its a num
                num.append(s[idx])
                idx += 1

        return ans
            


