# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- level order traversal => BFS, need to process the tree level by level
- use queue FIFO
- work happening at each level, add a node to a sublist. 
- work done when we've finished processing a level and add that sublist to final list
- ADDING VALUES TO LIST, NOT NODES
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case
        if not root:
            return []
        
        queue = deque()
        ans = []
        # add root node to queue
        queue.append(root)
        while queue:
            size = len(queue)
            sublist = []
            for _ in range(size):
                node = queue.popleft()
                sublist.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sublist)
        return ans