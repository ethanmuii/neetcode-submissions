"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
requirements:
- need to make a DEEP COPY i.e call Node()
- the index in the adjList represents the Node value and identifies the node itself. 
=> starts from 1 to n where n = len(adjList), n inclusive.
- node.neighbors is node addy, not indexs.

constraints:
- we are given a list of neighbors so that means we only need to create that NODE ONCE, even if multiple nodes have it as a neighbor. use a visited set or hashmap key?
- value of the node can be described as the value in each list of the adj list. 
- a node can't be completed until its list of neighbors is all already created.

edge case: 
- nodes are not guaranteed to go in the correct order of dependencies. not required to follow a specific next pattern. like there's no node with zero dependencies
- graph could be 0 in which you should return none

solution insight:
- hashmap, key = local Node and deep code is key. 
- iterate once to create the NODES with vals
- iterate once again separately to create the neighbors. 

- need to reevaluate iteration logic. 
=> start at one node, then add its neighbor to stack if its not already created 
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {None: None} # trick to avoid setdefault
        stack = []
        visited = set()
        stack.append(node)
        visited.add(node)
        while stack:
            curr = stack.pop()
            hashmap[curr] = Node(curr.val, None)
            print(curr.val, hashmap[curr].val)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        hashmap.pop(None)
        # now need to create the neighbors:
        for key, value in hashmap.items():
            for neighbor in key.neighbors:
                value.neighbors.append(hashmap[neighbor])
        return hashmap[node]
        """
        for curr in node
            hashmap[curr] = Node(curr.val, None)
            curr = curr.next

        curr = node
        while curr:
            for neighbor in curr.neighbors:
                hashmap[curr].neighbors.append(hashmap[neighbor])
                curr = curr.next

        return hashmap[curr]
        """