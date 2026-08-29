"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
requirements:
- need to return a DEEP COPY OF THE LIST (i.e creating all of these new nodes brand new)
- values are not increasing (by 1). values are completely random. can't make any assumptions about the ordering of the values
- L.L of length n -> we do not know n and won't know it until we iterate through the original list.
- input comes in the format of [] where each [] in the list is a "Node", and in [x,y] x represents the value of the node while y represents the index of the node its pointing to for 'random' in the L.L (0-indexed) -> this is just VISUALLY, not the actual structural representation

constraints:
- Node can't be created until the 'random' and 'next' Node both exist (unless we create dummy Nodes that don't hold the correct value and ptrs are both None)

insights:
- None/Null does not need to be created so it has no dependencies i.e you can't point to a Node if the node it's pointing to doesn't exist. -> NOT THE CASE FOR NULL (regardless of random/next)
- since we need a deepy copy (and are returning head of copied linked list), we should be making the list on the side AS WE OR AFTER we iterate through the original list. 

edge cases:
- null is NOT required in at least one node in the L.L's random pointer (they can all point to concrete nodes)
- random ptr in the L.L must be between 0 and n - 1 or null.
- node values are not guaranteed to be unique so can't make the value itself a distinct differential -> only the INDEXS.
- no cycles allowed in the input list so next must continue moving forward till a node eventually points to null.
- cycles are allowed to be created if you followed a node's random and random can also point to the node itself i.e self cycle
- local list can be empty. return None should be right? 


solution insights:
- hashmap? key=index, value = the original list node?  -> PROBLEM: wouldn't help because can't just create a copy of that node unless random and next exist in the deepy copy. also values wouldn't be good enough to differentiate the difference between 2 nodes, its only the addresses themselves

how to figure out the node  to be created first? is there always a node or possible solution for this?
- no this is not possible because in a valid test case EXAMPLE 1: there is no node that starts with a node's next and random both existing. 

another solution insight:
- what if we use a stack and append each original list node to stack. they get popped out in rreverse order and that allows us to build the next connection properly. i.e 4 cannot exist until 5 exists, etc. 
=> deep list stores nodes in the hashmap
=> len(stack) is the amount of nodes in the list. 
PROBLEM: visually, the input shows the index of random, but the code only allows us to get the listNode address
==> what if we store a hashmap of each original list node addy and its index it shows up at. 
==> after we build the next connections, we can then build the random pointers BY...
===> for each node in the deep list specified by index, we access our local list at the same time iterating through it, using next, and then that local list gives us the INDEX of it's random pointer by checking the local L.L library and then we use that INDEX to grab the deep value copy at that index and make the curr deep copy's random pointer point to it 
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edge case:
        if not head:
            return None

        deep_map = {} # key = index, value = Optional[Node]
        stack = [] # used to create the next connections for deepy copy
        local_map = {}# key = original L.L node addy, value = index (of where it is in the original list)

        # append to stack and create original list addy to index mapping
        curr = head
        index = 0
        while curr:
            stack.append(curr)
            local_map.setdefault(curr, index)
            index += 1
            curr = curr.next
    
        # now create the deep list mapping with next pointers
        index = len(stack) - 1 # will get decremented and represents the key of deep copy list. 0 to n - 1
        future = None # represents where the popped node's next should point to 
        while stack:
            curr = stack.pop()
            deep_map.setdefault(index, Node(curr.val, future, None))
            future = deep_map[index]
            index -= 1
        # now need to create the random pointers
        local_curr = head
        for value in reversed(deep_map.values()):
            random_node = local_curr.random
            if random_node != None:
                random_index = local_map[random_node]
                value.random = deep_map[random_index]
            local_curr = local_curr.next # need to update local_curr so it stays up to date with our iteration of deep list
            #print(value.val, value.next, value.random)
        return deep_map[0]

