# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- return boolean if condition is met. 

constraints:
- need to know left and right subtrees to know if its balanaced or not. 
- the question is for each node, do you pass up the max subtree or min subtree from each child to the next root?  => must be the max for both? cna't be max and min? . def can't it be both min and min since it wouldn't properly check the condition i.e if both mins are zero, it would think balanced, but its not. 


- as soon as a node is unbalanced, no need to do more calculations, we just need to pass False back up to the top. => especially important because the top node's subtrees could technically be balanced if we are taking the max of each subtree, but a node further down could be unbalanced. 
- need to pass the max depth up so we can compare depths along with the condition of whether this node is balanced or not. If a below node is unbalanced, then the whole tree is unbalanced and we don't even need to do work.
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def recursion(root):
            # base case
            if not root:
                return 0, True

            # now do depth calculation work
            left_depth, right_balanced = recursion(root.left)
            right_depth, left_balanced = recursion(root.right)

            # compare depths
            if abs(right_depth - left_depth) > 1: # then this node is unbalanced
                return -1, False
            if not right_balanced or not left_balanced:
                return -1, False
            
            return max(left_depth, right_depth) + 1, True
                



        temp, ans = recursion(root)
        return ans