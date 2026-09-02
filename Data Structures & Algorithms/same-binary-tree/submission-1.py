# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- returning a boolean based on a condition

constraints:
- not knowing the values or the structure of both of the trees

edge cases:
- same structure and same values. we can compare the same structure and same vals by doing a BFS traversal through both of the trees at the same time. As soon as it disagrees, return False. If it gets through it all, then return True
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque()
        q_queue = deque()
        p_queue.append(p)
        q_queue.append(q)
        while p_queue and q_queue:
            for _ in range(len(p_queue)):
                node_p = p_queue.popleft()
                node_q = q_queue.popleft()

                if node_p is None and node_q is None:
                    continue

                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False
                p_queue.append(node_p.left)
                p_queue.append(node_p.right)
                q_queue.append(node_q.left)
                q_queue.append(node_q.right)
        return True