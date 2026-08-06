# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
given the left sub has nodes with keys less than and right sub only nodes with values greater than node's key => NO DUPLICATES IN BST

DFS, not BFS since we are using path checking.

recursion since we can split into smaller subcases.
- a node is a valid binary search tree if its left and right subtree are also binary search trees. i.e they return True
- base case: a null node is automatically a valid BST since it meets the first 2 conditions
- POST-ORDER TRAVERSAL since whether left and right subtrees are BST's depends on it?
- this how you get the value to propogate upwards. 
- do the node's checks after you check the left and right subtrees. 
=> this is because whether the node's children meet the BST property is irrelevant if the node's left subtree or right subtree already broke the invariant => thus even if the node's children meet property, f it breaks it down lower  it becomes invalid.

EDGE CASE MY THINKING FORGOT:
- a node itself could be a valid BST, but could have a children value that invalidates the BST of a higher root node or itself could invalidate the BST of a higher root node
=> what if you add checks for the smallest value in the right subtree should still be bigger than the root itself. and largest value in the left subtree should still be bigger than the root itself. 


MORE EDGE CASES:
- problem the min in the right subtree and max in the left subtree has to be respective to the avaliable values in their subtrees. it cannot be global.
- my code only checked only the rightmost values for the min values in a node's right subtrees and only the leftmost values for the max values in a node's left subtrees, ignoring all "inner" nodes in the node's subtrees. => NOT TRUE MAXS OR MINS
-> we have to actually pass the value in for each recursive call. 
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, interval):
            if not root:
                return True
            #print("root", root.val, "interval", interval)
            # check if current node is within bounds 
            # PRE ORDER DFS
            if root.val >= interval[1]:
                return False
            elif root.val <= interval[0]:
                return False

            left_bool = helper(root.left, [interval[0], max(interval[0], root.val)])
            right_bool = helper(root.right, [max(interval[0], root.val) , interval[1]])
            # left or right subtree is not valid
            if (not left_bool) or (not right_bool):
                return False

            # happy path (made it all the way thru)
            return True
        return helper(root, [-1000000000, 1000000000])
        
        
        
        
        
        
        
        
        
        
        
"""     
        # base case
        #max_value = 1000000001 # smallest value in right subtree
        #min_value = -1000000001  # largest value in left subtree
        def helper(root, smallest_val_right, largest_value_left):
            if not root:
                return True
            left_bool = helper(root.left, )
            right_bool = helper(root.right)
            if (not left_bool) or (not right_bool):
                return False

            # **ERROR with current code**: it onyl checks the farthesr right side for min on right subtree for top root and vice versa for the left side. 
            if root.left and root.left.val > min_value: 
                min_value = root.left.val
            if root.right and root.right.val < max_value:
                max_value = root.right.val

            if min_value >= root.val:
                return False
            elif max_value <= root.val:
                return False
            else:
                return True


        return helper(root, root.val + 1, root.val - 1)

# cases:
# update largest value in left subtree and smallest value in right subtree including node's children
# then check if smallest node in right subtree is less than root.val -> return False
# check if largest node in left subtree is less than root.val -> return False
# these conditions upheld because after updating the largest and smallest value including the node's direct children, it factors in these conditions of extreme checking
# if root is less than smallest value in right subtree, it will be smaller than the direct right children would have been the smallest value
"""