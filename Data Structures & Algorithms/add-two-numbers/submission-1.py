# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
requirements:
- two non-empty L.L where each node in the L.L helps form a non-negative integer.
- digits are stored in reverse order -> think stack and then pop to get the actual number. 

- will need to combine the digits together as strings but then return it as ints. 

constraints:
- just space complexity of converting the numbers to strings to combine and then ints to perform operations on it
- instead of using a stack to reverse the order, just use a string and then reverse the string
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = []
        curr = l1
        while curr:
            str1.append(str(curr.val))
            curr = curr.next
        reverse = "".join(str1)
        reverse = reverse[::-1]
        value1 = int(reverse)
        
        str2 = []
        curr = l2
        while curr:
            str2.append(str(curr.val))
            curr = curr.next

        reverse = "".join(str2)
        reverse = reverse[::-1]
        value2 = int(reverse)

        combined = str(value1 + value2)
        dummy = ListNode(-1, None)
        future = None
        for char in combined:
            curr = ListNode(int(char), future)
            future = curr
        dummy.next = future
        return future