# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- given the root of whole tree
- can technically access the whole tree if we wanted
- NOT any values that are right children, technically we want only the right nodes that are ont he OUTERMOST EDGE. 
=> recurse only the right subtree of every node? -> that will naturally get only the right side of the tree.
- we want a list of VALUES. -> list of value should be ordered top to bottom so pre-order. process current node before recursing the right subtree? or we can just reverse the list
- so we could do a nonlocal way like nested function, or we can pass a list as a parameter in a nested function


**COMPLETELY FORGOT that nodes can techically be on the left subtree or the left children but can still be visible from the right side view => because there is no nodes blocking it. 

KEY INSIGHT: a node is visible from the right side if it is the last node to be processed in a level.
=> since BFS or level-order traversal goes from the left to the right, the last node in each level is the node farthesr right on each level and it is the node that is in the "front" if you are looking at the tree from the right side
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque()
        # append the root to queue
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
