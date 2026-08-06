# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- whatever traversal method SHOULD work as long as you do the same for both.
- this is because they should traverse the same nodes IN ORDER. 
- could do a BFS in order traversal. 

- values are easy to check, but structure can be checked by doing the same traversal

- BFS iterative queue traversal, in order
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque()
        q_queue = deque()
        # append the roots
        p_queue.append(p)
        q_queue.append(q)
        # grab the next node up in FIFO
        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            # do work and check the non-happy paths
            if not(p_node and q_node and p_node.val == q_node.val) and not(not p_node and not q_node):
                return False
            # append vals to p_queue and q_queue
            if p_node:
                p_queue.append(p_node.left)
                p_queue.append(p_node.right)
            if q_node:
                q_queue.append(q_node.left)
                q_queue.append(q_node.right)

        return True
