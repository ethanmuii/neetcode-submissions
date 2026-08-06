# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
for depth, we want the number of nodes in the LONGEST PATH
- can't necessarily determine if the tree is balanaced or not.

- to get the depth of each path, we want to do DFS. BFS would get us level by level, but not each vertical path. 
to get the max path, we want to have a variable called max. 

- in this case, each node's longest path depends on the longest path of its children
=> since a path is considered from a root(could be any node for a given subtree)
=> down to a leaf node in its subtree

=> to explicitely get the LONGEST one, at each node, we want to take the maximum between its left and subtree
=> that's ultimately what will create the longest path with that node. 

=> also post-order traversal since DFS since each root node depends on the values of its left and right nodes. 


** DFS, post-order traversal, recursion, save the result of left and right subtree
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # base case
            return 0 
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # the longest path of that node is considered the max between left and right subtree and then +1 for the actual node itself
        return max(left_depth, right_depth) + 1
        