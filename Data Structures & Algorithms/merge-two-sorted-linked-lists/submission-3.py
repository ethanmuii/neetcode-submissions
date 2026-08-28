# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
requirements:
- each list is already sorted
- list(s) could be empty
- modify the lists in place i.e don't create brand new nodes which takes extra space.

constraints:
- because list(s) can be empty, it is best to have a dummy node and just make it point to the head/start of the list
- what are the different cases you get from comparing the nodes between 2 lists?
1) one list is empty/done -> just add the rest of the other list
2) both lists are empty/done so we can return (this is the end condition)
3) both lists have a node and this leads to subcases
3.1) list1's node is >= list 2's node. P.S the equal symbol could go both ways, it doesn't matter.
3.2) list 1's node is < list 2's node.

-- now what happens at each comparison....?
=> node to get inserted needs to know the prev so prev can now point to it, and the node to get inserted can now point to its next. need to make sure we increment the curr pointers in both lists to go until the end

edge cases:
- for simplicity, let's say we are always merging list1 into list2. 
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, None)
        prev = dummy
        prev.next = list2
        # initialize 2 iterators
        curr1 = list1
        curr2 = list2

        while curr1 or curr2: # as long as there's more to see in either list execute.
            if curr1:
                print(curr1.val)
            if curr2:
                print(curr2.val)
            print(prev.val)
            print("------")
            if curr1 and not curr2: # add the rest of curr1 to our sorted list
                prev.next = curr1
                curr1 = None
            elif not curr1 and curr2: # add the rest of curr2 to our sorted list
                prev.next = curr2
                curr2 = None

            else: #curr1 and curr2
                if curr1.val < curr2.val:
                    prev.next = curr1
                    future_curr1 = curr1.next
                    curr1.next = curr2
                    prev = curr1
                    curr1 = future_curr1
                else: #curr1 >= curr2
                    prev = curr2
                    curr2 = curr2.next



        # handles base edge case where both lists don't exist. 
        return dummy.next
