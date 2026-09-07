# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
requirements:
- given a BST
- wan to return the value of the K-TH smallest element 1-indexed

constraints:
- BST allows us to know where to look to find smaller elements or bigger elements.
- 1 indexed basically means the k = 1 means smallest element, opposed to k = 0 being the smallest element
- node can have a max of 2 children, but you don't know the down-stream of how many nodes there are downstream, and then also how many children nodes they have as well.

- since the tree being a BST means every node to the left of that node is smaller, then its that subroot value, and then every node to the right of it is bigger. -> WE CAN MAKE THAT ASSUMPTION

- in english, we want to travese nodes where for each node we go left left left until we can't, and then we process that node, and THEN we go right right right. 
- this will ensure that we check the smallest possible node and keep on going left to find the smallest possible node until it doesn't exist, and then the next smallest node would be that subroot before we check its right subtree. -> this is how we follow the sorting invariant of how the values we will be. 

=> NOW to find the k-th smallest node. our answer isn't the right answer until we've popped from the stack k-times. then our answer is that one. for example, if we keep on adding nodes until we go left left left until we can't no more, then when we eventually can't add any more left nodes, then that popped node would be our k-th smalles tnode. 


=> how can you implement this via a stack? i kinda know how to do it via recursion


edge case:
- root can't be empty so guaranteed at least 1 root? k is never more than the number of nodes in tree



already did it the PQ way where you add everything to a priority queue, and then keep on popping to find the k-th smallest element where it is a min queue. 
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pops_used = 0
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # you are far left so then process the current node or the parent of None
            curr = stack.pop()
            pops_used += 1
            if pops_used == k:
                return curr.val
            curr = curr.right



        