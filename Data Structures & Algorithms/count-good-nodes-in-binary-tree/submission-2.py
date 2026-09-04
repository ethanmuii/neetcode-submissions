# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- given a root, return the COUNT of good nodes in a tree
- what defines a good node: there is no node with a value greater than the bottom node itself (i.e leaf node for each scenario)
=> basically need to check the path for every node in the tree (from root to node) -> so need to keep track of global root value
- BINARY TREE just means it has a max of 2 children, no guarantees as to the sorting order of the nodes like where to search. 

constraints:
- each node needs to be aware of the nodes that are along its path. i.e its parent and its parent's parent. 
- instead of tracking the nodes in path, we technically only need to track the value that is the BIGGEST between this node and root. cuz we want to make sure that there is no nodes from root to node > than node x i.e node x should be the biggest value or equal the biggest value that node x. and if its bigger/equal to the max value along the path, its bigger than everything else

each recursive call should return the count of total good nodes (from itself and left and right subtree) and then it should also pass down to its child the max value.

edge case:
- guaranteed to have at least 1 node in the tree, no empty cases
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        root_val = root.val
        
        def recursion(root, max_value):
            if not root:
                return 0

            max_value = max(max_value, root.val)
            left_count = recursion(root.left, max_value)
            right_count = recursion(root.right, max_value)
            node_itself = 0
            if root.val >= max_value:
                node_itself = 1

            return left_count + right_count + node_itself




        total = recursion(root, root_val)
        return total