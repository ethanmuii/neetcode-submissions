# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
depth: number of nodes from root node to farthest leaf node (not any leaf node)
- how can this problem be broken down into smaller subproblems with subroots?
- the depth of a root with no children is 1? 
- the depth of a root is the maximum depth between the depth of left child's depth and right child depth's depth + 1
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def recursion(root):
            # base case
            if not root:
                return 0
            left_depth = recursion(root.left)
            right_depth = recursion(root.right)
            return max(left_depth, right_depth) + 1



        ans = recursion(root)
        return ans