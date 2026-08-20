"""
requirements:
- string that contains only "(", ")", "*"
- return boolean if string meets contraints and condition

constraints:
- must be the same amount of "(" and ")" in the string i.e no "((" or "))"
- ( must come before ) so no ")("
- key detail: "*" is a wild card, it can be anything whether ")" or "(" or nothing if you want?

insight:
- reminds me of that problem where you use a stack to keep track of how many closing brackets you need when you see an open parenthesis

- what determines when you want to use a "*" and how you want to use it?
=> the difference between the open bracket and close brackets cannot differ by more than the number of '*'. this is because '*' can be used as a filler brackets or nothing if not needed (i.e ( and ) count are equal)

=> double check that this algo works regardless of the other you see stuff, since you aren't tracking when you see the ( or ) or *
- if the difference between * + open brackets is ever less than closing bracket, then its not a valid string since a closing bracket came first i.e )(* or )*(, these are both invalid. closing brackets always need to be less than open bracket so when you do add the closing bracket, its even

but... this would be valid ((*) or (*) or (*)) or ()*) would be valid too since ()(). i.e closing bracket must always be less than open + *

make sure you double check when you are incrementing counts and when you are checking


edge case: s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
- i think its because we are only checking the difference between open and close count at the end, not at every iteration, no because you don't know how many close parenthesis there may be in the future i.e ((*) would return false prematurely

can't just use a star whenever the open and close count differ by more than 1 because you don't know if you will see more ")" in the future and in that case you shouldn't have used the star as closing bracket, it should just be kept as empty. 

NEW IDEA: pre-compute the number open, close and stars you got? -> should make it easier to kknow what you got
- need to iterate across string and check whether you fix this current state because open - close could be greater than star and it could be false. 
- placement of the stars matter

# when do you have to use a star? -> when there's too many opening brackets and not enough closing brackets left
# or when there's too many closing brackets in the future and not enough open brackets
# it can be nothing when they are equal

# decrement every time you process one??

- more just need to precompute the amount of closing brackets in the future and then keep track of ur current star count, that's when you know if you have one avaliable and when it is avaliable

GOT HINTS: made google gemini prompt my thinking to develop the intuition
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []
        for index, char in enumerate(s):
            if char == "(":
                open_stack.append(index)
            elif char == ")":
                if open_stack:
                    open_stack.pop() # i.e found a matching close parenthesis.
                elif star_stack:
                    star_stack.pop() # has to use a star
                else:
                    return False # both empty so nothing to cover
            else:
                star_stack.append(index)
        
        # handle leftover open parentheses
        while open_stack:
            lastest_open = open_stack.pop()
            # is there a star that exists for the lastest ( to use?
            if star_stack:
                lastest_star = star_stack.pop()
                # is this star later enough for the lastest open?
                if lastest_open > lastest_star:
                    return False
            else: # not enough stars exist
                return False
        # finished matching all leftover open parentheses so
        return True
        