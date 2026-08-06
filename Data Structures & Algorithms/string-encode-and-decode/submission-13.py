"""
encoded string should include ways to tell when a string starts and ends
=> we are going to need this when we decode the BIG string into the list of strings again
=> use a separator to separate when strings start and end
=> however, how do you know if the separator is not a part of one of the words
=> include the length of the string? => can't be just length because runs into same case as seperator
=> length + separator? => works, but would only work and is easier to use if you put it in front
==> this is because we can make the assumption that the word is that many letters and begins after this seperator
==> if we put after the word itself, then its harder and takes more time to read in the words and create the word into a seperate string
    => since strings are immutable so have to re-create every time. 
    => and because we are reading the string first, you don't know if the number is a part of th string or the actual length of string
    => even if you do #numbers# => even this pattern could be a part of the word
    => also need sepeartor since number could be double digit.
    => need to put in the very front so when we try to extract the first word
    => we KNOW and can assume it won't be till after we read in that number + seperator
    => we created those conditions and KNOW IT HAS TO START WITH THAT before any words

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_list = []
        for word in strs:
            temp_list.append(str(len(word)))
            temp_list.append('#')
            temp_list.append(word)
        print("".join(temp_list))
        return "".join(temp_list)

    def decode(self, s: str) -> List[str]:
        idx = 0
        ans = []
        numbers = []
        while idx < len(s):
            if s[idx] != "#":
                numbers.append(s[idx])
                idx += 1
            else:
                length = int("".join(numbers))
                ans.append(s[idx + 1: idx + 1 + length])
                numbers = []
                idx += 1 + length
        return ans

