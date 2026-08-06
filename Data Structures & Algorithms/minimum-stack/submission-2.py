"""
constraints: O(1) time => technically means you can use other methods of the class in each other since they shoud all run O(1)

how to keep track of minVal in O(1) time?
- we can track minVal as we add it
- however, we also need to be able to remove a value:
    - minVal is the value we removed: need to update minVal to next minimumVal in our group of numbers
    => brute force would be O(n) to loop through all current stack and find the minimum
    - minVal is not the value we removed => minVal stays the same


    - could use another stack or just storing a tuple in the original stack where the first value is the value that was added, and second value is the previous minValue before it. 
    => make sure you pop from both lists so they always have the same amount of elements and their indexs will align then. 
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')
        self.backtracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.backtracker.append(self.minVal)
        if val < self.minVal:
            self.minVal = val
        return

    def pop(self) -> None:
        if self.top() == self.minVal:
            self.minVal = self.backtracker[-1]
        self.stack.pop()
        self.backtracker.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
