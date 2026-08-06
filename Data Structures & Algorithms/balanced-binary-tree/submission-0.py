# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
boolean binary tree problem

base case: 
- node is nullptr, return 0, can't be NOT height balanced
subcase:
- for each node, need to calc the height of left and right subtree, difference no greater than 1.
    - return false if this ever happens
=> what do you return? - BOOLEAN??, 

- DFS post order traversal, might calc left + right before you can preform work on the node itself
- should be returning the values, NOT boolean, boolean return happens in the work check


current problem: how do we preform the boolean checks and also return the heights
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_height_balanced = True
        def helper(root):
            nonlocal is_height_balanced
            if not is_height_balanced:
                return False
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            if abs(right - left) > 1:
                is_height_balanced = False
            return max(left, right) + 1


        helper(root)
        if not is_height_balanced:
            return False
        # happy path
        print(is_height_balanced)
        return True