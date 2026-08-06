# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- our final return value needs to be a value that represents conditions of the whole tree. i.e a fact of the whole tree
=> can we perform this condition at each subroot (i.e not necessarily the given root but at each subtree)
=> number of good nodes within a tree is just number of good nodes from left subtree and right subtree. 
=> the final recursionn is + 1 since there will be no nodes greater than root from root to root

- the root in this problem is the OG root, not the recursive subroot
- since we are doing paths, BFS is probably not the best idea since it process level by level instead of by path

- DFS! -> preorder or postorder, not in order. 
- DUPLICATE VALUES ARE ALLOWED

some ideas:
- pass the max value seen along the recursive path so far in a helper function, and once you reach leaf nodes check if the value is bigger than max value seen along the path. -> if yes, then return the count of good nodes
=> at each node, the recursion should have a max value on that path, and the thing that gets returned is the count? and then it propogates up the left and right subtree where the count is the total number of good nodes that pass through this node.
=> WOULD YOU INCLUDE THE ACTUAL NODE ITSELF? -> yes, but it must consider only the values are higher and not values lower, so you should do PRE-ORDER TRAVERSAL
- you could also pass a list of values seen as well instead of an int, but this might take O(n) and then O(n^2)  total since max takes O(n) time.  

another idea:
- you could also just assume a path is good and greedily increment the count and if a value bigger comes along before it reaches the root, decrement the count and decrement it from the array, this might also take O(n^2) since you may have to iterate through this path list and compare past values you've seen to the node you are currently on right node which could invalidate a node. also harder since there is multiple paths (2) that go through a node and you would have to go through both. 
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root, max_value):
            nonlocal count
            if not root:
                return # can't increment or decrement count
            if root.val >= max_value:
                count += 1
                left = helper(root.left, root.val)
                right = helper(root.right, root.val)
            # the curr node is not >= max value, max stays the same
            else:
                left = helper(root.left, max_value)
                right = helper(root.right, max_value)

        helper(root, -101) # - 101 is the min value for this problem constraint
        return count
        