# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
singly linked list -> we can only move forward throughout the list and thru each change
=> while we can technically store all of O(n) in memory. that is extra spac complexity and we don't want that

- first element never changes position

what needs to be done?
- prev element needs to point to new element that will get inserted
- new inserted element needs to point to that prev's element.next
[2,4,6] would become 2 -> 6 and 6 -> point 4 so [2,6,4]

problem: you don't know the value that needs to get swapped once you get to the position where it needs to happen
=> this is because it starts at the opposite i.e right end of the list and move inwards
=> while the positions to be inserted start from left end and move inwards


possible solution: first iterate through head to find length of it, and then use some version of slow and fast pointer?
-> then you know the "indexs" of the linked list like each position that we use to index via pointer
-> my plan was then using a slow and fast pointer
=> where slow's next position is where the value needs to be inserted
=> fast is the pointer before the value that needs to be inserted so we can get that value + move the fast's next to point to the inserted value's original next
    => if the prev's next doesn't get updated something that isn't the inserted value, it will create a cycle and go back constantly. 
=> we find fast by doing n - 1 - slow pointer to find how far back we have to go
=> to get this value we need a for loop to keep on doing .next since technically don't know how many .next's it is

once slow and fast are one a part that's when we no longer do the swap 
=> why is that? since slow's next should be that value, if that where it should be then there's no swapping neeed. this end conition is like the "middle point"
ex. [2, 4] => [2,4]
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
- fast's next value should change to none or inserted value's origal next
- inserted value should now point to slow's OLD next
- need to remember slow's OLD next before you break any chains


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
------------------------------------------------------------
07/12 notes:
- SOLUTION NEEDS TO BE O(N) time and O(1) space
- not optimal though since we are re-iterating over the same node multiple times
=> to get the end values
- problem: the amount of how far back we have to go into the list to get the prev of the value to be inserted
=> is still dynamic, meaning we can't just do .next.next because "how much next" is constantly changing and keeps on getting less
=> makes it not O(n) but could be a temp solution for now

- what's end condition? when slow is greater than or equal to fast pointer
- our fast is currently being recalculated from the anchor every time.
=> new fast changes every iteration since the list is re-ordered every iteration


- need at least 3 elements to make a swap. 

POSSIBLE SOLTION:
- what if you can calculate the index of the last element to be swapped/inserted
- this way you have 2 pointers: 1 that manages the position's next where the value should be inserted
=>  and 1 that manages the prev before the value to be inserted
- each pointer should start and stop at the proper index where their combined range should be n
=> ex. 0 - 5 and 5 - 10
=> DOESN'T WORK OR IS HARD SINCE both sides are moving inwards but going in opposite directions i.e move left to right versus moving right to left
"""
"""
new solution after getting guidance and hints from google gemini
1) first get the length of the linked list
2) once you get length of list, calc midpoint
work: [2 -> 4 -> 6 -> None][10 -> 8 -> 6 ]
3) after the midpoint, the node should points backwards
work: must remember the previous node before you move forward so you can point back to it
work: stop once you node.next won't exist. or like you don't run the work inside.
work: prev might exist on the last element, but the actual pointer doesn't exist. 
4) save pointer to the start of that new list, or backwards in this case. 
5) every 2 nodes to get to the next "prev" before the insertion pooint
work: need every 2 since you have to increment pass the new value you just added

need sure to break connections in proper order
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # calc the length of the original list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        # O(n) time complexity
        
        # calculate the midpoint. should be the index
        mid_idx = length // 2
        # turn the original linked list into 2 separate halves. one pointing forward and one pointing backwards
        
        prev = head
        curr = head.next
        idx = 1
        while curr:
            # --- DEBUG PRINT BLOCK ---
            debug_ptr = curr  # Replace 'head' with whatever node you want to inspect
            visual_list = []
            while debug_ptr:
                visual_list.append(str(debug_ptr.val))
                debug_ptr = debug_ptr.next
            print("Current List State: " + " -> ".join(visual_list) + " -> None")
            # -------------------------

            print(prev.val, curr.val, idx)
            if idx > mid_idx:
                print("entered backwrds looop")
                # need to realign the elements so break the connection and reorder them backwards
                curr_future_next = curr.next
                if idx - 1 == mid_idx:
                    prev.next = None
                curr.next = prev
                prev = curr

                curr = curr_future_next
                #print("curr", curr.val)
            else:
                prev = curr
                curr = curr.next
            idx += 1
        # prev points to the start of the backwards list




        
        # now begin reordering of the list:
        backwards_ptr = prev
        forwards_ptr = head
        while forwards_ptr.val and backwards_ptr.next: # stop once they meet in the midpoint, no more to swap
            # save 2's next  to 4
            forwards_ptr_next = forwards_ptr.next
            # save 8's next to 6
            backwards_ptr_next = backwards_ptr.next
            # 2 -> 8
            forwards_ptr.next = backwards_ptr
            # 8 -> 4
            backwards_ptr.next = forwards_ptr_next
            # make forwards_ptr = 4
            forwards_ptr = forwards_ptr_next
            # make backwards_ptr = 6
            backwards_ptr = backwards_ptr_next
            #[2, 10, 4, 6, 8]