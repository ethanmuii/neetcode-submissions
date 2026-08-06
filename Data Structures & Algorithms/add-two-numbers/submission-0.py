# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
- both lists are guaranteed to have at least 1 number
- numbers are represented and stored in reverse order in the linked list 
=> i.e 1 i the last digit of the number. 
- no leading zeroes in the number, meaning a number cannot end with a 0.
=> unless the last element (0)'s next value is None

- return the sum of the 2 numbers as a L.L, meaning you also have to return it in reverse order as well

brute force:
- have 2 lists one each for list. iterate through each list and store the numbers in list
- combine the numbers by converting them to int's. 
- sum them, then turn it into a string, and iterate it backwards and make it into L.L



# backwards reading reminds me of a stack

edge cases:
- lists can have different numbers
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        # iterate over list1
        curr = l1
        while curr:
            list1.append(str(curr.val))
            curr = curr.next
        # iterate over list2
        curr = l2
        while curr:
            list2.append(str(curr.val))
            curr = curr.next
        list1.reverse()
        list2.reverse()
        num1 = int("".join(list1))
        num2 = int("".join(list2))
        print(num1)
        print(num2)
        total = num1 + num2
        print(total)
        # turn the total into linked list
        dummy = ListNode(-1)
        curr = dummy
        str_total = str(total)
        print(str_total)
        print(reversed(str_total))
        for char in reversed(str_total):
            print(char)
            curr.next = ListNode(int(char), None)
            curr = curr.next
    
        return dummy.next
