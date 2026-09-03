# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- return a list of vals that are the rightmost 

constraints
- viewable from the right side doesn't necessarily mean right child.
- it just means the right most node on each level => this can technically be a left child, if there is no nodes on that level to the right of it. it can even be on the lleft subtree as well. 

- ordered from top to bottom, means top-level starts with given root.

- getting the right most node at each level should use a BFS traversal. and the rightmost node could be the frist node in the level if we add right childs first. 
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == 0:
                    ans.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)

        return ans

        