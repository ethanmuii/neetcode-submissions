"""
requirements:
- n nodes, meaning nodes are numbered 0, 1, 2, 3, 4 if n = 5
- edges are undirected meaning connections forms both ways. 
- definition of connected component: there are separate connected components if you can't get from one node to another via any path way. if there are no avaliable paths then that node is considered seperated at least and any other nodes that it is connected is also considered separated

constraints:
- efficienctly checking if there is no way to get to one node to another via any path, definition of seprated components
- idea: build adjacency list, and run the traversal over that node if its not already in visited. if that node was already visited via another traversal then it was all connected. every time you have to call the traversal, it is a seperate component
- cycles are allowed? but technically to prevent infinite loops from cycles, need a visited set. 
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = {i: [] for i in range(n)}
        for edge in edges:
            node_1 = edge[0]
            node_2 = edge[1]
            adjacency_list[node_1].append(node_2)
            adjacency_list[node_2].append(node_1)

        # start the iteration of with node 0
        num_components = 0
        visited = set()
        for key, value in adjacency_list.items():
            if key not in visited:
                # then can perform the iteration and should increment num_components
                stack = []
                visited.add(key)
                num_components += 1
                for node in value:
                    stack.append((node, key)) # (new_node, prev_node)
                    visited.add(node)
                while stack:
                    curr_node, prev_node = stack.pop()
                    for node in adjacency_list[curr_node]:
                        if node != prev_node and node not in visited:
                            stack.append((node, curr_node))
                            visited.add(node)

        return num_components

                    