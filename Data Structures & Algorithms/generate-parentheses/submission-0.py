"""
requirements:
- n determines the number of PAIRS of parentheses you can use. i.e n = 1 means 1 "()" or 1 "(" and 1 ")"
- definition of well formed parenthesis / well - formed parentheses string: 
=> all open parentheses must be closed i.e same number of "(" to ")"
=> when MUST they be closed? -> different whens lead to different strings TODO: nested, same level, or outside/separate
=> can't start with a ")" if there's no previous "("


constraints: 
base cases below:
- MUST use all n pairs. => how will you tell that you've used all n pairs, length of string should be double n since each parenthesis is 2 characters or len(2). 
=> or you can count once you've added N pairs of parethesis i.e count in increments of ( and )

solution ideas:
what are the different choices at each index of n: ... where an index represents a parentheses
- you can add the whole parentheses i.e "(" and ")"
- you can add just the "(" but when do you close the ")" later?
KEY INSIGHT: after you've used up all of the "(" i.e you've appended "(" a specific amount of the times with no ")", you MUST also add the leftover amount of ")" that need to close those open's. => this number depends on whether you are adding "()" or just "(" and promising to add ")" later
=> MAKES ME THINK WE NEED A STACK OR NEED TO KEEP TRACK OF HOW MANY ")" to add

Input: n = 2
 "(()) or "()()"


- use the current string as a temp_list and combine them using. join() then check len of it => optimization to be made so you aren't re-creating a new string every time. 
=> could make each "(" or ")" its own index in the temp_list so length of list just matches the n * 2 for appending so you aren't combining just to check.

edge case:
- appending () or ( when i = n - 1, has the same result like will result in duplicate.
- when do you handle the excluding case so it gets caught by backtrack
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr_path, open_count, closed_count):
            if len(curr_path) == 2 * n:
                ans.append("".join(curr_path))
                return
            # recurse on the 2 choices
            if open_count < n:
                curr_path.append("(")
                backtrack(curr_path, open_count + 1, closed_count)
                curr_path.pop()
            if closed_count < open_count:
                curr_path.append(")")
                backtrack(curr_path, open_count, closed_count + 1)
                curr_path.pop()

        backtrack([], 0, 0)
        return ans
        