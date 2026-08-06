"""
problem notes:
- evaluating if a string is valid given condition constraints
- brackets must be opened and closed by the same type
- should be an even number of brackets in the string or else there's no way for it to be valid
- ultimate question: how do we check that the open brackets are closed in the correct order?  => what is that order?
    => open brackets should be closed last in the order that they are seen? i.e the first open bracket should be closed last if there's another open bracket next to it
    => if next bracket isn't an open bracket, it should be the correct closed bracket
    
=> these insights make me think stack => you want last in first out => adding a closing bracket to an open bracket is making it "out"
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # edge cases: empty stack, only open bracket, only close bracket


        mapping = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for char in s:
            if char in mapping: # this should check keys
                stack.append(char)
            else:
                if stack and mapping[stack[-1]] != char:
                    return False
                elif not stack:
                    return False
                stack.pop()
        if stack: # still stuff leftover in stack like unclosed open brackets
            return False

        return True
        