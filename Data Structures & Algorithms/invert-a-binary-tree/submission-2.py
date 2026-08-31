# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
what does inverting mean? -> flip its left and right children. this should happen for each node and its children. 

we can iterate through the root and its children, performing the operation via stack. 

edge case:
- nodes have 0 children i.e leaf nodes
- node has 1 children on either left/right
- node has both children so can switch both.
- gonna go with BFS. doesnt necessarily have to be level by level
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if not curr: # don't want to call .left and .right on a non-existant Node
                continue

            left = curr.left
            right = curr.right
            curr.right = left
            curr.left = right
            queue.append(left)
            queue.append(right)

        return root