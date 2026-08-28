# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
requirements:
- return the head of the re-ordered list
- the values themselves are trivial. they could be anything (increasing, decreasing, etc). 
=> we care about actually re-ordering the INDEXS themselves.

constraints:
- must modify the list in place i.e move the nodes around. CANNOT create a new list or change values.
=> can only move the next pointer, and ideally should keep track of prev and future. 
=> can only move forward

why do we care about the indexs? 
- we are re-ordering the list where its like starting from the beginning and pulling from the back to insert. i.e 0, n-1, 1, n - 2, etc. => WE STOP THIS ACTION ONCE WE GET TO THE MIDDLE!! thus, the middle node of the original L.L should now be the last. or if its even, it should be the middle rounded up. 

possible ideas:
- iterate and create hashmap: key = index, value = Node. and then re-order them as you iterate through the list. stop once you get to the middle index. 
=> PROBLEM: would need to keep track of the node's prev like what is pointing to it? or does it not matter since its next gets updated to point to correct val. only thing is that we would have to make the last middle index point at nothing
[0, 1, 2, 3, 4, 5, 6] 0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3
[2,4,6,8] 2 -> 8 -> 4 -> 6, then 6 will point back to 4 and then we would have to make the middle's curr null.


edge cases:
- odd vs even number of nodes in L.L
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hashmap = {}
        curr = head
        index = 0
        while curr:
            hashmap.setdefault(index, curr)
            curr = curr.next
            index += 1
        print(hashmap)

        index = 0
        middle = len(hashmap) // 2
        curr = head
        tail = len(hashmap) - 1
        
        while index < middle:
            insert = hashmap[tail]
            future_curr = curr.next
            curr.next = insert
            insert.next = future_curr
            curr = future_curr
            index += 1
            tail -= 1
        
        curr.next = None

        return
        