# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1 = 1st smallest value (THE smallest value in whole tree)
2 = 2nd smallest value in the whole tree

- a binary search tree allowes us to figure out the type of values to be seen depending on whether we go left or right.
- with a binary search tree, we can't predict what will have nodes or null children and how many nodes are even in the tree

how can we split it into cases?
- there is a total of 3 nodes in the tree, one node with 2 children. it is techncially the 2nd smallest element b/c if you go left you get even smaller, if you right you get even bigger. 

simple solution: traverse the tree in any way you want and append every node to priority queue. depending on k, pop from the priority queue and that value is your k-th smallest element if the priority queue is a min queue
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_queue = []
        def helper(root):
            nonlocal min_queue
            if not root:
                return
            heapq.heappush(min_queue, root.val)
            helper(root.left)
            helper(root.right)
            return
        helper(root)
        for _ in range(k):
            value = heapq.heappop(min_queue)
        return value