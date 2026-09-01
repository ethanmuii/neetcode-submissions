# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- want the max diameter within the tree
- by definition, the longest path would be from the depth of left subtree + depth of right subtree. => however, the LONGEST path isn't always going to be the path through the root, it might be the path through a subroot as given in example 1. 


constraints:
- diameter can come from any path. path doesn't have to go through the root. it has to go through a node.
- the answer to the whole problem might not depend on the subcses of the original root i.e the longest path doesn't pass through the top root so its not just as simple as adding depth of left subtree + depth of right subtree of the root and propogating it back up. 
- ultimately the MAX length needs to get to the top root even if the diameter doesn't pass it. 
=> however, we can't just pass the MAX diameter see so far from the deepest subroot all the way to the top subroot. => this is because if we do this, how do we properly calculate the possible diameter of the root itself. it won't propogate up. 

INSIGHT, for every recursion we need to pass up the max depth whether its right/left subtree to the next node up in the tree because that will be its deepest path and the current MAX diameter seen so far. 
=> then at every node we calculate if our root's diameter is bigger than current Max Diameter. If it is, update it and return it, if it isn't then just keep on moving and pass it up. 
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def recursion(root, max_diameter):
            # base case
            if not root:
                return 0, max_diameter

            # can't calculate the diameter of root until we get its max from left and right subtrees
            left, max_diameter = recursion(root.left, max_diameter)
            right, max_diameter = recursion(root.right, max_diameter)

            current_diameter = left + right
            diameter = max(max_diameter, current_diameter)
            return max(left, right) + 1, diameter

        temp, ans = recursion(root, 0)
        return ans
        