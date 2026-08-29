"""
requirements:
- n nodes = meaning the nodes are 0, 1, 2, 3, 4 if n = 5. 
- undirected edges, meaning the connections are both ways i.e 0 to 1 is same as 1 to 0. 
- returning a boolean
- what is a valid tree? -> i.e all nodes are connected i.e there is a path to get to every node from anywhere. -> NO ISOLATED NODES.
=> what defines an isolated node? a node that has no inbound/outbound connections (any connection since its undirected)

constraints:
- checking the connections a node has. 

solution insight:
- make an adjancency list, but make sure when you iterate thru edges, you add to both sides isnce undirected
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adjacency_list = {i: [] for i in range(n)}
        # iterate through edges and build the list
        for edge in edges:
            node_1 = edge[0]
            node_2 = edge[1]
            adjacency_list[node_1].append(node_2)
            adjacency_list[node_2].append(node_1)

        # now do a traversal
        stack = []
        visited = set()
        visited.add(0)
        for node in adjacency_list[0]:
            stack.append((node, 0)) # (new_node, prev_node)
            visited.add(node)
        print(adjacency_list)
        print(stack)
        
        while stack:
            new_node, prev_node = stack.pop()
            for node in adjacency_list[new_node]:
                if node != prev_node and node not in visited:
                    stack.append((node, new_node))
                    visited.add(node)
        
        if len(visited) == n:
            return True
        return False
