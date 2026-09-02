# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- not a BFS solution
- do DFS solution
- need to return false from the top level function or the top level call of the function. 
- DFS just means we have to follow the same path between both p and q. and if they are the exact same tree, then the same path should be equal

constraints:
- don't call .left, .right, or .val on a node that's None. 
- for simplicity sake, you can also just call .left and .right for a node, even if it equals None. just make sure when you pop it from stack that you don't call the attributes on it
- make note that: 'not [obj]' is different from 'is None'

let's go with pre-order traversal. check the current node before you add it's left and right children so it stops at the top of the tree as soon as possible
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = []
        q_stack = []
        p_stack.append(p)
        q_stack.append(q)
        
        while p_stack and q_stack:
            curr_p = p_stack.pop()
            curr_q = q_stack.pop()

            # if they are both None, then we can continue
            if curr_p is None and curr_q is None:
                continue
            # only 1 exists or both exist and not equal then return false
            elif curr_p is None:
                return False
            elif curr_q is None:
                return False
            elif curr_p.val != curr_q.val:
                return False
            
            p_stack.append(curr_p.left)
            p_stack.append(curr_p.right)
            q_stack.append(curr_q.left)
            q_stack.append(curr_q.right)
        # they should both be empty. if one of them exists, then return False
        if p_stack or q_stack:
            return False
        return True