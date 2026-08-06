# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
singly linked list -> we can only move forward throughout the list and thru each change
=> while we can technically store all of O(n) in memory. that is extra spac complexity and we don't want that

- even though we know the exected values, need to reorder the nodes themslves
- understand the pattern and that can help you understand pointers to use
- first element never changes position
- technically don't know the length of the list at runtime

what needs to be done?
- prev element needs to point to new element that will get inserted
- new inserted element needs to point to that prev's element.next
[2,4,6] would become 2 -> 6 and 6 -> point 4 so [2,6,4]

problem: you don't the value that needs to get swapped once you get to the position where it needs to happen
=> this is because it starts at the opposite i.e right end of the list and move inwards
=> while the positions to be inserted start from left end and move inwards

SOLUTION NEEDS TO BE O(N) time and O(1) space

could you swap it greedily? => no that's not possible 

possible solution: first iterate through head to find length of it, and then use some version of slow and fast pointer?
-> then you know the "indexs" of the linked list like each position that we use to index via pointer
-> my plan was then using a slow and fast pointer
=> where slow's next position is where the value needs to be implemented
=> fast is the value that gets inserted
=> we find fast by doing n - 1 - slow pointer to find how far back we have to go
=> to get this value we need a for loop to keep on doing .next since technically don't know how many .next's it is

once slow and fast are one a part that's when we no longer do the swap 
=> why is that? since slow's next should be that value, if that should be then there's no swapping. it's like we reached the boundary but as we go towards middle
ex. [2, 4] => [2,4]

CHANGE OF PLANS: instead of fast_ptr equaling the value to be inserted, it needs to be the value that POINTS to the value to be inserted
=> this is because we need to change that value's next value to point to NONE
=> until that value is either reassigned and re-inserted everywhere or it needs to stay NONE
=> if we don't then it creates a cycle. 
--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------
LETS TRY THIS SOLUTION OUT, not optimal though since we are re-iterating over the same node multiple times
=> to get the end values

# edge case (we know length of L.L is at least 1)
- length 1: return the list as normal
- length 2: return the list as normal. don't need to do any swapping
- length > 2: this where our process should be generalized to. starting with length 3.

list of what needs to happen: 
- slow's next changes to inserted value
- fast's next value should change to none
- inserted value should now point to slow's OLD next
- need to remember slow's OLD next before you break any chains

problem: the amount of how far back we have to go into the list to get the prev of the value to be inserted
=> is still dynamic, meaning we can't just do .next.next because "how much next" is constantly changing and keeps on getting less
=> makes it not O(n) but could be a temp solution for now

[2, 10, 4, 6, 8] length = 5
for next iteration, slow increments by 2 and fast stays the same
slow = 4
fast = 6
1) save 4's next which is 6
2) save 6's next next which is None
3) save fast's next which is 8
4) assign 4's NEW NEXT to 8
5) assign 6's new NEXT to None
6) assign 8's next to 6
[2, 10, 4, 8, 6, None]

smallest ex. [2, 4, 6]
slow = 0
fast = n - 2 where n is length 
1) save 2's next which is 4
2) save 4's next next which is None
3) save fast's (4) next which is 6
4) assign 2's NEW next to 6
5) assign 4's NEW NEXT to None
6) assign 6 to slow's next (4)
* still need to increment and decrement fast ptr

- what's end condition? when slow is greater than or equal to fast pointer
- our fast needs to be recalculated from the anchor every time.
=> new fast changes every iteration since the list is re-ordered every iteration
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # calc the length
        anchor = head # always right since the head never changes
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        # beginning calculations
        slow = 0
        fast = length - 2
        slow_ptr = head
        fast_ptr = head
        while slow < fast: 
            # need to recalc fast
            fast_ptr = head
            for i in range(length - 2):
                fast_ptr = fast_ptr.next

            slow_old_next = slow_ptr.next
            fast_new_next = fast_ptr.next.next
            insert = fast_ptr.next
            slow_ptr.next = insert
            insert.next = slow_old_next
            fast_ptr.next = fast_new_next
            slow += 2
            slow_ptr = slow_ptr.next.next


        