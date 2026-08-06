# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
what if we just made it easier by having a dummy pointer and a pointer in the dummy list
then have 2 pointers in list1 and list 2
increment them before we make the dummy pointer's next point to the smaller value
""" 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        new_list_ptr = dummy
        # if both nodes exist
        list1_ptr = list1
        list2_ptr = list2
        while list1_ptr and list2_ptr:
            if list1_ptr.val <= list2_ptr.val:
                new_list_ptr.next = list1_ptr
                list1_ptr = list1_ptr.next
                new_list_ptr = new_list_ptr.next
            elif list1_ptr.val > list2_ptr.val:
                new_list_ptr.next = list2_ptr
                list2_ptr = list2_ptr.next
                new_list_ptr = new_list_ptr.next
        # one of the lists doesn't exist so add it on to the rest of new list
        if list1_ptr:
            new_list_ptr.next = list1_ptr
        elif list2_ptr:
            new_list_ptr.next = list2_ptr

        return dummy.next