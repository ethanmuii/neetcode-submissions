# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
solution is probs best O(n)
you iterate through linked list to find length
then iterate again through the linkd list with index to remove that nth node
if n = 1, just return the head's next. -> could also do it dummy node way

for every node that gets removed, make sure the prev points to that element's next and that node will get removed cuz there's no way to get to that node even if there is still a pointer to it

remember that its the N'th last element from END OF THE LIST, 
so position that needs to get removed is  
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
            

        if n == length:
            
            return head.next
        else:
            index = 0
            remove_index = length - n
            curr = head
            while curr and curr.next:
                if index == remove_index - 1:
                    print(index)
                    print(remove_index)
                    node_removed = curr.next
                    curr_future_next = node_removed.next
                    curr.next = curr_future_next
                index += 1
                curr = curr.next
        return head
