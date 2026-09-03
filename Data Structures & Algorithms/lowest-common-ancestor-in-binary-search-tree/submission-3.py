# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- BST means every node has max 2 children. 
- also means everything is in sorted order, and we should know where to look depending on how p and q compares to  the current node value we are at
- LCA: LOWEST node in tree where p AND Q are in subtrees or is the node value itself (for only one obviously)
- p and q for sure exist in the array

constraints:
- lowest hanging one means we want to go as far down as possible. technically root would be ancestor but isn't the lowest one
- pay attention to the difference between >, <, <=, and >=
=> an equal means one of the nodes is equal to it and this is our LCA

cases:
- if p and q is less than current value, we have to look left completely
- if p and q is greater than current value, then we have to look completely right. 
- the LCA happens when we have to split ways like one is less than and one is greater than

edge case:
- the node itself is one of p or q. in that case, its the LCA automatically. 
- p and/or q cannot be null. it must exist

since we are doing recursion we need to pass the variable up to the top of recursion
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def recursion(root):
            if p.val < root.val and q.val < root.val:
                ans = recursion(root.left)
                return ans
            elif p.val > root.val and q.val > root.val:
                ans = recursion(root.right)
                return ans
            elif p.val == root.val:
                return p
            elif q.val == root.val:
                return q
            else:
                return root

        return recursion(root)

        