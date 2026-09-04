# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- return bool if root is BST. the top node should bubble up the final answer
- a tree is BST if all of its subtrees are also their own BST -> this is how it breaks down into repetitive patterns
- tree is a BST if its left child is a valid BST AND its right child is a BST, and its left subtree of EVERY NODE is less than node's key and and right subtree of every node is GREATER than node's key

constraints:
- the whole left subtree must be less than the subroot not just the left child. this means for every node as a root, you need to track the MAX of its left subtree and the MIN of its right subtree. 


- the childs need to return/bubble up true or false of whether its a BST to the parent
- the left subtree of a node needs to bubble up its max left and the right subtree of a node needs to bubble up its max right
- you might need to pass down the current max's and min's too. 
- post-order traversal, you don't want to determine a node's bool until you see its left and right and then perform the check on the node itself


edge cases:
- duplicates are not allowed since it defeats the purpose of greater than/less than. 


how do you keep track of the max left and min right seen so far? 
- the left subtree should only return the max and the right subtree should only return the min for EACH node. 
- each node must bubble up the correct

- how do you make it so only the left size returns the max_left and right side only returns the min

- each node needs to pass up its max value and its min value. depending on which subtree then, the key node needs to be bigger than the left's max. and key node needs to be smaller than right subtree's min

what if you pass in the ranges for the left subtree and right subtree and that's a way to calculate min/max
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recursion(root):
            # Your insight: Openly bound None so it never fails a parent check
            if not root: 
                return True, float('-inf'), float('inf') 
            
            # Step 1: Check subtrees (no longer passing down constraints)
            is_left_valid, left_sub_max, left_sub_min = recursion(root.left)
            is_right_valid, right_sub_max, right_sub_min = recursion(root.right)
            
            # Step 2: If either subtree is invalid, bubble up failure immediately
            if not (is_left_valid and is_right_valid):
                return False, 0, 0 # Dummy values since the tree is already invalid
            
            # Step 3: Compare this node to the left max and right min
            if not (root.val > left_sub_max and root.val < right_sub_min):
                return False, 0, 0
                
            # Step 4: The node is valid! 
            # Now, how do we calculate this node's OWN max and min to return to its parent?
            actual_max = max(left_sub_max, right_sub_max, root.val)
            actual_min = min(left_sub_min, right_sub_min, root.val)
            return True, actual_max, actual_min

        # Kick off the recursion and only return the boolean to LeetCode
        is_valid_bst, actual_max, actual_min = recursion(root)
        return is_valid_bst
