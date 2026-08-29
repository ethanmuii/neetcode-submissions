# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
already solved it by doing the 2 pass solution, trying to figure out instict behind 2 pointers

requirements:
- given n, remove the nth- node from the END of the list, not start.
- still need to return the HEAD of the list after edit, even if that means editing the head.
- n is 1-indexed from the back

constraints:
- don't know the length of the linked list, just the index that we are suppsoed to remove.
- everything depends on how many nodes there are in the L.L, is there a way to iterate when you don't know how many nodes are in the L.L. -> that affects which node is considered the n-th node from the end of the list. 
- its a single L.L too so you can only go forward?

solution insight:
- because you are trying to remove the nth node from the END of the list, what if you have 2 pointers which should be n nodes apart so when the further pointer is at None, the second pointer should be at the node to remove.

-> problem is you need to update the linking so technically you would want the prev of the pointer to be removed so you can make the prev point the deleted node's next so its removed. 

edge case:
- list has 1 node and remove the head so should return None
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy

        # set up the further pointer (ptr2)
        index = 0
        ptr2 = prev
        while index != n + 1:
            ptr2 = ptr2.next
            index += 1

        ptr1 = prev
        while ptr2:
            ptr2 = ptr2.next
            ptr1 = ptr1.next

        # once ptr2 reaches the None, ptr1 should be at the prev of the node that needs to be deleted
        deleted_node = ptr1.next
        ptr1.next = deleted_node.next


        return dummy.next
        