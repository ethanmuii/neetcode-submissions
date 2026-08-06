"""
answer: array/list
- default value should be 0 in the result array
- increment it each time you search for a warmer future temp or could just do differences between indices and keep 0 as default if you never do that calculaiton


problem notes:
- brute force: O(n^2) to scan the array for a future warmer temp for each temp in temperatures
=> bad because your checking duplicates and re-scanning


- move left to right
- in a sense, you want the CLOSEST warmer temperature, so '>' 

a stack would allow you to keep track of all past seen values without having to re-iterate a new loop

add a temperature to a stack and then increment the pointer, if that value is > greater than stack value then pop it. -> repeat this process until condition is not true or stack is empty
then add this new element to stack

this is because the top of stack is always <= than the bottom of stack so any future value getting checked for top of the stack will for sure work for anything any value that also works for bottom of stack
=> it wont be blocking
=> there's a case where the top of stack is < than bottom of stack and chance future value works for top, but still not for bottom


HOW DO WE GET THE INDICES? 
- add it as a tuple? to get the difference between the indices 

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # edge case: temperatues is length 1
        if len(temperatures) == 1:
            return [0]


        result = [0] * len(temperatures) # intialize default value to 0
        stack = [] # first val is temp, next value is index. can be tuple since they don't change
        pointer = 1
        stack.append((0, temperatures[0]))
        while pointer != len(temperatures):
            while stack and stack[-1][1] < temperatures[pointer]:
                result[stack[-1][0]] = pointer - stack[-1][0]
                stack.pop()
            stack.append((pointer, temperatures[pointer]))
            pointer += 1


        return result
        