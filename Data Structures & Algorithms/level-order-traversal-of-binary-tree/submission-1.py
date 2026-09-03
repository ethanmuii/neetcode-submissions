# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- level order traversal means we want to process nodes level by level.
- each list should be a level, and we care about the node's value. don't add anything if its None. 

level order traversal means use a queue, just need to know which level a node is a part of it. can also do it DFS if you pass in the node's level with it. 
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue = deque([root])
        ans = []
        while queue:
            level = []
            for _ in range(len(queue)):
                top = queue.popleft()
                level.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            ans.append(level)

        return ans