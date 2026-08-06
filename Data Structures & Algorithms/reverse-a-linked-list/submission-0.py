# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
answer: returning the node (head) that starts the reversed list

edge cases:
- empty linked list
- 1 element in the linked list

because we are basically breaking connections and reassigning them, we need a third hand or a dummy node for the edge cases

brute force: create a brand new list and as you iterate forward in the original, you are assigning next pointers backwards

THINGS YOU NEED TO DO AT EACH NODE:
- make its next value point to prev
- increment curr to the next node
- store a reference to the future list so you can incrment curr
- need to store prev for the next iteration
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            future = curr.next
            curr.next = prev
            prev = curr 
            curr = future

        return prev # should end at the new list
        


        