# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        elif not list2 or (not list1 and not list2):
            return list1
        else: # list1 and list2 both exist
            curr1 = list1
            curr2 = list2
            prev = ListNode(-101, curr2)
            anchor = prev
            # cases: both lists have nodes, only one does, or neither
            while curr1 and curr2:
                
            # 1) compare list1 pointer and list2 pointer if not None
                if curr1 and curr2 and (curr1.val >= prev.val and curr1.val <= curr2.val):
                    curr1next = curr1.next # red 2
                    # before you change this, need to point the value that was pointing to curr2 to you
                    prev.next = curr1 # dummy node points to red 1
                    curr1.next = curr2 # blue 1
                    prev = curr1 # should always hold prev to urr2
                    curr1 = curr1next # red 2
                elif curr1 and curr2 and curr1.val > curr2.val:
                    if not curr2.next:
                        curr2.next = curr1 # adding curr1 to curr2
                        curr1 = None
                    # need to move the prev pointer to curr2 before you change curr2
                    prev = curr2
                    curr2 = curr2.next

            # 2) if list1 pointer is None, do nothing everything else is adde donto list2

            # #) if list2 pointer is None, need to add rest of list1 to end of list2

        return anchor.next
            
