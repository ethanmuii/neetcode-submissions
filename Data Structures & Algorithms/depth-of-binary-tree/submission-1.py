# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
goal: need to return max depth i.e longest path from root node to farthest leaf node
depth = top down
height = bottom up

base case:
nullptr node has zero depth
subcase: the depth of a node can be defined as the longest subtree path (right or left) + 1 (for the actual node itself)

- recursion or a stack would work since you the lower/farther down nodes affect the higher cases
- breadth search is almost always top down
- this has to be bottom up

- DFS and post order traversal, can't do/know the work for a node until you do it for its subcases
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        