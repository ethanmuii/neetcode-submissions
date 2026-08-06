# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
notes: 
- similiar to max depth except the root node doesn't have to be one of the ending nodes
- path cannot include same node twice so you can't just find longest half path and * 2
- path does not have to pass through the root, but it SHOULD pass through a subroot

- key insight: the longest path should be depth/height of left subtree + right subtree. Not + 1 since we are doing number of edges and not nuumber of nodes. in longest path

key details
- cannot know the longest path through a node until you know the left and right subtree height
=> the longest path through that node left + right
- BUT we aren't returning that. we should be returning the info that helps the higher node, and that's the MAX(left, right) since whatever side will end up being the longest path for the parent node to use as one of its sides
- need to keep a global max. we need all this information so likely need to do a nested function

current problem, we aren't incrementing the length of each subtree to calc the longest path
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def helper(root):
            nonlocal max_length
            # base case
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            path = left + right
            if path > max_length:
                max_length = path
            return max(left, right) + 1

        helper(root)
        return max_length
