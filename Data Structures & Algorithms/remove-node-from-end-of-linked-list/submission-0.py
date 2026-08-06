# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
given an integer, remove the nth node FROM THE END OF LIST, not start.
returning its head => head stays the same unless length = 1 and n = 1 or n = length of the original list
=> use dummy node because might be removing the first node

brute force solution, iterate through the original list to find length of it

and then do length - n to find the index of the node to remove => but remember need keep connections
=> so want end at the prev value of the node to be removed
=> length - n - 1

need to account for edge cases:
[dummy, 1, 2, 3, 4]
[0,     1, 2, 3, 4]
since we are starting from dummy for the removal, it would just length - n

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        # calc the length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        prev_ptr = dummy
        # iterate through the dummy + original list to get to node before the value to be removed
        for i in range(length - n):
            prev_ptr = prev_ptr.next
        deleted_node = prev_ptr.next
        prev_ptr_new_next = prev_ptr.next.next
        # break connections
        prev_ptr.next = prev_ptr_new_next
        deleted_node.next = None

        return dummy.next