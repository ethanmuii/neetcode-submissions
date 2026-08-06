"""
ans format: returning an int

problem notes:
- "division between integers always truncates toward zero" => use '//'
- an operator can only have a max of 2 operands before it, whether that is numbers in the token list
=> or thats a value added after a previous calculation in the expression

=> this assumption allows us to assume our stack can only be 2. operator + 2 operands OR operator + previous expression value + operand
=> we want a stack because we are working backwards. once we run into an operator, then we want to look 
=> to see what the operands is used on the operator and pop



I HAD IT ALL WRONG. the stack handles ordering for reverse polish notation. for each operator, it uses 2 operands
=> all operands are stored on stack, and then popped 2 at a time when an operator appears
=> you are working inside to outside or inner parenthesis first form left to right


*** the ras
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        ans = 0
        operators = {"+", "-", "*", "/"}
        for op in tokens:
            if op in operators: # do calc work
                val1 = stack.pop()
                val2 = stack.pop()
                if op == "+":
                    newVal = val1 + val2
                elif op == "-":
                    newVal = val2 - val1
                elif op =="*":
                    newVal = val1 * val2
                elif op == "/": # number you see first in stack is always what you are dividing by
                    newVal = int(val2 / val1)
                stack.append(newVal)
                print(stack[-1])
            elif op not in operators:
                stack.append(int(op))

        ans = stack.pop() # final value left in stack 
        return ans
        