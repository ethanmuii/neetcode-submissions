class Solution:
    # were supposed to think of these 2 functions AS ONE PROBLEM, instead of individually
    # need to encode the list of strings to one string, so this one string can be back decoded?
    # originally i thought it meant it wanted the list of strings concatenate into one string, but no it wants ENCODING 
    def encode(self, strs: List[str]) -> str:
        # currently encoding code as 3 letters when should be 4
        encoding = ''
        for word in strs:
            encoding = encoding + str(len(word)) + '#' + word
            # this adds the length of the world and then a delimiter
            # so our decoder will know how much letters are in word
            # need deliminter for strings more than 10
        return encoding

    def decode(self, s: str) -> List[str]:
        '''
        how should we ENCODE it so when we DECODE it, we can tell when a word starts ends
        input is our ENCODED word

        1) first read the number
        2) then the expected delimiter
        3) then comes the word that gets added to solution

        - how should i break up the iterations?
        - ex. 4#neet4#code4#love3#you
        - BRUTE FORCE FOR NOW

        - plan: read the string until you hit delimiter, once you hit delimiter, you know the number
        - then iterate/"read" that many spaces based on the number you found
        - add those chars/string to solution array
        - end: when you reach the end of the string

        4#neet4#code4#love3#you

        '''
        solution = []
        curr_idx = 0
        while curr_idx != len(s): # signifies the end
            num = ''
            while s[curr_idx] != '#':
                print(s[curr_idx])
                num += s[curr_idx]
                curr_idx += 1
            temp_word = ''
            # now read the word to add
            for char in s[curr_idx + 1:curr_idx + int(num) + 1]:
                temp_word += char
            curr_idx = curr_idx + 1 + int(num)
            solution.append(temp_word)

        return solution



# special cases:
# - strings that aren't letters
# - strings that are more than 10 digits long
