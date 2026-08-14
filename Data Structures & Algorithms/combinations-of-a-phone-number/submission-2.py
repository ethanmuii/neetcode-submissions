"""
requirements:
- return a list of strings where each string represents a letter combination that could be made from the given digits. THE ORDER of when the digits appear in the digit string is important because it affects the order which matters. dg is different from gd, and that's the difference between 34 versus 43. 
- 1 is not included
- each digit (2 through 9) represents 3 possible characters. 
- number of possible combinations is n^3 where 3 represents the choices for that digit. and n represents the number of digits.

constraints:
- must use every DIGIT (and convert it to a choice) i.e each string will be len(digits long) -> base case
- each element in curr_path will represent a letter option of that digit at digit[i] and append to answer when len(curr_path) == len(digits)
- DO NOT NEED TO START FROM DIFFERENT LOCATIONS like DO NOT START FROM DIFFERENT INDEXS in the digit string, we always start from digits[0]. => we are only choosing what combination we start with and move the index foward. we don't do a for loop through every index in digit, instead only through its options. 

edge case: 
- duplicates cannot occur since we are always moving forward? i.e 334 can only create ddg once like 334 will occur from the first 3's branch and it won't occur again in second 3 cuz we can't make the first 3 a d. 
- empty string base case or digits doesn't exist
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        # create mapping  of each digit mapping to specific characters
        char_map = { '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        def backtrack(start, curr_path):
            if not digits or digits == "":
                return
            print(len(curr_path), len(digits), curr_path)
            if len(curr_path) == len(digits):
                print("are we in here")
                s = "".join(curr_path)
                ans.append("".join(curr_path)[:])
                print(ans)
                return
            # go through all the options and backtrack
            for option in char_map[digits[start]]:
                curr_path.append(option)
                print(curr_path)
                backtrack(start + 1, curr_path)
                curr_path.pop()




        backtrack(0, [])
        return ans