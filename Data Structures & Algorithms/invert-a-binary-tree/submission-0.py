# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
what does it mean to invert?
-> left and right nodes are swapped
=> can't just switch the values because if you just switch the values then the whole thing isn't inverted, just the first layer
=> ex. if 2 and 3 switch values, then 3 will have the values 4 and 5 and those would switch
=> but then its 3 with 5 as its left children and 4 as its irght children
=> that solution is incorrect

breaking it down into each node's specific problem (since binary tree is recursive)
-> each node's left and right pointer should switch
=> if both None, don't have to do anything. 
=> if only one of them is None, still have to switch


don't need to return anything since its in place? not actually calculating anthing
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        left = root.left
        right = root.right
        root.right = left
        root.left = right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        






        