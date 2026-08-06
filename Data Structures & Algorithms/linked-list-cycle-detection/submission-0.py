# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
index determines where the cycle begins again like which node it loops back to
index = -1, no cycle and the tail node just ends like a normal LL

problem is singly linked list

brute force: could be to use a set() and add address of  Node to it, and then check if this node addy already in set, that's how you tell you visited it twice
=> this is O(n) space complexity though

can we do it in O(1) space complexity?

thinking back to circles, you know it is a cycle if one car, one thing catches up to another thing

use fast and slow pointers. if fast pointer eventually catches up or equals slow pointer which it should eventually meet at some point if there's a loop then yeah. loop

if fast pointer reaches end and never equals slow pointer, then its false
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
        