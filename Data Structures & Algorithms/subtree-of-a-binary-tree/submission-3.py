# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
requirements:
- return bool if there is a subtree (i.e subroot and its left and right child trees) with same STRUCTURE AND NODE VALUES. i.e can't extend past/add more nodes beyond any node in the subroot and false otherwise
=> this means each node in the matched subtree must have the same value and children as that specific node in the subroot. 

constraints:
- brute force: for each node in root, do the process of checking if its value and its node descedents values match up exactly with subroot. the starting value is the "root" of the subtree that compares against the root of subroot and all the way down.  -> This process is O(m * n) where m represents the number of nodes in root, and n represents number of nodes in subRoot. since at a maximum, you are checking almost all the values in subroot for each node in the original root. 

- the key thing to note is that it should match from the bottom up for each node in root. => for example, there are guaranteed to be leaf nodes in subroot, the only possible VALID NODES that could match the subroot and its descendents are nodes with the same DEPTH as the subroot node. => Any node with a higher depth will have too many nodes and be extended too high. can also be extended too low like leaf nodes in subroot have children in a possible matched subroot.

KEY THINGS TO NOTE:
- if we are doing recursion, if we have to pass the STATE/RESULT: did we find subtree that matches subroot's exact structure
=> can't return False until we check ourselves as the possible match meaning we check our node value against subroot's root. HOWEVER, if the parent already gets 'TRUE' passed to it, that means one of its subtrees below found a valid match. 

- we need to continue the search if a node has same value and children as the equivalent node in subroot. 
=> DO we do top down or bottom up? 

how do i ensure im not rechecking? like how do the subcases build back up? 




edge cases:
- root of the tree can also be the answer (considered a subtree of itself)
- a subtree could have too many descendents meaning if a subset of its nodes match subroot, if they have different children like values instead of leaf nodes like in example 2, it could still be wrong. 

"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checker(p):
            p_stack = []
            q_stack = []
            p_stack.append(p)
            q_stack.append(subRoot)
            while p_stack and q_stack:
                node_p = p_stack.pop()
                if node_p and node_p.val == 0:
                    print("yes this happens")
                node_q = q_stack.pop()
                if node_p is None and node_q is None:
                    continue
                elif node_p is None or node_q is None:
                    return False
                elif node_p.val != node_q.val:
                    return False
                # 0, None
                # None, None
                p_stack.append(node_p.left)
                p_stack.append(node_p.right)
                q_stack.append(node_q.left)
                q_stack.append(node_q.right)
            if p_stack or q_stack:
                return False

            return True

        # call the above function on each possible subroot in the original tree leading to O(m) and the helper function is O(n)
        root_stack = [root]
        while root_stack:
            curr_subroot = root_stack.pop()
            if checker(curr_subroot):
                return True
            # if its false we just have to continue checking left and right nodes as long as they aren't node. don't have to check if both subRoot is None i.e empty tree since it guarantees at least 1 node
            if curr_subroot.left:
                root_stack.append(curr_subroot.left)
            elif curr_subroot.right:
                root_stack.append(curr_subroot.right)
        return False

        