# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
key words: ANCESTOR is allowed to be a descendent of itself. => if one of the node its a child of the parent, then the parent is the LCA.

in simple terms, what node has both of the node its subtree(s). either both left, both right, or left and right. the root of the subtree is included in the "subtree" itself. 

SUBTREE PROBLEM so DFS. not process level-by-level type of problem. => affects the ordering of the processing

you don't know if a node is an ancestor to both or yet the LCA until you see its left and right subtrees

1) if p and q are on the same side of rooted node, then the LCA is just p or q itself (regardless of right or left) as you go down the tree
2) if p and q are on separate sides of the rooted node, then LCA is just lowest node where p and q are in separate subtrees

POST-ORDER DFS?

ideas:
- return booleans (or the actual node themselves??) to tell if is a possible ancestor and then set the LCA to first one you see since post-order DFS will naturally check the higher ancestors last
- p and q are both guaranteed to exist in the tree

"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # a null node cannot be p or q or have it in any subtrees
        if not root:
            return None
        print("Current Node", root.val)
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # cases
        # value is not equal to p or q
        if (root != p and root != q) and (not left and not right):
            return None
        # the subroot subtree's don't contain p or q, but the subroot is p or q
        elif isinstance(left, TreeNode):
            return left
        elif isinstance(right, TreeNode):
            return right
        elif (root == p or root == q) and (not left and not right):
            return True
        elif (root == p or root == q) and (left is True or right is True):
            return root
        elif left is True and right is True:
            return root
        elif left is True or right is True:
            return True
